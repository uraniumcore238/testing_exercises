from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('host', 'relative_url', {"key1": "param1", "key2": "param2"}) == 'host/relative_url?key1=param1&key2=param2'
