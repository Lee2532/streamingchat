from dataclasses import dataclass


@dataclass
class TOTALMSAMODEL:
    message: str
    total: int


@dataclass
class TOTALMODEL:
    user_id: str
    nickname: str
    message: str
    created_time: str
