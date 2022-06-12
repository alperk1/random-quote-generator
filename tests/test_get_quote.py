from random_quote_generator import get_quote, topla
from random_quote_generator.quotes import quotes


def test_get_quote():
    """
    GIVEN
    WHEN get_quote is called
    THEN random quote from quotes is returned
    """

    quote = get_quote()

    assert quote in quotes


def test_topla():
    x = 10
    y = 15
    toplam = topla(x, y)
    assert toplam == 25

    x = 10
    y = -5
    toplam = topla(x, y)
    assert toplam == 5
