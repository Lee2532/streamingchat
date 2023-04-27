import mysql.connector
import pandas as pd
import streamlit as st


class CONNECTIONDB:
    def __init__(self):
        self.conn = self.init_connection()

    @st.cache_resource
    def init_connection(_self):
        return mysql.connector.connect(**st.secrets["mysql"])

    def run_query(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def total_chat_message(self):
        query = open("dashboard/sqls/total_chat_message.sql").read()
        rows = self.run_query(query)
        return rows

    def list_to_df(self, data, model):
        df = pd.DataFrame(data)
        return df
