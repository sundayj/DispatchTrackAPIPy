# coding: utf-8

# flake8: noqa

"""
    DispatchTrack API

    # Authentication The authentication for this API is done via Oauth2 Access Token: - **GetTokenAuth**   You can find the client ID and secret in your application's Admin - Oauth2 Settings tab.   These are then passed via Basic Auth in the request to server's /oauth2/token endpoint to get the access token.   - **Auth**   With the Oauth2 Access Token received from /oauth2/token request, API requests for remaining API endpoints can be made.   It has to be sent as an Authorization Bearer header in the request.   If an invalid or expired access token is used, API will send back a 401 status.     # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.orders_api import OrdersApi
from swagger_client.api.route_api import RouteApi
# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.add_order_error import AddOrderError
from swagger_client.models.add_order_success import AddOrderSuccess
from swagger_client.models.add_order_success_data import AddOrderSuccessData
from swagger_client.models.add_order_success_data_failed_orders import AddOrderSuccessDataFailedOrders
from swagger_client.models.body import Body
from swagger_client.models.customer import Customer
from swagger_client.models.delete_order_error import DeleteOrderError
from swagger_client.models.delete_order_success import DeleteOrderSuccess
from swagger_client.models.export_order_error import ExportOrderError
from swagger_client.models.history import History
from swagger_client.models.image import Image
from swagger_client.models.import_order import ImportOrder
from swagger_client.models.import_order_additional_fields import ImportOrderAdditionalFields
from swagger_client.models.import_order_custom_fields import ImportOrderCustomFields
from swagger_client.models.import_order_customer import ImportOrderCustomer
from swagger_client.models.import_order_items import ImportOrderItems
from swagger_client.models.import_order_notes import ImportOrderNotes
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.item import Item
from swagger_client.models.manifest_order import ManifestOrder
from swagger_client.models.manifest_order_error import ManifestOrderError
from swagger_client.models.note import Note
from swagger_client.models.oauth_token import OauthToken
from swagger_client.models.oauth_token_error import OauthTokenError
from swagger_client.models.question import Question
from swagger_client.models.scanned_document import ScannedDocument
from swagger_client.models.service_order import ServiceOrder
from swagger_client.models.service_order_additional_fields import ServiceOrderAdditionalFields
from swagger_client.models.service_order_custom_fields import ServiceOrderCustomFields
from swagger_client.models.service_order_drivers import ServiceOrderDrivers
from swagger_client.models.service_order_pod import ServiceOrderPod
from swagger_client.models.service_order_signature import ServiceOrderSignature
from swagger_client.models.service_order_surveys import ServiceOrderSurveys
from swagger_client.models.service_order_truck import ServiceOrderTruck
from swagger_client.models.survey_comment import SurveyComment