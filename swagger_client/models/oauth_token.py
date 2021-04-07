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

class OauthToken(object):
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
        'access_token': 'str',
        'access_token_expires_at': 'str',
        'scope': 'bool'
    }

    attribute_map = {
        'access_token': 'access_token',
        'access_token_expires_at': 'access_token_expires_at',
        'scope': 'scope'
    }

    def __init__(self, access_token=None, access_token_expires_at=None, scope=False):  # noqa: E501
        """OauthToken - a model defined in Swagger"""  # noqa: E501
        self._access_token = None
        self._access_token_expires_at = None
        self._scope = None
        self.discriminator = None
        if access_token is not None:
            self.access_token = access_token
        if access_token_expires_at is not None:
            self.access_token_expires_at = access_token_expires_at
        if scope is not None:
            self.scope = scope

    @property
    def access_token(self):
        """Gets the access_token of this OauthToken.  # noqa: E501


        :return: The access_token of this OauthToken.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this OauthToken.


        :param access_token: The access_token of this OauthToken.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def access_token_expires_at(self):
        """Gets the access_token_expires_at of this OauthToken.  # noqa: E501


        :return: The access_token_expires_at of this OauthToken.  # noqa: E501
        :rtype: str
        """
        return self._access_token_expires_at

    @access_token_expires_at.setter
    def access_token_expires_at(self, access_token_expires_at):
        """Sets the access_token_expires_at of this OauthToken.


        :param access_token_expires_at: The access_token_expires_at of this OauthToken.  # noqa: E501
        :type: str
        """

        self._access_token_expires_at = access_token_expires_at

    @property
    def scope(self):
        """Gets the scope of this OauthToken.  # noqa: E501


        :return: The scope of this OauthToken.  # noqa: E501
        :rtype: bool
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this OauthToken.


        :param scope: The scope of this OauthToken.  # noqa: E501
        :type: bool
        """

        self._scope = scope

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
        if issubclass(OauthToken, dict):
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
        if not isinstance(other, OauthToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other