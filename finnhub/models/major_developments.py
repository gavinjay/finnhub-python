# coding: utf-8

"""
    Finnhub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from finnhub.configuration import Configuration


class MajorDevelopments(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'symbol': 'str',
        'major_development': 'list[object]'
    }

    attribute_map = {
        'symbol': 'symbol',
        'major_development': 'majorDevelopment'
    }

    def __init__(self, symbol=None, major_development=None, local_vars_configuration=None):  # noqa: E501
        """MajorDevelopments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol = None
        self._major_development = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if major_development is not None:
            self.major_development = major_development

    @property
    def symbol(self):
        """Gets the symbol of this MajorDevelopments.  # noqa: E501

        Company symbol.  # noqa: E501

        :return: The symbol of this MajorDevelopments.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this MajorDevelopments.

        Company symbol.  # noqa: E501

        :param symbol: The symbol of this MajorDevelopments.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def major_development(self):
        """Gets the major_development of this MajorDevelopments.  # noqa: E501

        Array of major developments.  # noqa: E501

        :return: The major_development of this MajorDevelopments.  # noqa: E501
        :rtype: list[object]
        """
        return self._major_development

    @major_development.setter
    def major_development(self, major_development):
        """Sets the major_development of this MajorDevelopments.

        Array of major developments.  # noqa: E501

        :param major_development: The major_development of this MajorDevelopments.  # noqa: E501
        :type: list[object]
        """

        self._major_development = major_development

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MajorDevelopments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MajorDevelopments):
            return True

        return self.to_dict() != other.to_dict()
