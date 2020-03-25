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


class IstioNetworkingV1alpha3WorkloadSelector(object):
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
        'labels': 'dict(str, str)'
    }

    attribute_map = {
        'labels': 'labels'
    }

    def __init__(self, labels=None):  # noqa: E501
        """IstioNetworkingV1alpha3WorkloadSelector - a model defined in OpenAPI"""  # noqa: E501

        self._labels = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels

    @property
    def labels(self):
        """Gets the labels of this IstioNetworkingV1alpha3WorkloadSelector.  # noqa: E501

        One or more labels that indicate a specific set of pods/VMs on which this `Sidecar` configuration should be applied. The scope of label search is restricted to the configuration namespace in which the the resource is present.  # noqa: E501

        :return: The labels of this IstioNetworkingV1alpha3WorkloadSelector.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IstioNetworkingV1alpha3WorkloadSelector.

        One or more labels that indicate a specific set of pods/VMs on which this `Sidecar` configuration should be applied. The scope of label search is restricted to the configuration namespace in which the the resource is present.  # noqa: E501

        :param labels: The labels of this IstioNetworkingV1alpha3WorkloadSelector.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

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
        if not isinstance(other, IstioNetworkingV1alpha3WorkloadSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other