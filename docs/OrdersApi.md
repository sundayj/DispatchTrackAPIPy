# swagger_client.OrdersApi

All URIs are relative to *https://dtdapi.dispatchtrack.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_order_post**](OrdersApi.md#add_order_post) | **POST** /add-order | Add Orders
[**delete_order_delete**](OrdersApi.md#delete_order_delete) | **DELETE** /delete-order | Delete Orders
[**export_post**](OrdersApi.md#export_post) | **POST** /export | Export Orders
[**oauth2_token_post**](OrdersApi.md#oauth2_token_post) | **POST** /oauth2/token | Get Oauth2 Access Token

# **add_order_post**
> AddOrderSuccess add_order_post(body)

Add Orders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body() # Body | 

try:
    # Add Orders
    api_response = api_instance.add_order_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->add_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | 

### Return type

[**AddOrderSuccess**](AddOrderSuccess.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order_delete**
> DeleteOrderSuccess delete_order_delete(order_number, _date=_date)

Delete Orders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
order_number = 'order_number_example' # str | Order Numbers - comma separated list
_date = '_date_example' # str | Date (mm/dd/yyyy) (optional)

try:
    # Delete Orders
    api_response = api_instance.delete_order_delete(order_number, _date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->delete_order_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **str**| Order Numbers - comma separated list | 
 **_date** | **str**| Date (mm/dd/yyyy) | [optional] 

### Return type

[**DeleteOrderSuccess**](DeleteOrderSuccess.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_post**
> InlineResponse200 export_post(body=body)

Export Orders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Export Orders
    api_response = api_instance.export_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_token_post**
> OauthToken oauth2_token_post(grant_type=grant_type)

Get Oauth2 Access Token

> Note: The Client ID and Secret aren't included in the POST body, but rather are placed in the HTTP Authorization header following the rules of HTTP Basic Auth. ```   # Header sample    Authorization: Basic c2FjbGllbnRpZDpzYWNsaWVudHNlY3JldA==    # base64(clientId + \":\" + clientSecret) generates c2FjbGllbnRpZDpzYWNsaWVudHNlY3JldA== ``` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: GetTokenAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
grant_type = 'grant_type_example' # str |  (optional)

try:
    # Get Oauth2 Access Token
    api_response = api_instance.oauth2_token_post(grant_type=grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->oauth2_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [optional] 

### Return type

[**OauthToken**](OauthToken.md)

### Authorization

[GetTokenAuth](../README.md#GetTokenAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

