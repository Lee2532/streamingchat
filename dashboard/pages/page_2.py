import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
)

from typing import List

import pandas as pd
import streamlit as st

from dashboard.conn_db import CONNECTIONDB
from dashboard.models.message_model import *

st.markdown("# Pandas Chart")
st.sidebar.markdown("# Page 2 ❄️")

conn_db = CONNECTIONDB()


channel_message_total = conn_db.message_count_chennel_message()
channel_message_total_list: List[MESSAGECOUNTMODEL] = [
    MESSAGECOUNTMODEL(*item) for item in channel_message_total
]

channel_message_total_df = pd.DataFrame([vars(i) for i in channel_message_total_list])

st.pyplot(channel_message_total_df.plot().figure)
