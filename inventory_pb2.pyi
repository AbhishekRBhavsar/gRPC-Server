from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Inventory(_message.Message):
    __slots__ = ["inventory_id", "name", "description", "unit_price", "quantity_in_stock", "inventory_value", "reorder_level", "reorder_time", "reorder_quantity", "discontinued"]
    INVENTORY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_IN_STOCK_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_VALUE_FIELD_NUMBER: _ClassVar[int]
    REORDER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    REORDER_TIME_FIELD_NUMBER: _ClassVar[int]
    REORDER_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DISCONTINUED_FIELD_NUMBER: _ClassVar[int]
    inventory_id: str
    name: str
    description: str
    unit_price: int
    quantity_in_stock: int
    inventory_value: int
    reorder_level: int
    reorder_time: int
    reorder_quantity: int
    discontinued: bool
    def __init__(self, inventory_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., unit_price: _Optional[int] = ..., quantity_in_stock: _Optional[int] = ..., inventory_value: _Optional[int] = ..., reorder_level: _Optional[int] = ..., reorder_time: _Optional[int] = ..., reorder_quantity: _Optional[int] = ..., discontinued: bool = ...) -> None: ...

class SearchByIdRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SearchByIdResponse(_message.Message):
    __slots__ = ["inventory"]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    inventory: Inventory
    def __init__(self, inventory: _Optional[_Union[Inventory, _Mapping]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ["key_name", "key_value"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    key_value: int
    def __init__(self, key_name: _Optional[str] = ..., key_value: _Optional[int] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ["inventories"]
    INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    inventories: _containers.RepeatedCompositeFieldContainer[Inventory]
    def __init__(self, inventories: _Optional[_Iterable[_Union[Inventory, _Mapping]]] = ...) -> None: ...

class SearchInRangeRequest(_message.Message):
    __slots__ = ["key_name", "min_value", "max_value"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    min_value: int
    max_value: int
    def __init__(self, key_name: _Optional[str] = ..., min_value: _Optional[int] = ..., max_value: _Optional[int] = ...) -> None: ...

class SearchInRangeResponse(_message.Message):
    __slots__ = ["inventories"]
    INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    inventories: _containers.RepeatedCompositeFieldContainer[Inventory]
    def __init__(self, inventories: _Optional[_Iterable[_Union[Inventory, _Mapping]]] = ...) -> None: ...

class GetDistributionRequest(_message.Message):
    __slots__ = ["key_name", "percentile"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    PERCENTILE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    percentile: float
    def __init__(self, key_name: _Optional[str] = ..., percentile: _Optional[float] = ...) -> None: ...

class GetDistributionResponse(_message.Message):
    __slots__ = ["percentile"]
    PERCENTILE_FIELD_NUMBER: _ClassVar[int]
    percentile: float
    def __init__(self, percentile: _Optional[float] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ["key_name", "key_value", "update_key_name", "update_value"]
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VALUE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    key_value: int
    update_key_name: str
    update_value: int
    def __init__(self, key_name: _Optional[str] = ..., key_value: _Optional[int] = ..., update_key_name: _Optional[str] = ..., update_value: _Optional[int] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ["updated"]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    updated: bool
    def __init__(self, updated: bool = ...) -> None: ...
