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
        self.line = ""
        self.basis_dt = ""
        self.lines = ""

    def is_date_line(self) -> bool:
        """
        날짜가 지날경우 바뀌는 값을 가져와서 basis_date 변경
        --------------- 2022년 3월 14일 월요일 ---------------
        :return: True, False
        """
        date_re = re.compile("-+ \d+년 \d+월 \d+일")  # 날짜

        if bool(re.search(date_re, self.line)):
            date = re.findall("\d+", self.line)
            self.basis_dt = str(
                datetime.strptime(
                    f"{int(date[0])}-{int(date[1])}-{int(date[2])}", "%Y-%m-%d"
                ).date()
            )
            return True
        return False

    def is_entry_exit(self):
        """
        누군가 입장, 퇴장했습니다 구분
        :return:
        """
        entry_re = re.compile(".*님을 초대하였습니다.")
        exit_re = re.compile(".*님이 나갔습니다.")

        if bool(re.search(entry_re, self.line)) or bool(re.search(exit_re, self.line)):
            return True
        return False

    def _parsing(self):
        """
        메시지 분석하는 로직
        :return:
        """
        pattern = r"\[([\w\s\-\[\]]+)\]\s*\[([\w\s:]+)\]\s*(.+)"

        messages = []
        current_message = None

        for line in self.lines:
            self.line = line

            if self.is_date_line() or self.is_entry_exit():
                continue

            match = re.match(pattern, line)
            if match:
                name = match.group(1)
                time = match.group(2)
                message = match.group(3)

                if current_message:
                    messages.append(current_message)

                current_message = {
                    "basis_dt": self.basis_dt,
                    "name": name,
                    "time": time,
                    "message": message,
                }
            elif current_message:
                current_message["message"] += "\n" + line.strip()

        if current_message:
            messages.append(current_message)

        for msg in messages:
            print(msg)

    def main(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        self.lines = lines
        self._parsing()


if __name__ == "__main__":
    KakaoTalk().main()
