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


class IstioNetworkingV1alpha3EnvoyFilterClusterMatch(object):
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
        'service': 'str',
        'subset': 'str'
    }

    attribute_map = {
        'name': 'name',
        'port_number': 'portNumber',
        'service': 'service',
        'subset': 'subset'
    }

    def __init__(self, name=None, port_number=None, service=None, subset=None):  # noqa: E501
        """IstioNetworkingV1alpha3EnvoyFilterClusterMatch - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._port_number = None
        self._service = None
        self._subset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if port_number is not None:
            self.port_number = port_number
        if service is not None:
            self.service = service
        if subset is not None:
            self.subset = subset

    @property
    def name(self):
        """Gets the name of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501

        The exact name of the cluster to match. To match a specific cluster by name, such as the internally generated \"Passthrough\" cluster, leave all fields in clusterMatch empty, except the name.  # noqa: E501

        :return: The name of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.

        The exact name of the cluster to match. To match a specific cluster by name, such as the internally generated \"Passthrough\" cluster, leave all fields in clusterMatch empty, except the name.  # noqa: E501

        :param name: The name of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port_number(self):
        """Gets the port_number of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501

        The service port for which this cluster was generated. If omitted, applies to clusters for any port.  # noqa: E501

        :return: The port_number of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.

        The service port for which this cluster was generated. If omitted, applies to clusters for any port.  # noqa: E501

        :param port_number: The port_number of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501
        :type: int
        """

        self._port_number = port_number

    @property
    def service(self):
        """Gets the service of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501

        The fully qualified service name for this cluster. If omitted, applies to clusters for any service. For services defined through service entries, the service name is same as the hosts defined in the service entry.  # noqa: E501

        :return: The service of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.

        The fully qualified service name for this cluster. If omitted, applies to clusters for any service. For services defined through service entries, the service name is same as the hosts defined in the service entry.  # noqa: E501

        :param service: The service of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def subset(self):
        """Gets the subset of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501

        The subset associated with the service. If omitted, applies to clusters for any subset of a service.  # noqa: E501

        :return: The subset of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501
        :rtype: str
        """
        return self._subset

    @subset.setter
    def subset(self, subset):
        """Sets the subset of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.

        The subset associated with the service. If omitted, applies to clusters for any subset of a service.  # noqa: E501

        :param subset: The subset of this IstioNetworkingV1alpha3EnvoyFilterClusterMatch.  # noqa: E501
        :type: str
        """

        self._subset = subset

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
        if not isinstance(other, IstioNetworkingV1alpha3EnvoyFilterClusterMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
