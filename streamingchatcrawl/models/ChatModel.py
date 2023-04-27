import json
from dataclasses import asdict, dataclass, field
from datetime import datetime

from confluent_kafka import Consumer, Producer, avro


@dataclass
class CHATMODEL:
    user_id: str
    nickname: str
    message: str
    create_time: str

    value_schema_str = """
        {
        "type": "record",
        "name": "my_record",
        "fields": [
            {"name": "user_id", "type": "string"},
            {"name": "nickname", "type": "string"},
            {"name": "message", "type": "string"},
            {"name": "create_time", "type": "string"}
            ]
        }
    """
    schema = avro.loads(value_schema_str)
