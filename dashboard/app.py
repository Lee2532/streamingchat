from typing import List

import lance
import pandas as pd
import streamlit as st
from conn_db import CONNECTIONDB
from models.message_model import *

st.title("Hello Streamlit")


conn_db = CONNECTIONDB()

total_message_list = conn_db.total_chat_message()
author_data = conn_db.total_author_message()

data_list: List[TOTALMSAMODEL] = [TOTALMSAMODEL(*item) for item in total_message_list]

total_auth_list: List[TOTALAUTHORHMODEL] = [
    TOTALAUTHORHMODEL(*item) for item in author_data
]

# dataclass 리스트를 DataFrame으로 변환
total_message_df = pd.DataFrame([vars(i) for i in data_list])
total_auth_df = pd.DataFrame([vars(i) for i in total_auth_list])

st.dataframe(total_message_df)
st.dataframe(total_auth_df[:20])
