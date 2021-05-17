import boto3, time
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch.exceptions import NotFoundError, RequestError
from requests_aws4auth import AWS4Auth
from database.template import DYNAMIC_TEMPLATE
from logger import logger
from config import Config


class ESClient(Elasticsearch):
    """
    Elasticsearch database client extending the generic library one and
    passing the right configuration parameters for AWS.
    """
    def __init__(self):
        credentials = boto3.Session().get_credentials()
        aws_auth = None
        hosts = [{'host': Config.ES_HOST, 'port': Config.ES_PORT}]
        if credentials:
            aws_auth = AWS4Auth(credentials.access_key,
                                credentials.secret_key,
                                boto3.Session().region_name, 'es',
                                session_token=credentials.token)
        super().__init__(
            hosts=hosts,
            http_auth=aws_auth,
            use_ssl=False,
            verify_certs=True,
            connection_class=RequestsHttpConnection)


    def search(self, **kwargs):
        """
        Wrapping the native search method with an error handler.
        :param kwargs: parameters for the ES request.
        :return dict results: ES results for the request.
        """
        try:
            return super().search(**kwargs)
        except (NotFoundError, RequestError) as error:
            logger.warn(error)
            return {}

    def create_index(self, wait=10):
        """
        Creating the ES index used to store the z-scores.
        If it does already exist, it will be skipped.
        :param int wait: waiting time in seconds before creating the index.
        """
        try:
            time.sleep(wait)
            self.indices.create('zscores', body=DYNAMIC_TEMPLATE)
        except Exception as error:
            logger.warn(error)
