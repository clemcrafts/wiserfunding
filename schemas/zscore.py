from marshmallow import fields, Schema, post_dump, pre_load, post_load
from marshmallow.validate import Length, NoneOf
from schemas.utils import get_zscore
from config import Config


class Financial(Schema):
    year = fields.Integer(required=True)
    ebit = fields.Float(required=True)
    equity = fields.Float(required=True)
    retained_earnings = fields.Float(required=True)
    sales = fields.Float(required=True)
    total_assets = fields.Float(validate=NoneOf([0]), required=True)
    total_liabilities = fields.Float(validate=NoneOf([0]), required=True)


class Score(Schema):
    year = fields.Integer()
    zscore = fields.Float()


class ZscoreQuery(Schema):
    financials = fields.Nested(
        Financial, many=True,
        validate=Length(equal=Config.FINANCIAL_YEARS_COUNT))


class ZscoreResponse(Schema):
    scores = fields.Nested(Score, many=True)

    @pre_load
    def pre_load(self, financials, **kwargs):
        """
        Formatting the fields for the response and calculating the z-score.
        n.b: the mysterious **kwargs argument is mandatory in Marshmallow 3.x
        even if not used.
        :param dict financials: the financials received from the user.
        :return dict response: the response payload to be validated
        """
        resp = {'scores': []}
        for f in financials['financials']:
            resp['scores'].append({'year': f['year'], 'zscore': get_zscore(f)})
        return resp
