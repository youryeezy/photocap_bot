from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("phone", "url", "abonent", "lac", "cell", "azimut", "bs_address")
    PHONE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ABONENT_FIELD_NUMBER: _ClassVar[int]
    LAC_FIELD_NUMBER: _ClassVar[int]
    CELL_FIELD_NUMBER: _ClassVar[int]
    AZIMUT_FIELD_NUMBER: _ClassVar[int]
    BS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    phone: int
    url: str
    abonent: str
    lac: int
    cell: int
    azimut: int
    bs_address: str
    def __init__(self, phone: _Optional[int] = ..., url: _Optional[str] = ..., abonent: _Optional[str] = ..., lac: _Optional[int] = ..., cell: _Optional[int] = ..., azimut: _Optional[int] = ..., bs_address: _Optional[str] = ...) -> None: ...

class IsSuccessfully(_message.Message):
    __slots__ = ("is_successfully",)
    IS_SUCCESSFULLY_FIELD_NUMBER: _ClassVar[int]
    is_successfully: bool
    def __init__(self, is_successfully: bool = ...) -> None: ...
