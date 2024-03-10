import pytest

from functions.level_2.one_pr_url import is_github_pull_request_url


@pytest.mark.parametrize(('url', 'result'), [
    ('https://github.com/test/test/pull/1', True),
    ('https://github.com/test/test/pull/', True)
])
def test__one_pr_url__return_true_if_len_is_seven_github_on_third_and_pull_on_sixth_place_and_len_is_seven(url, result):
    assert is_github_pull_request_url(url) == result


@pytest.mark.parametrize(('url', 'result'), [
    ('https://github.com/test/test/pull/1/test', False),
    ('https://github.com/test/test/pull', False)
])
def test__one_pr_url__return_false_if_len_is_not_seven(url, result):
    assert is_github_pull_request_url(url) == result


@pytest.mark.parametrize(('url', 'result'), [
    ('https://git.com/test/test/pull/1', False),
    ('https://github.com/test/test/no_pull/1', False)
])
def test__one_pr_url__return_false_if_no_github_on_third_place_or_no_pul_on_sixth_place(url, result):
    assert is_github_pull_request_url(url) == result
