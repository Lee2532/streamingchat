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
        self.topic = self.channel.split("/")[-1]
        schema_registry = CachedSchemaRegistryClient(
            {"url": constants.SCHEMA_REGISTRY_URL}
        )
        self.producer = AvroProducer(
            config=constants.KAFKA_CONFIG,
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
                        topic=self.topic,
                        value=asdict(CHATMODEL(**msg)),
                        value_schema=CHATMODEL.schema,
                    )
                except Exception as e:
                    logging.info(e)

            time.sleep(0.1)


if __name__ == "__main__":
    TwitchChat("https://www.twitch.tv/handongsuk").twitch_chat()
