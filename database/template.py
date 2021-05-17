
DYNAMIC_TEMPLATE = {
    "settings": {
        # Allows for case-insensitive searches.
        "analysis": {
            "normalizer": {
                "lower_ascii_normalizer": {
                    "type": "custom",
                    "filter": [
                        "lowercase",
                        "asciifolding"
                    ]
                }
            }
        },
        "number_of_shards": 1,
        "number_of_replicas": 1,
    },
    "mappings": {
        "document": {
            "dynamic_templates": [
                {
                    "strings": {
                        "match_mapping_type": "string",
                        "mapping": {
                            "type": "keyword",
                            "normalizer": "lower_ascii_normalizer"
                        }
                    }
                }
            ]
        }
    }
}
