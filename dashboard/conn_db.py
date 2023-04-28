from string import Template

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

    def total_chat_message(self, channel):
        """가장 많이 나온 단어"""
        sql = open("dashboard/sqls/total_chat_message.sql").read()
        query = Template(sql).substitute(
            channel=channel,
        )
        rows = self.run_query(query)
        return rows

    def total_author_message(self, channel):
        """가장 많은 채팅을 작성한 유저"""
        sql = open("dashboard/sqls/total_author_message.sql").read()
        query = Template(sql).substitute(
            channel=channel,
        )
        rows = self.run_query(query)
        return rows

    def message_count_chennel_message(self):
        """채널별 채팅 수 통계"""
        sql = open("dashboard/sqls/message_count.sql").read()
        query = Template(sql).substitute()
        rows = self.run_query(query)
        return rows

    def list_to_df(self, data, model):
        df = pd.DataFrame(data)
        return df
