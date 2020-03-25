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


class IstioNetworkingV1alpha3Destination(object):
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
        'host': 'str',
        'port': 'IstioNetworkingV1alpha3PortSelector',
        'subset': 'str'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'subset': 'subset'
    }

    def __init__(self, host=None, port=None, subset=None):  # noqa: E501
        """IstioNetworkingV1alpha3Destination - a model defined in OpenAPI"""  # noqa: E501

        self._host = None
        self._port = None
        self._subset = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if subset is not None:
            self.subset = subset

    @property
    def host(self):
        """Gets the host of this IstioNetworkingV1alpha3Destination.  # noqa: E501

        The name of a service from the service registry. Service names are looked up from the platform's service registry (e.g., Kubernetes services, Consul services, etc.) and from the hosts declared by [ServiceEntry](https://istio.io/docs/reference/config/networking/service-entry/#ServiceEntry). Traffic forwarded to destinations that are not found in either of the two, will be dropped.  # noqa: E501

        :return: The host of this IstioNetworkingV1alpha3Destination.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this IstioNetworkingV1alpha3Destination.

        The name of a service from the service registry. Service names are looked up from the platform's service registry (e.g., Kubernetes services, Consul services, etc.) and from the hosts declared by [ServiceEntry](https://istio.io/docs/reference/config/networking/service-entry/#ServiceEntry). Traffic forwarded to destinations that are not found in either of the two, will be dropped.  # noqa: E501

        :param host: The host of this IstioNetworkingV1alpha3Destination.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this IstioNetworkingV1alpha3Destination.  # noqa: E501


        :return: The port of this IstioNetworkingV1alpha3Destination.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3PortSelector
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this IstioNetworkingV1alpha3Destination.


        :param port: The port of this IstioNetworkingV1alpha3Destination.  # noqa: E501
        :type: IstioNetworkingV1alpha3PortSelector
        """

        self._port = port

    @property
    def subset(self):
        """Gets the subset of this IstioNetworkingV1alpha3Destination.  # noqa: E501

        The name of a subset within the service. Applicable only to services within the mesh. The subset must be defined in a corresponding DestinationRule.  # noqa: E501

        :return: The subset of this IstioNetworkingV1alpha3Destination.  # noqa: E501
        :rtype: str
        """
        return self._subset

    @subset.setter
    def subset(self, subset):
        """Sets the subset of this IstioNetworkingV1alpha3Destination.

        The name of a subset within the service. Applicable only to services within the mesh. The subset must be defined in a corresponding DestinationRule.  # noqa: E501

        :param subset: The subset of this IstioNetworkingV1alpha3Destination.  # noqa: E501
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
        if not isinstance(other, IstioNetworkingV1alpha3Destination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
