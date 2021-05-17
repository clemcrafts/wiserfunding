from flask_restful import Resource
from schemas.zscore import ZscoreQuery, ZscoreResponse
from webargs.flaskparser import use_args
from database.database import ESClient
from config import Config


class Zscore(Resource):
    """
    Class in charge of the Z-scores endpoints.
    n.b: Z-Score is a scalar predicting the likelihood of a bankruptcy for
    a company. For more details, see task PDF.
    """

    @use_args(ZscoreQuery)
    def put(self, args, **parameters):
        """
        PUT endpoint, calculating and storing the Z-scores.
        n.b: The update will overwrite the former Z-scores. This behaviour
        could be discussed and challenged depending on the use.
        :param dict args: the financial arguments in JSON format.
        :param dict parameters: the URL parameters in the query.
        :return list z_scores: The Z-scores calculated for the company.
        """
        return ZscoreResponse().dump(self._store(
            ZscoreResponse(unknown='EXCLUDE').load(data=args), parameters))

    def get(self, **parameters):
        """
        GET endpoint, returning the Z-scores previously calculated and stored.
        n.b: The database errors are handled at the client level.
        :param args parameters: the URL parameters in the query.
        :return list z_scores: The Z-scores stored for the company.
        """
        try:
            records = self._search(parameters)["hits"]["hits"][0]['_source']
        except (KeyError, IndexError):
            return {'scores': []}
        return ZscoreResponse().dump(
            {'scores':
                 [{'zscore': records[year], 'year': year}
                  for year in records.keys()]})

    def _store(self, scores, parameters):
        """
        Storing a list of Z-score payloads.
        n.b: The database errors are handled at the client level.
        :param dict scores: Z-score payloads.
        """
        ESClient().create(
            doc_type=Config.ES_DOC_TYPE,
            index=Config.ES_ZSCORES_INDEX,
            id=parameters['country_code'] + str(parameters['company_id']),
            body={s['year']: s['zscore'] for s in scores['scores']})
        return scores

    def _search(self, parameters):
        """
        Search a list of Z-score payloads
        :return dict z-scores: z-scores search results from Elasticsearch.
        """
        return ESClient().search(
         doc_type=Config.ES_DOC_TYPE,
         index=Config.ES_ZSCORES_INDEX,
         body={"query": {
               "term": {
               "_id": parameters['country_code']
                      + str(parameters['company_id'])
                 }
                }
              })
