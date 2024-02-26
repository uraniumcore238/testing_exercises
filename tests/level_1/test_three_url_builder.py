import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(('host', 'relative_url', 'get_params', 'result'), [
    ('host', 'relative_url', {"key1": "param1", "key2": "param2"}, 'host/relative_url?key1=param1&key2=param2'),
    ('https://example.com', 'relative_url', {"key1": "PARAM1", "key2": "PARAM2"}, 'https://example.com/relative_url?key1=PARAM1&key2=PARAM2'),
    ('http://example.com', 'path/to/resource', {"key1": "param1", "key2": "param&2"}, 'http://example.com/path/to/resource?key1=param1&key2=param&2'),
    ('!@#$%^&*()_+|}/*-+~`<>?', '!@#$%^&*()_+|}/*-+~`<>?', {"key1": "!@#$%^&*()_+|}/*-+~`<>?", "key2": "!@#$%^&*()_+|}/*-+~`<>?"}, '!@#$%^&*()_+|}/*-+~`<>?/!@#$%^&*()_+|}/*-+~`<>??key1=!@#$%^&*()_+|}/*-+~`<>?&key2=!@#$%^&*()_+|}/*-+~`<>?')
])
def test_build_url(host, relative_url, get_params, result):
    assert (build_url(host, relative_url, get_params) == result)


@pytest.mark.parametrize(('host', 'relative_url', 'get_params', 'result'), [
    ('http://example.com', '', {"key1": "param1", "key2": "param2"}, 'http://example.com/?key1=param1&key2=param2'),
    ('', '', {"key1": "param1", "key2": "param2"}, '/?key1=param1&key2=param2'),
    ('http://example.com', 'path/to/resource', {"key1": "", "key2": "param2"}, 'http://example.com/path/to/resource?key1=&key2=param2'),
    ('http://example.com', 'path/to/resource', {"key1": "param1", "": "param2"}, 'http://example.com/path/to/resource?key1=param1&=param2'),
    ('', '', {"": "", "": ""}, '/?=')
])
def test_build_url_with_empty_data(host, relative_url, get_params, result):
    assert (build_url(host, relative_url, get_params) == result)
