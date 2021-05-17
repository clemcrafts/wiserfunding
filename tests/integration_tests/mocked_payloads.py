

VALID_PAYLOAD = {"financials": [
        {"year": 2020, "ebit": 123.45, "equity": 234.56,
         "retained_earnings": 345.67, "sales": 1234.56, "total_assets": 345.67,
         "total_liabilities": 456.78},
        {"year": 2019, "ebit": 122.63, "equity": 224.56,
         "retained_earnings": 325.33, "sales": 1214.99, "total_assets": 325.04,
         "total_liabilities": 426.78},
        {"year": 2018, "ebit": 120.17, "equity": 214.06,
         "retained_earnings": 225.00, "sales": 1204.01, "total_assets": 305.11,
         "total_liabilities": 426.78},
        {"year": 2017, "ebit": 118.23, "equity": 204.96,
         "retained_earnings": 125.97, "sales": 1200.00, "total_assets": 290.75,
         "total_liabilities": 426.78},
        {"year": 2016, "ebit": 116.05, "equity": 234.56,
         "retained_earnings": 105.11, "sales": 1010.82, "total_assets": 250.13,
         "total_liabilities": 42.78}]}

INVALID_PAYLOAD_TOTAL_ASSETS_IS_NULL = {"financials": [
        {"year": 2020, "ebit": 123.45, "equity": 234.56,
         "retained_earnings": 345.67, "sales": 1234.56, "total_assets": 0.0,
         "total_liabilities": 456.78},
        {"year": 2019, "ebit": 122.63, "equity": 224.56,
         "retained_earnings": 325.33, "sales": 1214.99, "total_assets": 0.0,
         "total_liabilities": 426.78},
        {"year": 2018, "ebit": 120.17, "equity": 214.06,
         "retained_earnings": 225.00, "sales": 1204.01, "total_assets": 0.0,
         "total_liabilities": 426.78},
        {"year": 2017, "ebit": 118.23, "equity": 204.96,
         "retained_earnings": 125.97, "sales": 1200.00, "total_assets": 0.0,
         "total_liabilities": 426.78},
        {"year": 2016, "ebit": 116.05, "equity": 234.56,
         "retained_earnings": 105.11, "sales": 1010.82, "total_assets": 0.0,
         "total_liabilities": 42.78}]}

INVALID_PAYLOAD_TOTAL_LIABILITIES_IS_NULL = {"financials": [
        {"year": 2020, "ebit": 123.45, "equity": 234.56,
         "retained_earnings": 345.67, "sales": 1234.56, "total_assets": 345.67,
         "total_liabilities": 0.0},
        {"year": 2019, "ebit": 122.63, "equity": 224.56,
         "retained_earnings": 325.33, "sales": 1214.99, "total_assets": 325.04,
         "total_liabilities": 0.0},
        {"year": 2018, "ebit": 120.17, "equity": 214.06,
         "retained_earnings": 225.00, "sales": 1204.01, "total_assets": 305.11,
         "total_liabilities": 0.0},
        {"year": 2017, "ebit": 118.23, "equity": 204.96,
         "retained_earnings": 125.97, "sales": 1200.00, "total_assets": 290.75,
         "total_liabilities": 0.0},
        {"year": 2016, "ebit": 116.05, "equity": 234.56,
         "retained_earnings": 105.11, "sales": 1010.82, "total_assets": 250.13,
         "total_liabilities": 0.0}]}

INVALID_PAYLOAD_TOO_FEW_YEARS = {"financials": [
        {"year": 2020, "ebit": 123.45, "equity": 234.56,
         "retained_earnings": 345.67, "sales": 1234.56, "total_assets": 345.67,
         "total_liabilities": 456.78},
        {"year": 2019, "ebit": 122.63, "equity": 224.56,
         "retained_earnings": 325.33, "sales": 1214.99, "total_assets": 325.04,
         "total_liabilities": 426.78}]}

INVALID_PAYLOAD_TOO_MANY_YEARS = {"financials": [
        {"year": 2020, "ebit": 123.45, "equity": 234.56,
         "retained_earnings": 345.67, "sales": 1234.56, "total_assets": 345.67,
         "total_liabilities": 456.78},
        {"year": 2019, "ebit": 122.63, "equity": 224.56,
         "retained_earnings": 325.33, "sales": 1214.99, "total_assets": 325.04,
         "total_liabilities": 426.78},
        {"year": 2018, "ebit": 120.17, "equity": 214.06,
         "retained_earnings": 225.00, "sales": 1204.01, "total_assets": 305.11,
         "total_liabilities": 426.78},
        {"year": 2017, "ebit": 118.23, "equity": 204.96,
         "retained_earnings": 125.97, "sales": 1200.00, "total_assets": 290.75,
         "total_liabilities": 426.78},
        {"year": 2016, "ebit": 116.05, "equity": 234.56,
         "retained_earnings": 105.11, "sales": 1010.82, "total_assets": 250.13,
         "total_liabilities": 42.78},
        {"year": 2015, "ebit": 116.05, "equity": 234.56,
         "retained_earnings": 105.11, "sales": 1010.82, "total_assets": 250.13,
         "total_liabilities": 42.78}]}

DATABASE_RESPONSE = {
    "took": 48,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 1,
            "relation": "eq"
        },
        "max_score": 1.0,
        "hits": [
            {
                "_index": "zscore",
                "_type": "document",
                "_id": "gb11223344",
                "_score": 1.0,
                "_source": {
                    "2020": 6.144846255454092,
                    "2019": 6.395165589110549,
                    "2018": 6.216291793051449,
                    "2017": 5.975450833426112,
                    "2016": 13.484716441139247
                }
            }
        ]
      }
    }


EMPTY_DATABASE_RESPONSE = {
        "took": 9,
        "_shards": {
            "total": 1,
            "successful": 1,
            "skipped": 0,
            "failed": 0
        },
        "hits": {
            "total": {
                "value": 0,
                "relation": "eq"
            },
            "hits": []
        }
    }
