from flask_restful import Resource


class ServiceStatus(Resource):
    """
    Class in charge of the WiseFunding API status (health check).
    """
    def get(self):
        """
        GET endpoint for health check purposes.
        :return dict health_check: returned if the WiseFunding API is alive.
        """
        return {'alive': True}
