from bbquote.lib import get_quote

def test_getquote():
    assert type(get_quote()) == str