#!/usr/bin/env python3.7
###############################################################################

"""API test cases"""

from utils import call_api_with_retries
from utils import pretty_print_request
from utils import pretty_print_response
from utils import assert_valid_schema


INVALID_URL = 'http://127.0.0.1:9000/v1/invalid'
HEADERS = {'Content-Type': 'application/json'}

def test_get_core_businesses():
    """Verify the URL"""
    valid_url = 'http://127.0.0.1:9000/v1/core/businesses'

    resp = call_api_with_retries().get(url=valid_url, headers=HEADERS)
    pretty_print_request(resp.request)
    assert resp.status_code == 200
    pretty_print_response(resp)

    resp = call_api_with_retries().get(url=INVALID_URL, headers=HEADERS)
    pretty_print_request(resp.request)
    assert resp.status_code == 400
    pretty_print_response(resp)


def test_get_sales_summary_sales():
    """Verify the URL"""
    valid_url = 'http://127.0.0.1:9000/v1/sales/summary-sales'

    resp = call_api_with_retries().get(url=valid_url, headers=HEADERS)
    pretty_print_request(resp.request)
    assert resp.status_code == 200
    pretty_print_response(resp)

    resp = call_api_with_retries().get(url=INVALID_URL, headers=HEADERS)
    pretty_print_request(resp.request)
    assert resp.status_code == 400
    pretty_print_response(resp)


def test_get_businessids():
    """Verify the URL"""
    url = 'http://127.0.0.1:9000/v1/core/businesses/'
    invalid_business_id = 'foo'
    valid_business_id = '7047'

    resp = call_api_with_retries().get(url=url + valid_business_id, headers=HEADERS)
    pretty_print_request(resp.request)
    assert resp.status_code == 200
    pretty_print_response(resp)

    resp = call_api_with_retries().get(url=url + invalid_business_id, headers=HEADERS)
    pretty_print_request(resp.request)
    assert resp.status_code == 400
    pretty_print_response(resp)


def test_json_schema():
    """Validate the JSON response"""
    url = 'http://127.0.0.1:9000/v1/core/businesses'

    resp = call_api_with_retries().get(url=url, headers=HEADERS)
    pretty_print_request(resp.request)
    assert resp.status_code == 200

    pretty_print_response(resp)
    json_data = resp.json()

    assert_valid_schema(json_data, 'schema.json')
