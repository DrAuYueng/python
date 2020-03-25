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


class IstioNetworkingV1alpha3HTTPRewrite(object):
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
        'uri': 'str',
        'authority': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'authority': 'authority'
    }

    def __init__(self, uri=None, authority=None):  # noqa: E501
        """IstioNetworkingV1alpha3HTTPRewrite - a model defined in OpenAPI"""  # noqa: E501

        self._uri = None
        self._authority = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if authority is not None:
            self.authority = authority

    @property
    def uri(self):
        """Gets the uri of this IstioNetworkingV1alpha3HTTPRewrite.  # noqa: E501

        rewrite the path (or the prefix) portion of the URI with this value. If the original URI was matched based on prefix, the value provided in this field will replace the corresponding matched prefix.  # noqa: E501

        :return: The uri of this IstioNetworkingV1alpha3HTTPRewrite.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this IstioNetworkingV1alpha3HTTPRewrite.

        rewrite the path (or the prefix) portion of the URI with this value. If the original URI was matched based on prefix, the value provided in this field will replace the corresponding matched prefix.  # noqa: E501

        :param uri: The uri of this IstioNetworkingV1alpha3HTTPRewrite.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def authority(self):
        """Gets the authority of this IstioNetworkingV1alpha3HTTPRewrite.  # noqa: E501

        rewrite the Authority/Host header with this value.  # noqa: E501

        :return: The authority of this IstioNetworkingV1alpha3HTTPRewrite.  # noqa: E501
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this IstioNetworkingV1alpha3HTTPRewrite.

        rewrite the Authority/Host header with this value.  # noqa: E501

        :param authority: The authority of this IstioNetworkingV1alpha3HTTPRewrite.  # noqa: E501
        :type: str
        """

        self._authority = authority

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
        if not isinstance(other, IstioNetworkingV1alpha3HTTPRewrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
