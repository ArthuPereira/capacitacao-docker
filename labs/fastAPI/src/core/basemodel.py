from datetime import datetime,timezone
from typing import Any
from pydantic import BaseModel,ConfigDict,field_serializer


class CustomModel(BaseModel):
    model_config=ConfigDict(
       from_attributes=True,
       populate_by_name=True,
    )

    @field_serializer("*",when_used="json",check_fields=False)
    def serialize_datetime(self,value:Any):
        if isinstance(value,datetime):
            return value.astimezone(timezone.utc).isoformat()
        return value

