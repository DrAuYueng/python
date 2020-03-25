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


class IstioNetworkingV1alpha3TLSRoute(object):
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
        'route': 'list[IstioNetworkingV1alpha3RouteDestination]',
        'match': 'list[IstioNetworkingV1alpha3TLSMatchAttributes]'
    }

    attribute_map = {
        'route': 'route',
        'match': 'match'
    }

    def __init__(self, route=None, match=None):  # noqa: E501
        """IstioNetworkingV1alpha3TLSRoute - a model defined in OpenAPI"""  # noqa: E501

        self._route = None
        self._match = None
        self.discriminator = None

        if route is not None:
            self.route = route
        if match is not None:
            self.match = match

    @property
    def route(self):
        """Gets the route of this IstioNetworkingV1alpha3TLSRoute.  # noqa: E501

        The destination to which the connection should be forwarded to.  # noqa: E501

        :return: The route of this IstioNetworkingV1alpha3TLSRoute.  # noqa: E501
        :rtype: list[IstioNetworkingV1alpha3RouteDestination]
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this IstioNetworkingV1alpha3TLSRoute.

        The destination to which the connection should be forwarded to.  # noqa: E501

        :param route: The route of this IstioNetworkingV1alpha3TLSRoute.  # noqa: E501
        :type: list[IstioNetworkingV1alpha3RouteDestination]
        """

        self._route = route

    @property
    def match(self):
        """Gets the match of this IstioNetworkingV1alpha3TLSRoute.  # noqa: E501

        Match conditions to be satisfied for the rule to be activated. All conditions inside a single match block have AND semantics, while the list of match blocks have OR semantics. The rule is matched if any one of the match blocks succeed.  # noqa: E501

        :return: The match of this IstioNetworkingV1alpha3TLSRoute.  # noqa: E501
        :rtype: list[IstioNetworkingV1alpha3TLSMatchAttributes]
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this IstioNetworkingV1alpha3TLSRoute.

        Match conditions to be satisfied for the rule to be activated. All conditions inside a single match block have AND semantics, while the list of match blocks have OR semantics. The rule is matched if any one of the match blocks succeed.  # noqa: E501

        :param match: The match of this IstioNetworkingV1alpha3TLSRoute.  # noqa: E501
        :type: list[IstioNetworkingV1alpha3TLSMatchAttributes]
        """

        self._match = match

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
        if not isinstance(other, IstioNetworkingV1alpha3TLSRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
