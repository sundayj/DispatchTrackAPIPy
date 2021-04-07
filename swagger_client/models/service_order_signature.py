# coding: utf-8

"""
    DispatchTrack API

    # Authentication The authentication for this API is done via Oauth2 Access Token: - **GetTokenAuth**   You can find the client ID and secret in your application's Admin - Oauth2 Settings tab.   These are then passed via Basic Auth in the request to server's /oauth2/token endpoint to get the access token.   - **Auth**   With the Oauth2 Access Token received from /oauth2/token request, API requests for remaining API endpoints can be made.   It has to be sent as an Authorization Bearer header in the request.   If an invalid or expired access token is used, API will send back a 401 status.     # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ServiceOrderSignature(object):
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
        'created_at': 'str',
        'callback_code': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'callback_code': 'callback_code'
    }

    def __init__(self, created_at=None, callback_code=None):  # noqa: E501
        """ServiceOrderSignature - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._callback_code = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if callback_code is not None:
            self.callback_code = callback_code

    @property
    def created_at(self):
        """Gets the created_at of this ServiceOrderSignature.  # noqa: E501


        :return: The created_at of this ServiceOrderSignature.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ServiceOrderSignature.


        :param created_at: The created_at of this ServiceOrderSignature.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def callback_code(self):
        """Gets the callback_code of this ServiceOrderSignature.  # noqa: E501


        :return: The callback_code of this ServiceOrderSignature.  # noqa: E501
        :rtype: str
        """
        return self._callback_code

    @callback_code.setter
    def callback_code(self, callback_code):
        """Sets the callback_code of this ServiceOrderSignature.


        :param callback_code: The callback_code of this ServiceOrderSignature.  # noqa: E501
        :type: str
        """

        self._callback_code = callback_code

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
        if issubclass(ServiceOrderSignature, dict):
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
        if not isinstance(other, ServiceOrderSignature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other