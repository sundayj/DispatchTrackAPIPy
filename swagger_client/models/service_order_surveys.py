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

class ServiceOrderSurveys(object):
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
        'questions': 'list[Question]',
        'comments': 'list[SurveyComment]'
    }

    attribute_map = {
        'questions': 'questions',
        'comments': 'comments'
    }

    def __init__(self, questions=None, comments=None):  # noqa: E501
        """ServiceOrderSurveys - a model defined in Swagger"""  # noqa: E501
        self._questions = None
        self._comments = None
        self.discriminator = None
        if questions is not None:
            self.questions = questions
        if comments is not None:
            self.comments = comments

    @property
    def questions(self):
        """Gets the questions of this ServiceOrderSurveys.  # noqa: E501


        :return: The questions of this ServiceOrderSurveys.  # noqa: E501
        :rtype: list[Question]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """Sets the questions of this ServiceOrderSurveys.


        :param questions: The questions of this ServiceOrderSurveys.  # noqa: E501
        :type: list[Question]
        """

        self._questions = questions

    @property
    def comments(self):
        """Gets the comments of this ServiceOrderSurveys.  # noqa: E501


        :return: The comments of this ServiceOrderSurveys.  # noqa: E501
        :rtype: list[SurveyComment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ServiceOrderSurveys.


        :param comments: The comments of this ServiceOrderSurveys.  # noqa: E501
        :type: list[SurveyComment]
        """

        self._comments = comments

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
        if issubclass(ServiceOrderSurveys, dict):
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
        if not isinstance(other, ServiceOrderSurveys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other