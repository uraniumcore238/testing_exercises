import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(('url', 'result'), [
    ('https://github.com/test/test/pull/1', True),
    ('https://github.com/test/test/pull/', True),
    ('https://github.com/test/test/pull/1/test', False),
    ('https://git.com/test/test/pull/1', False),
    ('https://github.com/test/test/no_pull/1', False),
    ('https://github.com/test/test/pull', False),

])
def test_four_sentiment(url, result):
    assert is_github_pull_request_url(url) == result
