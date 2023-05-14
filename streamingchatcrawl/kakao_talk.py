"""
카카오톡 대화 내용
"""
import os
import re
from datetime import datetime


class KakaoTalk:
    """
    카톡 대화
    """

    def __init__(self):
        self.file_path = "kakao_data/KakaoTalk_sample.txt"
        self.row = ""
        self.basis_dt = ""

    def is_date_line(self) -> None:
        """
        날짜가 지날경우 바뀌는 값을 가져와서 basis_date 변경
        --------------- 2022년 3월 14일 월요일 ---------------
        :return:
        """
        date_re = re.compile("-+ \d+년 \d+월 \d+일")  # 날짜

        if bool(re.search(date_re, self.row)):
            date = re.findall("\d+", self.row)
            self.basis_dt = datetime.strptime(
                f"{int(date[0])}-{int(date[1])}-{int(date[2])}", "%Y-%m-%d"
            )
            print(str(self.basis_dt))
        return None

    def read_file(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = {}
            for row in file:
                self.row = row
                self.is_date_line()


if __name__ == "__main__":
    KakaoTalk().read_file()
