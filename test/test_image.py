# coding: utf-8

"""
    DispatchTrack API

    # Authentication The authentication for this API is done via Oauth2 Access Token: - **GetTokenAuth**   You can find the client ID and secret in your application's Admin - Oauth2 Settings tab.   These are then passed via Basic Auth in the request to server's /oauth2/token endpoint to get the access token.   - **Auth**   With the Oauth2 Access Token received from /oauth2/token request, API requests for remaining API endpoints can be made.   It has to be sent as an Authorization Bearer header in the request.   If an invalid or expired access token is used, API will send back a 401 status.     # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.image import Image  # noqa: E501
from swagger_client.rest import ApiException


class TestImage(unittest.TestCase):
    """Image unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImage(self):
        """Test Image"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.image.Image()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
