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


class IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings(object):
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
        'max_connections': 'int',
        'connect_timeout': 'str',
        'tcp_keepalive': 'IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettingsTcpKeepalive'
    }

    attribute_map = {
        'max_connections': 'maxConnections',
        'connect_timeout': 'connectTimeout',
        'tcp_keepalive': 'tcpKeepalive'
    }

    def __init__(self, max_connections=None, connect_timeout=None, tcp_keepalive=None):  # noqa: E501
        """IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings - a model defined in OpenAPI"""  # noqa: E501

        self._max_connections = None
        self._connect_timeout = None
        self._tcp_keepalive = None
        self.discriminator = None

        if max_connections is not None:
            self.max_connections = max_connections
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if tcp_keepalive is not None:
            self.tcp_keepalive = tcp_keepalive

    @property
    def max_connections(self):
        """Gets the max_connections of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501

        Maximum number of HTTP1 /TCP connections to a destination host. Default 2^32-1.  # noqa: E501

        :return: The max_connections of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """Sets the max_connections of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.

        Maximum number of HTTP1 /TCP connections to a destination host. Default 2^32-1.  # noqa: E501

        :param max_connections: The max_connections of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501
        :type: int
        """

        self._max_connections = max_connections

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501

        TCP connection timeout.  # noqa: E501

        :return: The connect_timeout of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501
        :rtype: str
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.

        TCP connection timeout.  # noqa: E501

        :param connect_timeout: The connect_timeout of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501
        :type: str
        """

        self._connect_timeout = connect_timeout

    @property
    def tcp_keepalive(self):
        """Gets the tcp_keepalive of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501


        :return: The tcp_keepalive of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettingsTcpKeepalive
        """
        return self._tcp_keepalive

    @tcp_keepalive.setter
    def tcp_keepalive(self, tcp_keepalive):
        """Sets the tcp_keepalive of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.


        :param tcp_keepalive: The tcp_keepalive of this IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings.  # noqa: E501
        :type: IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettingsTcpKeepalive
        """

        self._tcp_keepalive = tcp_keepalive

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
        if not isinstance(other, IstioNetworkingV1alpha3ConnectionPoolSettingsTCPSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
