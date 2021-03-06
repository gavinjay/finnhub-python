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
from finnhub.models.report import Report  # noqa: E501
from finnhub.rest import ApiException

class TestReport(unittest.TestCase):
    """Report unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Report
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = finnhub.models.report.Report()  # noqa: E501
        if include_optional :
            return Report(
                access_number = '0', 
                symbol = '0', 
                cik = '0', 
                year = 56, 
                quarter = 56, 
                form = '0', 
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                filed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                accepted_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                report = None
            )
        else :
            return Report(
        )

    def testReport(self):
        """Test Report"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
