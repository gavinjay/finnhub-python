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
from finnhub.models.price_target import PriceTarget  # noqa: E501
from finnhub.rest import ApiException

class TestPriceTarget(unittest.TestCase):
    """PriceTarget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PriceTarget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = finnhub.models.price_target.PriceTarget()  # noqa: E501
        if include_optional :
            return PriceTarget(
                symbol = '0', 
                target_high = 1.337, 
                target_low = 1.337, 
                target_mean = 1.337, 
                target_median = 1.337, 
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return PriceTarget(
        )

    def testPriceTarget(self):
        """Test PriceTarget"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
