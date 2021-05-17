import pytest
from unittest.mock import Mock
from . import get, put
from ..mocked_payloads import (
    VALID_PAYLOAD,
    INVALID_PAYLOAD_TOO_FEW_YEARS,
    INVALID_PAYLOAD_TOO_MANY_YEARS,
    INVALID_PAYLOAD_TOTAL_LIABILITIES_IS_NULL,
    INVALID_PAYLOAD_TOTAL_ASSETS_IS_NULL,
    DATABASE_RESPONSE,
    EMPTY_DATABASE_RESPONSE)


def test_get_valid_query(monkeypatch):
    """
    Testing the z-score GET endpoint for a valid query.
    :param obj monkeypatch: a patching instance.
    """
    query_result = Mock(return_value=Mock(
        search=Mock(
            return_value=DATABASE_RESPONSE)))
    monkeypatch.setattr(
      'endpoints.zscore.ESClient', query_result)

    status_code, response_data = get(url='/company/gb/11223344',
                                     headers={
                                         'content-type': 'application/json'})
    assert response_data == {
	'scores': [{
		'year': 2020,
		'zscore': 6.144846255454092
	 }, {
		'year': 2019,
		'zscore': 6.395165589110549
	 }, {
		'year': 2018,
		'zscore': 6.216291793051449
	 }, {
		'year': 2017,
		'zscore': 5.975450833426112
	 }, {
		'year': 2016,
		'zscore': 13.484716441139247
	 }]
    }


def test_put_valid_query(monkeypatch):
    """
    Testing the z-score PUT endpoint for valid queries.
    """
    query_result = Mock(return_value=Mock(
        search=Mock(
            return_value={})))
    monkeypatch.setattr(
      'endpoints.zscore.ESClient', query_result)

    status_code, response_data = put(url='/company/fr/2233445566',
                                     data=VALID_PAYLOAD,
                                     headers={
                                         'content-type': 'application/json'})
    assert response_data == {
	'scores': [{
		'zscore': 6.144846255454092,
		'year': 2020
	}, {
		'zscore': 6.395165589110549,
		'year': 2019
	}, {
		'zscore': 6.216291793051449,
		'year': 2018
	}, {
		'zscore': 5.975450833426112,
		'year': 2017
	}, {
		'zscore': 13.484716441139247,
		'year': 2016
	}]
}


@pytest.mark.parametrize('query',
                         ['/company/not_country_code/not_integer',
                          '/company/US/not_integer',
                          '/US/1223344',
                          '/company'])
def test_get_invalid_queries(query):
    """
    Testing the z-score GET endpoint for invalid queries.
    n.b: here we expect 404 for all these requests as the format of the query
    does not match the contract.
    :param str query: a query instance.
    """
    status_code, response_data = get(url=query,
                                     headers={
                                         'content-type': 'application/json'})
    assert status_code == 404


@pytest.mark.parametrize('query',
                         ['/company/not_country_code/not_integer',
                          '/company/US/not_integer',
                          '/US/1223344',
                          '/company'])
def test_put_invalid_queries(query):
    """
    Testing the z-score PUT endpoint for invalid queries.
    n.b: here we expect 404 for all these requests as the format of the query
    does not match the contract.
    :param str query: a query instance.
    """
    status_code, response_data = put(url=query,
                                     data={},
                                     headers={
                                         'content-type': 'application/json'})
    assert status_code == 404


def test_get_zscores_no_response(monkeypatch):
    """
    Testing that an empty database response returns the right format.
    """
    query_result = Mock(return_value=Mock(
        search=Mock(
            return_value=EMPTY_DATABASE_RESPONSE)))
    monkeypatch.setattr(
        'endpoints.zscore.ESClient', query_result)

    status_code, response_data = get(url='/company/gb/1',
                                     headers={
                                         'content-type': 'application/json'})
    assert response_data == {'scores': []}


@pytest.mark.parametrize(
    'financials',
    [INVALID_PAYLOAD_TOO_FEW_YEARS,
     INVALID_PAYLOAD_TOO_MANY_YEARS])
def test_incorrect_financial_years_raise_validation_error(
        financials, monkeypatch):
    """
    Testing that if the number of financial years is not exactly the one
    defined in the task description, we raise a validation error.
    """
    query_result = Mock(return_value=Mock(
        search=Mock(
            return_value={})))
    monkeypatch.setattr(
      'endpoints.zscore.ESClient', query_result)

    status_code, response_data = put(url='/company/fr/2233445566',
                                     data=financials,
                                     headers={
                                         'content-type': 'application/json'})
    assert response_data == {'message':
                                 'Client error, please correct the request.',
                             'errors': {'financials': ['Length must be 5.']}}


@pytest.mark.parametrize(
    'financials, error',
    [(INVALID_PAYLOAD_TOTAL_ASSETS_IS_NULL,
      {'message': 'Client error, please correct the request.',
       'errors': {'financials': {'0':
                                     {'total_assets': ['Invalid input.']},
                                 '1':
                                     {'total_assets': ['Invalid input.']},
                                 '2':
                                     {'total_assets': ['Invalid input.']},
                                 '3':
                                     {'total_assets': ['Invalid input.']},
                                 '4':
                                     {'total_assets': ['Invalid input.']}}}}),
     (INVALID_PAYLOAD_TOTAL_LIABILITIES_IS_NULL,
      {'message': 'Client error, please correct the request.',
       'errors': {'financials': {'0':
                                     {'total_liabilities': ['Invalid input.']},
                                 '1':
                                     {'total_liabilities': ['Invalid input.']},
                                 '2':
                                     {'total_liabilities': ['Invalid input.']},
                                 '3':
                                     {'total_liabilities': ['Invalid input.']},
                                 '4':
                                     {'total_liabilities': ['Invalid input.']}
                                 }}})])
def test_null_totals_raise_validation_error(financials, error, monkeypatch):
    """

    :return:
    """
    query_result = Mock(return_value=Mock(
        search=Mock(
            return_value={})))
    monkeypatch.setattr(
      'endpoints.zscore.ESClient', query_result)

    status_code, response_data = put(url='/company/fr/2233445566',
                                     data=financials,
                                     headers={
                                         'content-type': 'application/json'})
    assert response_data == error
