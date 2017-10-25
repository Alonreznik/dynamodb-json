import os
import sys

from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    # Remove old distributions
    dist_ = 'dist'
    for f in os.listdir(dist_):
        file_path = os.path.join(dist_, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

    os.system('python setup.py sdist')
    os.system('python setup.py bdist_wheel')
    os.system('python setup.py register -r https://pypi.python.org/pypi')
    os.system('twine upload dist/* -r pypi')
    print("Make a tag to me")
    print("  git tag -a {0} -m 'version {0}'".format(__import__('dynamodb_json').__version__))
    print("  git push --tags")
    sys.exit()

install_requires = [
    'simplejson>=3.10.0',
    'boto3>=1.4.0',
    'six'
]

setup(
    name='dynamodb-json',
    version=__import__('dynamodb_json').__version__,
    packages=find_packages(),
    url='https://github.com/Alonreznik/dynamodb-json',
    author='Alon Reznik',
    author_email='alonreznik@gmail.com',
    description='A DynamoDB json util from and to python objects',
    long_description=open('README.md').read(),
    zip_safe=False,
    license='Mozilla',
    keywords='python dynamodb amazon json aws',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],
)
