import os


class Config:
    ES_HOST = os.environ.get('ES_HOST', 'localhost')
    ES_PORT = int(os.environ.get('ES_PORT', 9200))
    ES_DOC_TYPE = os.environ.get('ES_DOC_TYPE', 'document')
    ES_ZSCORES_INDEX = os.environ.get('ES_ZSCORES_INDEX', 'zscores')
    FINANCIAL_YEARS_COUNT = int(os.environ.get('FINANCIAL_YEARS_COUNT', 5))
    ZSCORE_X1_COEFFICIENT = os.environ.get('ZSCORE_X1_COEFFICIENT', 1.2)
    ZSCORE_X2_COEFFICIENT = os.environ.get('ZSCORE_X2_COEFFICIENT', 1.4)
    ZSCORE_X3_COEFFICIENT = os.environ.get('ZSCORE_X3_COEFFICIENT', 3.3)
    ZSCORE_X4_COEFFICIENT = os.environ.get('ZSCORE_X4_COEFFICIENT', 0.6)
    ZSCORE_X5_COEFFICIENT = os.environ.get('ZSCORE_X5_COEFFICIENT', 1.0)
