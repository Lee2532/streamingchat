from typing import List

import lance
import pandas as pd
import streamlit as st
from conn_db import CONNECTIONDB
from models.message_model import *

st.title("Hello Streamlit")


channel = st.selectbox("방송 채널을 선택해주세요", ("silphtv", "handongsuk", "tmxk319"))

st.write("선택한 채널 : ", channel)

conn_db = CONNECTIONDB()

total_message_list = conn_db.total_chat_message(channel)
author_data = conn_db.total_author_message(channel)

data_list: List[TOTALMSAMODEL] = [TOTALMSAMODEL(*item) for item in total_message_list]

total_auth_list: List[TOTALAUTHORHMODEL] = [
    TOTALAUTHORHMODEL(*item) for item in author_data
]

# dataclass 리스트를 DataFrame으로 변환
total_message_df = pd.DataFrame([vars(i) for i in data_list])
total_auth_df = pd.DataFrame([vars(i) for i in total_auth_list])

st.dataframe(total_message_df[:50])
st.dataframe(total_auth_df[:50])

st.bar_chart(total_auth_df[:50])
