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

    def _parser(self):
        """chat parsing"""
        pattern = r"\[([\w\s\-\[\]]+)\]\s*\[([\w\s:]+)\]\s*(.+)"

        data = {}
        match = re.match(pattern, self.row)
        if match:
            nickname = match.group(1)
            date = match.group(2)
            message = match.group(3)
            data["nickname"] = nickname
            data["date"] = date
            data["message"] = message
            data["basis_date"] = self.basis_dt

            # print(f"Nickname: {nickname}")
            # print(f"Date: {date}")
            # print(f"Message: {message}")
            print(data)
        else:
            print("No match found")
            print(self.row)
        return None

    def read_file(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = {}
            for row in file:
                self.row = row
                self.is_date_line()
                self._parser()


if __name__ == "__main__":
    KakaoTalk().read_file()
