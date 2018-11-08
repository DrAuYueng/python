# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1Webhook(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_config': 'V1beta1WebhookClientConfig',
        'failure_policy': 'str',
        'name': 'str',
        'namespace_selector': 'V1LabelSelector',
        'rules': 'list[V1beta1RuleWithOperations]'
    }

    attribute_map = {
        'client_config': 'clientConfig',
        'failure_policy': 'failurePolicy',
        'name': 'name',
        'namespace_selector': 'namespaceSelector',
        'rules': 'rules'
    }

    def __init__(self, client_config=None, failure_policy=None, name=None, namespace_selector=None, rules=None):
        """
        V1beta1Webhook - a model defined in Swagger
        """

        self._client_config = None
        self._failure_policy = None
        self._name = None
        self._namespace_selector = None
        self._rules = None
        self.discriminator = None

        self.client_config = client_config
        if failure_policy is not None:
          self.failure_policy = failure_policy
        self.name = name
        if namespace_selector is not None:
          self.namespace_selector = namespace_selector
        if rules is not None:
          self.rules = rules

    @property
    def client_config(self):
        """
        Gets the client_config of this V1beta1Webhook.
        ClientConfig defines how to communicate with the hook. Required

        :return: The client_config of this V1beta1Webhook.
        :rtype: V1beta1WebhookClientConfig
        """
        return self._client_config

    @client_config.setter
    def client_config(self, client_config):
        """
        Sets the client_config of this V1beta1Webhook.
        ClientConfig defines how to communicate with the hook. Required

        :param client_config: The client_config of this V1beta1Webhook.
        :type: V1beta1WebhookClientConfig
        """
        if client_config is None:
            raise ValueError("Invalid value for `client_config`, must not be `None`")

        self._client_config = client_config

    @property
    def failure_policy(self):
        """
        Gets the failure_policy of this V1beta1Webhook.
        FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Ignore.

        :return: The failure_policy of this V1beta1Webhook.
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """
        Sets the failure_policy of this V1beta1Webhook.
        FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Ignore.

        :param failure_policy: The failure_policy of this V1beta1Webhook.
        :type: str
        """

        self._failure_policy = failure_policy

    @property
    def name(self):
        """
        Gets the name of this V1beta1Webhook.
        The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.

        :return: The name of this V1beta1Webhook.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1beta1Webhook.
        The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.

        :param name: The name of this V1beta1Webhook.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def namespace_selector(self):
        """
        Gets the namespace_selector of this V1beta1Webhook.
        NamespaceSelector decides whether to run the webhook on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the webhook.  For example, to run the webhook on any objects whose namespace is not associated with \"runlevel\" of \"0\" or \"1\";  you will set the selector as follows: \"namespaceSelector\": {   \"matchExpressions\": [     {       \"key\": \"runlevel\",       \"operator\": \"NotIn\",       \"values\": [         \"0\",         \"1\"       ]     }   ] }  If instead you want to only run the webhook on any objects whose namespace is associated with the \"environment\" of \"prod\" or \"staging\"; you will set the selector as follows: \"namespaceSelector\": {   \"matchExpressions\": [     {       \"key\": \"environment\",       \"operator\": \"In\",       \"values\": [         \"prod\",         \"staging\"       ]     }   ] }  See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ for more examples of label selectors.  Default to the empty LabelSelector, which matches everything.

        :return: The namespace_selector of this V1beta1Webhook.
        :rtype: V1LabelSelector
        """
        return self._namespace_selector

    @namespace_selector.setter
    def namespace_selector(self, namespace_selector):
        """
        Sets the namespace_selector of this V1beta1Webhook.
        NamespaceSelector decides whether to run the webhook on an object based on whether the namespace for that object matches the selector. If the object itself is a namespace, the matching is performed on object.metadata.labels. If the object is another cluster scoped resource, it never skips the webhook.  For example, to run the webhook on any objects whose namespace is not associated with \"runlevel\" of \"0\" or \"1\";  you will set the selector as follows: \"namespaceSelector\": {   \"matchExpressions\": [     {       \"key\": \"runlevel\",       \"operator\": \"NotIn\",       \"values\": [         \"0\",         \"1\"       ]     }   ] }  If instead you want to only run the webhook on any objects whose namespace is associated with the \"environment\" of \"prod\" or \"staging\"; you will set the selector as follows: \"namespaceSelector\": {   \"matchExpressions\": [     {       \"key\": \"environment\",       \"operator\": \"In\",       \"values\": [         \"prod\",         \"staging\"       ]     }   ] }  See https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ for more examples of label selectors.  Default to the empty LabelSelector, which matches everything.

        :param namespace_selector: The namespace_selector of this V1beta1Webhook.
        :type: V1LabelSelector
        """

        self._namespace_selector = namespace_selector

    @property
    def rules(self):
        """
        Gets the rules of this V1beta1Webhook.
        Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.

        :return: The rules of this V1beta1Webhook.
        :rtype: list[V1beta1RuleWithOperations]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this V1beta1Webhook.
        Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.

        :param rules: The rules of this V1beta1Webhook.
        :type: list[V1beta1RuleWithOperations]
        """

        self._rules = rules

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1Webhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
