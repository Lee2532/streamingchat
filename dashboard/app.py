from typing import List

import lance
import pandas as pd
import streamlit as st
from conn_db import CONNECTIONDB
from models.message_model import *

st.title("Hello Streamlit")


channel = st.selectbox(
    "방송 채널을 선택해주세요",
    (
        "airikanna_stellive",
        "handongsuk",
        "runner0608",
        "silphtv",
        "tmxk319",
        "woowakgood",
    ),
)

st.write("선택한 채널 : ", channel)

if st.button("Clear All"):
    st.cache_resource.clear()

conn_db = CONNECTIONDB()

channel_message_total = conn_db.message_count_chennel_message()
channel_message_total_list: List[MESSAGECOUNTMODEL] = [
    MESSAGECOUNTMODEL(*item) for item in channel_message_total
]

channel_message_total_df = pd.DataFrame([vars(i) for i in channel_message_total_list])

# 채널별 채팅 수
st.bar_chart(channel_message_total_df, x="channel", y="count")

total_message_list = conn_db.total_chat_message(channel)
author_data = conn_db.total_author_message(channel)

data_list: List[TOTALMSAMODEL] = [TOTALMSAMODEL(*item) for item in total_message_list]

total_auth_list: List[TOTALAUTHORHMODEL] = [
    TOTALAUTHORHMODEL(*item) for item in author_data
]

# dataclass 리스트를 DataFrame으로 변환
total_message_df = pd.DataFrame([vars(i) for i in data_list])


col1, col2 = st.columns(2)
with col1:
    st.dataframe(total_message_df[:50])
with col2:
    st.bar_chart(data=total_message_df[:50], x="message", y="total")

total_auth_df = pd.DataFrame([vars(i) for i in total_auth_list])

col1, col2 = st.columns(2)
with col1:
    st.dataframe(total_auth_df[:50])
with col2:
    st.bar_chart(data=total_auth_df[:50], x="nickname", y="total")
