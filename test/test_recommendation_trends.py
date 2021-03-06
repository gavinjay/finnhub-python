# coding: utf-8

"""
    Finnhub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import finnhub
from finnhub.models.recommendation_trends import RecommendationTrends  # noqa: E501
from finnhub.rest import ApiException

class TestRecommendationTrends(unittest.TestCase):
    """RecommendationTrends unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RecommendationTrends
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = finnhub.models.recommendation_trends.RecommendationTrends()  # noqa: E501
        if include_optional :
            return RecommendationTrends(
                symbol = '0', 
                buy = 56, 
                hold = 56, 
                period = '0', 
                sell = 56, 
                strong_buy = 56, 
                strong_sell = 56
            )
        else :
            return RecommendationTrends(
        )

    def testRecommendationTrends(self):
        """Test RecommendationTrends"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
