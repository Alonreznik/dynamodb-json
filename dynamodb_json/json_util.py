import re
import uuid
from decimal import Decimal
import six
import sys
from datetime import datetime, date
import simplejson as json
from boto3.dynamodb.types import TypeSerializer


def json_serial(o):
    if isinstance(o, datetime):
        serial = o.strftime('%Y-%m-%dT%H:%M:%S.%f')
    elif isinstance(o, date):
        serial = o.strftime('%Y-%m-%d')
    elif isinstance(o, Decimal):
        if o % 1 > 0:
            serial = float(o)
        elif six.PY3:
            serial = int(o)
        elif o < sys.maxsize:
            serial = int(o)
        else:
            serial = long(o)
    elif isinstance(o, uuid.UUID):
        serial = str(o.hex)
    elif isinstance(o, set):
        serial = list(o)
    else:
        serial = o
    return serial


def dumps(dct, as_dict=False, **kwargs):
    """ Dump the dict to json in DynamoDB Format
        You can use any other simplejson or json options
        :param dct - the dict to dump
        :param as_dict - returns the result as python dict (useful for DynamoDB boto3 library) or as json sting
        :returns: DynamoDB json format.
        """

    result_ = TypeSerializer().serialize(json.loads(json.dumps(dct, default=json_serial),
                                                    use_decimal=True))
    if as_dict:
        return next(six.iteritems(result_))[1]
    else:
        return json.dumps(next(six.iteritems(result_))[1], **kwargs)


def object_hook(dct):
    """ DynamoDB object hook to return python values """
    try:
        # AttributeValue objects always have exactly one type key.
        if len(dct) == 1:
            key, value = next(six.iteritems(dct))
            # First - Try to parse the dct as DynamoDB AttributeValue wrapper.
            if key == 'BOOL':
                return value
            if key == 'S':
                try:
                    return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                except:
                    return str(value)
            if key == 'SS':
                return list(value)
            if key == 'N':
                if re.match(r"^-?\d+?\.\d+?$", value) is not None:
                    return float(value)
                else:
                    try:
                        return int(value)
                    except:
                        return int(value)
            if key == 'B':
                return str(value)
            if key == 'NS':
                return set(value)
            if key == 'BS':
                return set(value)
            if key == 'M':
                return value
            if key == 'L':
                return value
            if key == 'NULL' and value is True:
                return None
    except:
        return dct

    # In a Case of returning a regular python dict
    for key, val in six.iteritems(dct):
        if isinstance(val, six.string_types):
            try:
                dct[key] = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
            except:
                # This is a regular Basestring object
                pass

        if isinstance(val, Decimal):
            if val % 1 > 0:
                dct[key] = float(val)
            elif six.PY3:
                dct[key] = int(val)
            elif val < sys.maxsize:
                dct[key] = int(val)
            else:
                dct[key] = long(val)

    return dct


def loads(s, as_dict=False, *args, **kwargs):
    """ Loads dynamodb json format to a python dict.
        :param s - the json string or dict (with the as_dict variable set to True) to convert
        :returns python dict object
    """
    if as_dict or (not isinstance(s, six.string_types)):
        s = json.dumps(s)
    kwargs['object_hook'] = object_hook
    return json.loads(s, *args, **kwargs)
