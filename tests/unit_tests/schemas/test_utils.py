from schemas.utils import get_zscore


def test_get_zscore():
    """
    Testing the z-score calculation.
    """
    financial = {"year": 2020,
                 "ebit": 123.45,
                 "equity": 234.56,
                 "retained_earnings": 345.67,
                 "sales": 1234.56,
                 "total_assets": 345.67,
                 "total_liabilities": 456.78}
    assert get_zscore(financial) == 6.07242023479448
