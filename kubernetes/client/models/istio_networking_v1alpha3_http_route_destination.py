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


class IstioNetworkingV1alpha3HTTPRouteDestination(object):
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
        'weight': 'int',
        'remove_response_headers': 'list[str]',
        'append_response_headers': 'dict(str, str)',
        'remove_request_headers': 'list[str]',
        'append_request_headers': 'dict(str, str)',
        'headers': 'IstioNetworkingV1alpha3Headers',
        'destination': 'IstioNetworkingV1alpha3Destination'
    }

    attribute_map = {
        'weight': 'weight',
        'remove_response_headers': 'removeResponseHeaders',
        'append_response_headers': 'appendResponseHeaders',
        'remove_request_headers': 'removeRequestHeaders',
        'append_request_headers': 'appendRequestHeaders',
        'headers': 'headers',
        'destination': 'destination'
    }

    def __init__(self, weight=None, remove_response_headers=None, append_response_headers=None, remove_request_headers=None, append_request_headers=None, headers=None, destination=None):  # noqa: E501
        """IstioNetworkingV1alpha3HTTPRouteDestination - a model defined in OpenAPI"""  # noqa: E501

        self._weight = None
        self._remove_response_headers = None
        self._append_response_headers = None
        self._remove_request_headers = None
        self._append_request_headers = None
        self._headers = None
        self._destination = None
        self.discriminator = None

        if weight is not None:
            self.weight = weight
        if remove_response_headers is not None:
            self.remove_response_headers = remove_response_headers
        if append_response_headers is not None:
            self.append_response_headers = append_response_headers
        if remove_request_headers is not None:
            self.remove_request_headers = remove_request_headers
        if append_request_headers is not None:
            self.append_request_headers = append_request_headers
        if headers is not None:
            self.headers = headers
        if destination is not None:
            self.destination = destination

    @property
    def weight(self):
        """Gets the weight of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501

        The proportion of traffic to be forwarded to the service version. (0-100). Sum of weights across destinations SHOULD BE == 100. If there is only one destination in a rule, the weight value is assumed to be 100.  # noqa: E501

        :return: The weight of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this IstioNetworkingV1alpha3HTTPRouteDestination.

        The proportion of traffic to be forwarded to the service version. (0-100). Sum of weights across destinations SHOULD BE == 100. If there is only one destination in a rule, the weight value is assumed to be 100.  # noqa: E501

        :param weight: The weight of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def remove_response_headers(self):
        """Gets the remove_response_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501

        Use of `remove_response_header` is deprecated. Use the `headers` field instead.  # noqa: E501

        :return: The remove_response_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_response_headers

    @remove_response_headers.setter
    def remove_response_headers(self, remove_response_headers):
        """Sets the remove_response_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.

        Use of `remove_response_header` is deprecated. Use the `headers` field instead.  # noqa: E501

        :param remove_response_headers: The remove_response_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :type: list[str]
        """

        self._remove_response_headers = remove_response_headers

    @property
    def append_response_headers(self):
        """Gets the append_response_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501

        Use of `append_response_headers` is deprecated. Use the `headers` field instead.  # noqa: E501

        :return: The append_response_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._append_response_headers

    @append_response_headers.setter
    def append_response_headers(self, append_response_headers):
        """Sets the append_response_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.

        Use of `append_response_headers` is deprecated. Use the `headers` field instead.  # noqa: E501

        :param append_response_headers: The append_response_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :type: dict(str, str)
        """

        self._append_response_headers = append_response_headers

    @property
    def remove_request_headers(self):
        """Gets the remove_request_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501

        Use of `remove_request_headers` is deprecated. Use the `headers` field instead.  # noqa: E501

        :return: The remove_request_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_request_headers

    @remove_request_headers.setter
    def remove_request_headers(self, remove_request_headers):
        """Sets the remove_request_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.

        Use of `remove_request_headers` is deprecated. Use the `headers` field instead.  # noqa: E501

        :param remove_request_headers: The remove_request_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :type: list[str]
        """

        self._remove_request_headers = remove_request_headers

    @property
    def append_request_headers(self):
        """Gets the append_request_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501

        Use of `append_request_headers` is deprecated. Use the `headers` field instead.  # noqa: E501

        :return: The append_request_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._append_request_headers

    @append_request_headers.setter
    def append_request_headers(self, append_request_headers):
        """Sets the append_request_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.

        Use of `append_request_headers` is deprecated. Use the `headers` field instead.  # noqa: E501

        :param append_request_headers: The append_request_headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :type: dict(str, str)
        """

        self._append_request_headers = append_request_headers

    @property
    def headers(self):
        """Gets the headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501


        :return: The headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3Headers
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this IstioNetworkingV1alpha3HTTPRouteDestination.


        :param headers: The headers of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :type: IstioNetworkingV1alpha3Headers
        """

        self._headers = headers

    @property
    def destination(self):
        """Gets the destination of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501


        :return: The destination of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :rtype: IstioNetworkingV1alpha3Destination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this IstioNetworkingV1alpha3HTTPRouteDestination.


        :param destination: The destination of this IstioNetworkingV1alpha3HTTPRouteDestination.  # noqa: E501
        :type: IstioNetworkingV1alpha3Destination
        """

        self._destination = destination

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
        if not isinstance(other, IstioNetworkingV1alpha3HTTPRouteDestination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other