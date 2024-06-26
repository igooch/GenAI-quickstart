# coding: utf-8

"""
    sdk.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class GameServerObjectMeta(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'name': 'str',
        'namespace': 'str',
        'uid': 'str',
        'resource_version': 'str',
        'generation': 'str',
        'creation_timestamp': 'str',
        'deletion_timestamp': 'str',
        'annotations': 'dict(str, str)',
        'labels': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'uid': 'uid',
        'resource_version': 'resource_version',
        'generation': 'generation',
        'creation_timestamp': 'creation_timestamp',
        'deletion_timestamp': 'deletion_timestamp',
        'annotations': 'annotations',
        'labels': 'labels'
    }

    def __init__(self, name=None, namespace=None, uid=None, resource_version=None, generation=None, creation_timestamp=None, deletion_timestamp=None, annotations=None, labels=None, _configuration=None):  # noqa: E501
        """GameServerObjectMeta - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._namespace = None
        self._uid = None
        self._resource_version = None
        self._generation = None
        self._creation_timestamp = None
        self._deletion_timestamp = None
        self._annotations = None
        self._labels = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if uid is not None:
            self.uid = uid
        if resource_version is not None:
            self.resource_version = resource_version
        if generation is not None:
            self.generation = generation
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if deletion_timestamp is not None:
            self.deletion_timestamp = deletion_timestamp
        if annotations is not None:
            self.annotations = annotations
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        """Gets the name of this GameServerObjectMeta.  # noqa: E501


        :return: The name of this GameServerObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GameServerObjectMeta.


        :param name: The name of this GameServerObjectMeta.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this GameServerObjectMeta.  # noqa: E501


        :return: The namespace of this GameServerObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this GameServerObjectMeta.


        :param namespace: The namespace of this GameServerObjectMeta.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def uid(self):
        """Gets the uid of this GameServerObjectMeta.  # noqa: E501


        :return: The uid of this GameServerObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this GameServerObjectMeta.


        :param uid: The uid of this GameServerObjectMeta.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def resource_version(self):
        """Gets the resource_version of this GameServerObjectMeta.  # noqa: E501


        :return: The resource_version of this GameServerObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this GameServerObjectMeta.


        :param resource_version: The resource_version of this GameServerObjectMeta.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

    @property
    def generation(self):
        """Gets the generation of this GameServerObjectMeta.  # noqa: E501


        :return: The generation of this GameServerObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this GameServerObjectMeta.


        :param generation: The generation of this GameServerObjectMeta.  # noqa: E501
        :type: str
        """

        self._generation = generation

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this GameServerObjectMeta.  # noqa: E501


        :return: The creation_timestamp of this GameServerObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this GameServerObjectMeta.


        :param creation_timestamp: The creation_timestamp of this GameServerObjectMeta.  # noqa: E501
        :type: str
        """

        self._creation_timestamp = creation_timestamp

    @property
    def deletion_timestamp(self):
        """Gets the deletion_timestamp of this GameServerObjectMeta.  # noqa: E501


        :return: The deletion_timestamp of this GameServerObjectMeta.  # noqa: E501
        :rtype: str
        """
        return self._deletion_timestamp

    @deletion_timestamp.setter
    def deletion_timestamp(self, deletion_timestamp):
        """Sets the deletion_timestamp of this GameServerObjectMeta.


        :param deletion_timestamp: The deletion_timestamp of this GameServerObjectMeta.  # noqa: E501
        :type: str
        """

        self._deletion_timestamp = deletion_timestamp

    @property
    def annotations(self):
        """Gets the annotations of this GameServerObjectMeta.  # noqa: E501


        :return: The annotations of this GameServerObjectMeta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this GameServerObjectMeta.


        :param annotations: The annotations of this GameServerObjectMeta.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def labels(self):
        """Gets the labels of this GameServerObjectMeta.  # noqa: E501


        :return: The labels of this GameServerObjectMeta.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this GameServerObjectMeta.


        :param labels: The labels of this GameServerObjectMeta.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(GameServerObjectMeta, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GameServerObjectMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GameServerObjectMeta):
            return True

        return self.to_dict() != other.to_dict()
