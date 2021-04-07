# ImportOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_number** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** | Use this if you are using DispatchTrack Customer Self Scheduling System | [optional] [default to 'New']
**ready_to_schedule_date** | **str** | Use this if you are using DispatchTrack Customer Self Scheduling System | [optional] 
**schedule_before_date** | **str** | Use this if you are using DispatchTrack Customer Self Scheduling System | [optional] 
**delivery_date** | **str** |  | [optional] 
**delivery_time_window_start** | **str** |  | [optional] 
**delivery_time_window_end** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**cod_amount** | **float** |  | [optional] 
**cube** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**pieces** | **float** |  | [optional] 
**delivery_charge** | **float** |  | [optional] 
**taxes** | **float** |  | [optional] 
**skill_level** | **float** |  | [optional] 
**equipment_type** | **str** |  | [optional] 
**additional_fields** | [**ImportOrderAdditionalFields**](ImportOrderAdditionalFields.md) |  | [optional] 
**custom_fields** | [**ImportOrderCustomFields**](ImportOrderCustomFields.md) |  | [optional] 
**customer** | [**ImportOrderCustomer**](ImportOrderCustomer.md) |  | [optional] 
**items** | [**list[ImportOrderItems]**](ImportOrderItems.md) |  | [optional] 
**notes** | [**list[ImportOrderNotes]**](ImportOrderNotes.md) | Notes (op) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

