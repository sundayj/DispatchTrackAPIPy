# coding: utf-8

"""
    DispatchTrack API

    # Authentication The authentication for this API is done via Oauth2 Access Token: - **GetTokenAuth**   You can find the client ID and secret in your application's Admin - Oauth2 Settings tab.   These are then passed via Basic Auth in the request to server's /oauth2/token endpoint to get the access token.   - **Auth**   With the Oauth2 Access Token received from /oauth2/token request, API requests for remaining API endpoints can be made.   It has to be sent as an Authorization Bearer header in the request.   If an invalid or expired access token is used, API will send back a 401 status.     # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="DispatchTrack API",
    author_email="",
    url="",
    keywords=["Swagger", "DispatchTrack API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    # Authentication The authentication for this API is done via Oauth2 Access Token: - **GetTokenAuth**   You can find the client ID and secret in your application&#x27;s Admin - Oauth2 Settings tab.   These are then passed via Basic Auth in the request to server&#x27;s /oauth2/token endpoint to get the access token.   - **Auth**   With the Oauth2 Access Token received from /oauth2/token request, API requests for remaining API endpoints can be made.   It has to be sent as an Authorization Bearer header in the request.   If an invalid or expired access token is used, API will send back a 401 status.     # noqa: E501
    """
)
