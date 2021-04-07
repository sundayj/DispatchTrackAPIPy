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

class Customer(object):
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
        'customer_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'phone1': 'str',
        'phone2': 'str',
        'phone3': 'str',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'latitude': 'str',
        'longitude': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'phone1': 'phone1',
        'phone2': 'phone2',
        'phone3': 'phone3',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone1=None, phone2=None, phone3=None, address1=None, address2=None, city=None, state=None, zip=None, latitude=None, longitude=None):  # noqa: E501
        """Customer - a model defined in Swagger"""  # noqa: E501
        self._customer_id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._phone1 = None
        self._phone2 = None
        self._phone3 = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state = None
        self._zip = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None
        if customer_id is not None:
            self.customer_id = customer_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if phone1 is not None:
            self.phone1 = phone1
        if phone2 is not None:
            self.phone2 = phone2
        if phone3 is not None:
            self.phone3 = phone3
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def customer_id(self):
        """Gets the customer_id of this Customer.  # noqa: E501


        :return: The customer_id of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Customer.


        :param customer_id: The customer_id of this Customer.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def first_name(self):
        """Gets the first_name of this Customer.  # noqa: E501


        :return: The first_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Customer.


        :param first_name: The first_name of this Customer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Customer.  # noqa: E501


        :return: The last_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Customer.


        :param last_name: The last_name of this Customer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this Customer.  # noqa: E501


        :return: The email of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.


        :param email: The email of this Customer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone1(self):
        """Gets the phone1 of this Customer.  # noqa: E501


        :return: The phone1 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone1

    @phone1.setter
    def phone1(self, phone1):
        """Sets the phone1 of this Customer.


        :param phone1: The phone1 of this Customer.  # noqa: E501
        :type: str
        """

        self._phone1 = phone1

    @property
    def phone2(self):
        """Gets the phone2 of this Customer.  # noqa: E501


        :return: The phone2 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """Sets the phone2 of this Customer.


        :param phone2: The phone2 of this Customer.  # noqa: E501
        :type: str
        """

        self._phone2 = phone2

    @property
    def phone3(self):
        """Gets the phone3 of this Customer.  # noqa: E501


        :return: The phone3 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """Sets the phone3 of this Customer.


        :param phone3: The phone3 of this Customer.  # noqa: E501
        :type: str
        """

        self._phone3 = phone3

    @property
    def address1(self):
        """Gets the address1 of this Customer.  # noqa: E501


        :return: The address1 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this Customer.


        :param address1: The address1 of this Customer.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this Customer.  # noqa: E501


        :return: The address2 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Customer.


        :param address2: The address2 of this Customer.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Customer.  # noqa: E501


        :return: The city of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Customer.


        :param city: The city of this Customer.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Customer.  # noqa: E501


        :return: The state of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Customer.


        :param state: The state of this Customer.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this Customer.  # noqa: E501


        :return: The zip of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Customer.


        :param zip: The zip of this Customer.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def latitude(self):
        """Gets the latitude of this Customer.  # noqa: E501


        :return: The latitude of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Customer.


        :param latitude: The latitude of this Customer.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Customer.  # noqa: E501


        :return: The longitude of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Customer.


        :param longitude: The longitude of this Customer.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

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
        if issubclass(Customer, dict):
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
        if not isinstance(other, Customer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
