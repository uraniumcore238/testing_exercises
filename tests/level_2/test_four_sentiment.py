import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(('text', 'result'), [
    ('good news', 'GOOD'),
    ('the best of the best news', 'GOOD'),
    ('good fff best news', 'GOOD')
])
def test__four_sentiment__return_good_if_good_words_more_than_bad(text, result):
    assert check_tweet_sentiment(text, {'good', 'better', 'best'}, {'f', 'ff', 'fff'}) == result


@pytest.mark.parametrize(('text', 'result'), [
    ('ff news', 'BAD'),
    ('f and fff news', 'BAD'),
    ('good f ff news', 'BAD')
])
def test__four_sentiment__return_bad_if_bad_words_more_than_good(text, result):
    assert check_tweet_sentiment(text, {'good', 'better', 'best'}, {'f', 'ff', 'fff'}) == result


@pytest.mark.parametrize(('text', 'result'), [
    ('normal news', None),
    ('good best f ff news', None)
])
def test__four_sentiment__return_none_if_quantity_of_good_and_bad_words_is_equal(text, result):
    assert check_tweet_sentiment(text, {'good', 'better', 'best'}, {'f', 'ff', 'fff'}) == result


@pytest.mark.parametrize(('text', 'result'), [
    ('', None),
    (' ', None)
])
def test__four_sentiment__return_none_if_no_words_in_text(text, result):
    assert check_tweet_sentiment(text, {'good', 'better', 'best'}, {'f', 'ff', 'fff'}) == result


def test__four_sentiment__return_none_if_good_list_is_empty_and_no_bad_verbs_in_text():
    assert check_tweet_sentiment('good news', {}, {'f', 'ff', 'fff'}) == None


def test__four_sentiment__return_none_if_bad_list_is_empty_and_no_good_verbs_in_text():
    assert check_tweet_sentiment('ff news', {'good', 'better', 'best'}, {}) == None


def test__four_sentiment__return_bad_if_good_list_is_empty_and_some_bad_verbs_in_text():
    assert check_tweet_sentiment('ff news', {}, {'f', 'ff', 'fff'}) == 'BAD'


def test__four_sentiment__return_good_if_bad_list_is_empty_and_some_good_verbs_in_text():
    assert check_tweet_sentiment('good news', {'good', 'better', 'best'}, {}) == 'GOOD'