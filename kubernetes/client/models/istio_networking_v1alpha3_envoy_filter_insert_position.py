# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class IstioNetworkingV1alpha3EnvoyFilterInsertPosition(object):
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
        'index': 'str',
        'relative_to': 'str'
    }

    attribute_map = {
        'index': 'index',
        'relative_to': 'relativeTo'
    }

    def __init__(self, index=None, relative_to=None):  # noqa: E501
        """IstioNetworkingV1alpha3EnvoyFilterInsertPosition - a model defined in OpenAPI"""  # noqa: E501

        self._index = None
        self._relative_to = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if relative_to is not None:
            self.relative_to = relative_to

    @property
    def index(self):
        """Gets the index of this IstioNetworkingV1alpha3EnvoyFilterInsertPosition.  # noqa: E501

        Index/position in the filter chain.  # noqa: E501

        :return: The index of this IstioNetworkingV1alpha3EnvoyFilterInsertPosition.  # noqa: E501
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this IstioNetworkingV1alpha3EnvoyFilterInsertPosition.

        Index/position in the filter chain.  # noqa: E501

        :param index: The index of this IstioNetworkingV1alpha3EnvoyFilterInsertPosition.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRST", "LAST", "BEFORE", "AFTER"]  # noqa: E501
        if index not in allowed_values:
            raise ValueError(
                "Invalid value for `index` ({0}), must be one of {1}"  # noqa: E501
                .format(index, allowed_values)
            )

        self._index = index

    @property
    def relative_to(self):
        """Gets the relative_to of this IstioNetworkingV1alpha3EnvoyFilterInsertPosition.  # noqa: E501

        If BEFORE or AFTER position is specified, specify the name of the filter relative to which this filter should be inserted.  # noqa: E501

        :return: The relative_to of this IstioNetworkingV1alpha3EnvoyFilterInsertPosition.  # noqa: E501
        :rtype: str
        """
        return self._relative_to

    @relative_to.setter
    def relative_to(self, relative_to):
        """Sets the relative_to of this IstioNetworkingV1alpha3EnvoyFilterInsertPosition.

        If BEFORE or AFTER position is specified, specify the name of the filter relative to which this filter should be inserted.  # noqa: E501

        :param relative_to: The relative_to of this IstioNetworkingV1alpha3EnvoyFilterInsertPosition.  # noqa: E501
        :type: str
        """

        self._relative_to = relative_to

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
        if not isinstance(other, IstioNetworkingV1alpha3EnvoyFilterInsertPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other