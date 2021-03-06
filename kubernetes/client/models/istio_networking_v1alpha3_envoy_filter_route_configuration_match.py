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


class IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch(object):
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
        'name': 'str',
        'port_number': 'int',
        'port_name': 'str',
        'gateway': 'str',
        'vhost': 'IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatchVirtualHostMatch'
    }

    attribute_map = {
        'name': 'name',
        'port_number': 'portNumber',
        'port_name': 'portName',
        'gateway': 'gateway',
        'vhost': 'vhost'
    }

    def __init__(self, name=None, port_number=None, port_name=None, gateway=None, vhost=None):  # noqa: E501
        """IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._port_number = None
        self._port_name = None
        self._gateway = None
        self._vhost = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if port_number is not None:
            self.port_number = port_number
        if port_name is not None:
            self.port_name = port_name
        if gateway is not None:
            self.gateway = gateway
        if vhost is not None:
            self.vhost = vhost

    @property
    def name(self):
        """Gets the name of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501

        Route configuration name to match on. Can be used to match a specific route configuration by name, such as the internally generated \"http_proxy\" route configuration for all sidecars.  # noqa: E501

        :return: The name of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.

        Route configuration name to match on. Can be used to match a specific route configuration by name, such as the internally generated \"http_proxy\" route configuration for all sidecars.  # noqa: E501

        :param name: The name of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port_number(self):
        """Gets the port_number of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501

        The service port number or gateway server port number for which this route configuration was generated. If omitted, applies to route configurations for all ports.  # noqa: E501

        :return: The port_number of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.

        The service port number or gateway server port number for which this route configuration was generated. If omitted, applies to route configurations for all ports.  # noqa: E501

        :param port_number: The port_number of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :type: int
        """

        self._port_number = port_number

    @property
    def port_name(self):
        """Gets the port_name of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501

        Applicable only for GATEWAY context. The gateway server port name for which this route configuration was generated.  # noqa: E501

        :return: The port_name of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        """Sets the port_name of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.

        Applicable only for GATEWAY context. The gateway server port name for which this route configuration was generated.  # noqa: E501

        :param port_name: The port_name of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :type: str
        """

        self._port_name = port_name

    @property
    def gateway(self):
        """Gets the gateway of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501

        The Istio gateway config's namespace/name for which this route configuration was generated. Applies only if the context is GATEWAY. Should be in the namespace/name format. Use this field in conjunction with the portNumber and portName to accurately select the Envoy route configuration for a specific HTTPS server within a gateway config object.  # noqa: E501

        :return: The gateway of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.

        The Istio gateway config's namespace/name for which this route configuration was generated. Applies only if the context is GATEWAY. Should be in the namespace/name format. Use this field in conjunction with the portNumber and portName to accurately select the Envoy route configuration for a specific HTTPS server within a gateway config object.  # noqa: E501

        :param gateway: The gateway of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def vhost(self):
        """Gets the vhost of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501


        :return: The vhost of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatchVirtualHostMatch
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        """Sets the vhost of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.


        :param vhost: The vhost of this IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch.  # noqa: E501
        :type: IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatchVirtualHostMatch
        """

        self._vhost = vhost

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
        if not isinstance(other, IstioNetworkingV1alpha3EnvoyFilterRouteConfigurationMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
