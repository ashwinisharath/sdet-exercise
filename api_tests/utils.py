#!/usr/bin/env python3.7
###############################################################################

"""Utils file"""
import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from os.path import join, dirname
from jsonschema import validate


def call_api_with_retries():
    """ Call the api with retries """
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1)
    session.mount('https://', HTTPAdapter(max_retries=retries))
    return session


def pretty_print_request(request):
    """Pretty print the request"""
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )


def pretty_print_response(response):
    """Pretty print the response body"""
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )


def assert_valid_schema(data, schema_file):
    """ Checks whether the given data matches the schema """

    schema = load_json_schema(schema_file)
    return validate(data, schema)


def load_json_schema(filename):
    """ Loads the given schema file """

    relative_path = join(filename)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())