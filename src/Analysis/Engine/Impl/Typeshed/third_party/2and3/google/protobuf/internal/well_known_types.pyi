from typing import Any, Optional

class Error(Exception): ...
class ParseError(Error): ...

# This is named 'Any' in the original, but that conflicts with typing.Any,
# and we really only need this file to mix in.
class Any_:
    type_url: Any = ...
    value: Any = ...
    def Pack(self, msg: Any, type_url_prefix: bytes = ..., deterministic: Optional[Any] = ...) -> None: ...
    def Unpack(self, msg: Any): ...
    def TypeName(self): ...
    def Is(self, descriptor: Any): ...

class Timestamp:
    def ToJsonString(self): ...
    seconds: Any = ...
    nanos: Any = ...
    def FromJsonString(self, value: Any) -> None: ...
    def GetCurrentTime(self) -> None: ...
    def ToNanoseconds(self): ...
    def ToMicroseconds(self): ...
    def ToMilliseconds(self): ...
    def ToSeconds(self): ...
    def FromNanoseconds(self, nanos: Any) -> None: ...
    def FromMicroseconds(self, micros: Any) -> None: ...
    def FromMilliseconds(self, millis: Any) -> None: ...
    def FromSeconds(self, seconds: Any) -> None: ...
    def ToDatetime(self): ...
    def FromDatetime(self, dt: Any) -> None: ...

class Duration:
    def ToJsonString(self): ...
    seconds: Any = ...
    nanos: Any = ...
    def FromJsonString(self, value: Any) -> None: ...
    def ToNanoseconds(self): ...
    def ToMicroseconds(self): ...
    def ToMilliseconds(self): ...
    def ToSeconds(self): ...
    def FromNanoseconds(self, nanos: Any) -> None: ...
    def FromMicroseconds(self, micros: Any) -> None: ...
    def FromMilliseconds(self, millis: Any) -> None: ...
    def FromSeconds(self, seconds: Any) -> None: ...
    def ToTimedelta(self): ...
    def FromTimedelta(self, td: Any) -> None: ...

class FieldMask:
    def ToJsonString(self): ...
    def FromJsonString(self, value: Any) -> None: ...
    def IsValidForDescriptor(self, message_descriptor: Any): ...
    def AllFieldsFromDescriptor(self, message_descriptor: Any) -> None: ...
    def CanonicalFormFromMask(self, mask: Any) -> None: ...
    def Union(self, mask1: Any, mask2: Any) -> None: ...
    def Intersect(self, mask1: Any, mask2: Any) -> None: ...
    def MergeMessage(self, source: Any, destination: Any, replace_message_field: bool = ..., replace_repeated_field: bool = ...) -> None: ...

class _FieldMaskTree:
    def __init__(self, field_mask: Optional[Any] = ...) -> None: ...
    def MergeFromFieldMask(self, field_mask: Any) -> None: ...
    def AddPath(self, path: Any): ...
    def ToFieldMask(self, field_mask: Any) -> None: ...
    def IntersectPath(self, path: Any, intersection: Any): ...
    def AddLeafNodes(self, prefix: Any, node: Any) -> None: ...
    def MergeMessage(self, source: Any, destination: Any, replace_message: Any, replace_repeated: Any) -> None: ...

class Struct:
    def __getitem__(self, key: Any): ...
    def __contains__(self, item: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def get_or_create_list(self, key: Any): ...
    def get_or_create_struct(self, key: Any): ...
    def update(self, dictionary: Any) -> None: ...

class ListValue:
    def __len__(self): ...
    def append(self, value: Any) -> None: ...
    def extend(self, elem_seq: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def items(self) -> None: ...
    def add_struct(self): ...
    def add_list(self): ...