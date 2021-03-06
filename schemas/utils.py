from config import Config


def get_zscore(financial):
    """
    Calculating the z-score for a given financial year of a company.
    The terms here are not really defined and can lead to confusion
    (maybe part of the test) but "working capital" seems to be *current* assets
    - *current* liabilities however the only fields available here are
    *total* assets - *total* liabilities. This operation would give "equity"
    not "working capital". However the field "equity" is not equal to that
    difference either. I've decided to not spend too much time over-thinking
    this, and used working_capital = total assets - total liabilities.
    Formula: Z = 1.2X1 + 1.4X2 + 3.3X3 + 0.6X4 + 1.0X5
    X1 = working_capital / total_assets
    X2 = retained_earnings / total_assets
    X3 = ebit / total_assets
    X4 = equity / total_liabilities
    X5 = sales / total_assets
    n.b: the total assets and liabilities can't be null, we validate them
    beforehand at the reception of the payload.
    :param dict financial: financial year report of a company for a given year.
    e.g: {'equity': 3000, .... , 'total_liability: 1400}
    :return float zscore: the z-score for this company for a given year.
    """
    x_1 = (financial['total_assets'] -
           financial['total_liabilities']) / financial['total_assets']
    x_2 = financial['retained_earnings'] / financial['total_assets']
    x_3 = financial['ebit'] / financial['total_assets']
    x_4 = financial['equity'] / financial['total_liabilities']
    x_5 = financial['sales'] / financial['total_assets']
    return (Config.ZSCORE_X1_COEFFICIENT * x_1 +
            Config.ZSCORE_X2_COEFFICIENT * x_2 +
            Config.ZSCORE_X3_COEFFICIENT * x_3 +
            Config.ZSCORE_X4_COEFFICIENT * x_4 +
            Config.ZSCORE_X5_COEFFICIENT * x_5)
