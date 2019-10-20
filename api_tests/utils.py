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


def validate_json_for_core_business(response):
    """Validate json content"""
    key_list = ['businessId', 'businessName', 'currencyCode', 'revenueCenters']
    found_keys = []
    for key, value in response.items():
        for item in value:
            for k, v in item.items():
                # assert all the keys are present
                if k in key_list and k not in found_keys:
                    found_keys.append(k)

                # assert value types are correct
                if k == 'businessId' or k == 'businessName' or k == 'currencyCode':
                    assert isinstance(v, str)
                elif k == 'revenueCenters':
                    assert isinstance(v, list)
    assert len(key_list) == len(found_keys)


def validate_json_for_summary_sales(response):
    """Validate json content"""
    key_list = ['organization', 'metrics', 'businessDay', 'currencyCode']
    found_keys = []

    for key, value in response.items():
        for item in value:
            for k, v in item.items():
                # assert all the keys are present
                if k in key_list and k not in found_keys:
                    found_keys.append(k)

                # assert value types are correct
                if k == 'organization' or k == 'metrics':
                    assert isinstance(v, dict)
                elif k == 'businessDay' or k == 'currencyCode':
                    assert isinstance(v, str)

    assert len(key_list) == len(found_keys)
