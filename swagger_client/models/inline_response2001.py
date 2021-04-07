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

class InlineResponse2001(object):
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
        'success': 'bool',
        'status': 'float',
        'note': 'str',
        'service_orders': 'list[ManifestOrder]'
    }

    attribute_map = {
        'success': 'success',
        'status': 'status',
        'note': 'note',
        'service_orders': 'service_orders'
    }

    def __init__(self, success=None, status=None, note=None, service_orders=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._success = None
        self._status = None
        self._note = None
        self._service_orders = None
        self.discriminator = None
        if success is not None:
            self.success = success
        if status is not None:
            self.status = status
        if note is not None:
            self.note = note
        if service_orders is not None:
            self.service_orders = service_orders

    @property
    def success(self):
        """Gets the success of this InlineResponse2001.  # noqa: E501


        :return: The success of this InlineResponse2001.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse2001.


        :param success: The success of this InlineResponse2001.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def status(self):
        """Gets the status of this InlineResponse2001.  # noqa: E501


        :return: The status of this InlineResponse2001.  # noqa: E501
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2001.


        :param status: The status of this InlineResponse2001.  # noqa: E501
        :type: float
        """

        self._status = status

    @property
    def note(self):
        """Gets the note of this InlineResponse2001.  # noqa: E501


        :return: The note of this InlineResponse2001.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this InlineResponse2001.


        :param note: The note of this InlineResponse2001.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def service_orders(self):
        """Gets the service_orders of this InlineResponse2001.  # noqa: E501


        :return: The service_orders of this InlineResponse2001.  # noqa: E501
        :rtype: list[ManifestOrder]
        """
        return self._service_orders

    @service_orders.setter
    def service_orders(self, service_orders):
        """Sets the service_orders of this InlineResponse2001.


        :param service_orders: The service_orders of this InlineResponse2001.  # noqa: E501
        :type: list[ManifestOrder]
        """

        self._service_orders = service_orders

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other