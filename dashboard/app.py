from typing import List

import lance
import pandas as pd
import streamlit as st
from conn_db import CONNECTIONDB
from models.message_model import TOTALMSAMODEL

st.title("Hello Streamlit")


conn_db = CONNECTIONDB()

total_message_list = conn_db.total_chat_message()


# 리스트 데이터를 dataclass 리스트로 변환
data_list: List[TOTALMSAMODEL] = [TOTALMSAMODEL(*item) for item in total_message_list]

# dataclass 리스트를 DataFrame으로 변환
total_message_df = pd.DataFrame([vars(i) for i in data_list])

st.dataframe(total_message_df)
st.line_chart(total_message_df[:20])
