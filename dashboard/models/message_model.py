from dataclasses import dataclass


@dataclass
class TOTALMSAMODEL:
    """가장 많이 나온 단어"""

    message: str
    total: int


@dataclass
class TOTALMODEL:
    """채팅 전체 목록"""

    user_id: str
    nickname: str
    message: str
    created_time: str


@dataclass
class TOTALAUTHORHMODEL:
    """가장 많이 채팅을 작성한 사람"""

    nickname: str
    total: int
