import os
import sys

from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    print("Make a tag to me")
    print("  git tag -a {0} -m 'version {0}'".format(__import__('pynamodb').__version__))
    print("  git push --tags")
    sys.exit()

install_requires = [
    'simplejson',
    'boto3',
]

setup(
    name='dynamodb_json',
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
        'Development Status :: 1',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Mozilla',
    ],
)