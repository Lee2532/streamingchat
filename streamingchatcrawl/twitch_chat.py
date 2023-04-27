"""
트위치 웹드라이버를 통한 데이터 수집 (API는 미사용)
입력한 채널 기반으로 여러개의 웹드라이버를 띄워서 수집
"""
import logging
import time
from dataclasses import asdict
from datetime import datetime

from bs4 import BeautifulSoup
from confluent_kafka.avro import AvroProducer, CachedSchemaRegistryClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import constants
from streamingchatcrawl.models.ChatModel import CHATMODEL


class TwitchChat:
    """트위치 채팅 수집"""

    def __init__(self, channel: str):
        self.channel = channel
        # self.conf = {
        #     "bootstrap.servers": constants.BOOTSTRAPSERVER,
        #     "client.id": constants.CLIENTID,
        # }
        # self.producer = Producer(self.conf)
        schema_registry = CachedSchemaRegistryClient(
            {"url": constants.SCHEMA_REGISTRY_URL}
        )
        self.producer = AvroProducer(
            {"bootstrap.servers": constants.BOOTSTRAPSERVER},
            schema_registry=schema_registry,
        )

    def _webdriver(self) -> webdriver:
        """
        open webdriver
        :return: webdriver
        """
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("disable-gpu")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        logging.info("Webdriver open")
        return driver

    def _duduplication(self, before_list: list, after_list: list) -> list:
        """중복제거, 이전 메시지의 가장 마지막 메시지를 기반으로, 새로온 메시지 리스트중 중복 체크 후 그 이후것만 가져옴"""
        try:
            last_msg = before_list[-1]
        except Exception as e:
            return after_list

        max_num = 0
        for i in range(len(after_list)):
            if (
                last_msg["user_id"] == after_list[i]["user_id"]
                and last_msg["nickname"] == after_list[i]["nickname"]
                and last_msg["message"] == after_list[i]["message"]
            ):
                max_num = i + 1
        return after_list[max_num:]

    def twitch_chat(self):
        driver = self._webdriver()
        driver.get(self.channel)
        logging.info(f"goto {self.channel}")

        while True:
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            for i in soup.select(
                "section > div > div > div > div.scrollable-area > div.simplebar-scroll-content > div > div > div"
            ):
                try:
                    user_id = i.get("data-a-user", "")
                    nickname = i.select_one("span.chat-author__display-name").get_text()
                    message = i.select_one("span.text-fragment").get_text()

                    msg = {
                        "user_id": user_id,
                        "nickname": nickname,
                        "message": message,
                        "create_time": str(datetime.now()),
                    }

                    self.producer.produce(
                        topic=constants.TOPIC,
                        value=asdict(CHATMODEL(**msg)),
                        value_schema=CHATMODEL.schema,
                    )
                except Exception as e:
                    logging.info(e)

            time.sleep(0.1)


if __name__ == "__main__":
    TwitchChat("https://www.twitch.tv/silphtv").twitch_chat()
