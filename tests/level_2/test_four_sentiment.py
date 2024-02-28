import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(('text', 'result'), [
    ('good news', 'GOOD'),
    ('the best of the best news', 'GOOD'),
    ('good fff best news', 'GOOD'),
    ('ff news', 'BAD'),
    ('f and fff news', 'BAD'),
    ('good f ff news', 'BAD'),
    ('normal news', None),
    ('good best f ff news', None)
])
def test_four_sentiment(text, result):
    assert check_tweet_sentiment(text, {'good', 'better', 'best'}, {'f', 'ff', 'fff'}) == result
