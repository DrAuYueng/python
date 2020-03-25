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


class IstioNetworkingV1alpha3ConnectionPoolSettings(object):
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
        'tcp': 'IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings',
        'http': 'IstioNetworkingV1alpha3ConnectionPoolSettingsHTTPSettings'
    }

    attribute_map = {
        'tcp': 'tcp',
        'http': 'http'
    }

    def __init__(self, tcp=None, http=None):  # noqa: E501
        """IstioNetworkingV1alpha3ConnectionPoolSettings - a model defined in OpenAPI"""  # noqa: E501

        self._tcp = None
        self._http = None
        self.discriminator = None

        if tcp is not None:
            self.tcp = tcp
        if http is not None:
            self.http = http

    @property
    def tcp(self):
        """Gets the tcp of this IstioNetworkingV1alpha3ConnectionPoolSettings.  # noqa: E501


        :return: The tcp of this IstioNetworkingV1alpha3ConnectionPoolSettings.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings
        """
        return self._tcp

    @tcp.setter
    def tcp(self, tcp):
        """Sets the tcp of this IstioNetworkingV1alpha3ConnectionPoolSettings.


        :param tcp: The tcp of this IstioNetworkingV1alpha3ConnectionPoolSettings.  # noqa: E501
        :type: IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings
        """

        self._tcp = tcp

    @property
    def http(self):
        """Gets the http of this IstioNetworkingV1alpha3ConnectionPoolSettings.  # noqa: E501


        :return: The http of this IstioNetworkingV1alpha3ConnectionPoolSettings.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3ConnectionPoolSettingsHTTPSettings
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this IstioNetworkingV1alpha3ConnectionPoolSettings.


        :param http: The http of this IstioNetworkingV1alpha3ConnectionPoolSettings.  # noqa: E501
        :type: IstioNetworkingV1alpha3ConnectionPoolSettingsHTTPSettings
        """

        self._http = http

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
        if not isinstance(other, IstioNetworkingV1alpha3ConnectionPoolSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other