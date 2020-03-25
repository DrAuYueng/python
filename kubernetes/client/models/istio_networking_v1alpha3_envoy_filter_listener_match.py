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


class IstioNetworkingV1alpha3EnvoyFilterListenerMatch(object):
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
        'filter_chain': 'IstioNetworkingV1alpha3EnvoyFilterListenerMatchFilterChainMatch'
    }

    attribute_map = {
        'name': 'name',
        'port_number': 'portNumber',
        'port_name': 'portName',
        'filter_chain': 'filterChain'
    }

    def __init__(self, name=None, port_number=None, port_name=None, filter_chain=None):  # noqa: E501
        """IstioNetworkingV1alpha3EnvoyFilterListenerMatch - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._port_number = None
        self._port_name = None
        self._filter_chain = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if port_number is not None:
            self.port_number = port_number
        if port_name is not None:
            self.port_name = port_name
        if filter_chain is not None:
            self.filter_chain = filter_chain

    @property
    def name(self):
        """Gets the name of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501

        Match a specific listener by its name. The listeners generated by Pilot are typically named as IP:Port.  # noqa: E501

        :return: The name of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.

        Match a specific listener by its name. The listeners generated by Pilot are typically named as IP:Port.  # noqa: E501

        :param name: The name of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port_number(self):
        """Gets the port_number of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501

        The service port/gateway port to which traffic is being sent/received. If not specified, matches all listeners. Even though inbound listeners are generated for the instance/pod ports, only service ports should be used to match listeners.  # noqa: E501

        :return: The port_number of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.

        The service port/gateway port to which traffic is being sent/received. If not specified, matches all listeners. Even though inbound listeners are generated for the instance/pod ports, only service ports should be used to match listeners.  # noqa: E501

        :param port_number: The port_number of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501
        :type: int
        """

        self._port_number = port_number

    @property
    def port_name(self):
        """Gets the port_name of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501

        Instead of using specific port numbers, a set of ports matching a given service's port name can be selected. Matching is case insensitive. Not implemented. $hide_from_docs  # noqa: E501

        :return: The port_name of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501
        :rtype: str
        """
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        """Sets the port_name of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.

        Instead of using specific port numbers, a set of ports matching a given service's port name can be selected. Matching is case insensitive. Not implemented. $hide_from_docs  # noqa: E501

        :param port_name: The port_name of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501
        :type: str
        """

        self._port_name = port_name

    @property
    def filter_chain(self):
        """Gets the filter_chain of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501


        :return: The filter_chain of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3EnvoyFilterListenerMatchFilterChainMatch
        """
        return self._filter_chain

    @filter_chain.setter
    def filter_chain(self, filter_chain):
        """Sets the filter_chain of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.


        :param filter_chain: The filter_chain of this IstioNetworkingV1alpha3EnvoyFilterListenerMatch.  # noqa: E501
        :type: IstioNetworkingV1alpha3EnvoyFilterListenerMatchFilterChainMatch
        """

        self._filter_chain = filter_chain

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
        if not isinstance(other, IstioNetworkingV1alpha3EnvoyFilterListenerMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other