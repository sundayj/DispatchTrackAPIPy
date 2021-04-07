# swagger_client.RouteApi

All URIs are relative to *https://dtdapi.dispatchtrack.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manifest_post**](RouteApi.md#manifest_post) | **POST** /manifest | Manifest Export

# **manifest_post**
> InlineResponse2001 manifest_post(body=body)

Manifest Export

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RouteApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Manifest Export
    api_response = api_instance.manifest_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->manifest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

