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


class IstioNetworkingV1alpha3GatewaySpec(object):
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
        'servers': 'list[IstioNetworkingV1alpha3Server]',
        'selector': 'dict(str, str)'
    }

    attribute_map = {
        'servers': 'servers',
        'selector': 'selector'
    }

    def __init__(self, servers=None, selector=None):  # noqa: E501
        """IstioNetworkingV1alpha3GatewaySpec - a model defined in OpenAPI"""  # noqa: E501

        self._servers = None
        self._selector = None
        self.discriminator = None

        self.servers = servers
        self.selector = selector

    @property
    def servers(self):
        """Gets the servers of this IstioNetworkingV1alpha3GatewaySpec.  # noqa: E501

        A list of server specifications.  # noqa: E501

        :return: The servers of this IstioNetworkingV1alpha3GatewaySpec.  # noqa: E501
        :rtype: list[IstioNetworkingV1alpha3Server]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this IstioNetworkingV1alpha3GatewaySpec.

        A list of server specifications.  # noqa: E501

        :param servers: The servers of this IstioNetworkingV1alpha3GatewaySpec.  # noqa: E501
        :type: list[IstioNetworkingV1alpha3Server]
        """
        if servers is None:
            raise ValueError("Invalid value for `servers`, must not be `None`")  # noqa: E501

        self._servers = servers

    @property
    def selector(self):
        """Gets the selector of this IstioNetworkingV1alpha3GatewaySpec.  # noqa: E501

        One or more labels that indicate a specific set of pods/VMs on which this gateway configuration should be applied. The scope of label search is restricted to the configuration namespace in which the the resource is present. In other words, the Gateway resource must reside in the same namespace as the gateway workload instance.  # noqa: E501

        :return: The selector of this IstioNetworkingV1alpha3GatewaySpec.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this IstioNetworkingV1alpha3GatewaySpec.

        One or more labels that indicate a specific set of pods/VMs on which this gateway configuration should be applied. The scope of label search is restricted to the configuration namespace in which the the resource is present. In other words, the Gateway resource must reside in the same namespace as the gateway workload instance.  # noqa: E501

        :param selector: The selector of this IstioNetworkingV1alpha3GatewaySpec.  # noqa: E501
        :type: dict(str, str)
        """
        if selector is None:
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

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
        if not isinstance(other, IstioNetworkingV1alpha3GatewaySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other