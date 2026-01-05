"""日历生成模块"""

from typing import List, Tuple, Optional
from datetime import datetime
from bs4 import BeautifulSoup
from ics import Calendar, Event
from pytz import timezone
import os

from .config import Config


class CalendarGenerator:
    """日历生成器"""

    def __init__(self, config: Optional[Config] = None):
        self.config = config or Config()
        self.tz = timezone("Asia/Shanghai")

    def parse_exam_page(self, html_content: str) -> List[dict]:
        """
        解析考试页面HTML，提取考试信息

        返回: 考试信息列表
        """
        soup = BeautifulSoup(html_content, "html.parser")
        exams = []

        for row in soup.select("table#dataList tr")[1:]:
            cells = row.find_all("td")
            if len(cells) < 11:
                continue

            exam = {
                "exam_number": cells[0].text.strip(),
                "campus": cells[1].text.strip(),
                "session": cells[2].text.strip(),
                "course_code": cells[3].text.strip(),
                "course_name": cells[4].text.strip(),
                "teacher": cells[5].text.strip(),
                "exam_time": cells[6].text.strip(),
                "location": cells[7].text.strip(),
                "seat_number": cells[8].text.strip(),
            }
            exams.append(exam)

        return exams

    def create_calendar(self, exams: List[dict]) -> Calendar:
        """
        根据考试信息创建日历
        """
        calendar = Calendar()

        for exam in exams:
            try:
                # 解析考试时间
                date_str, time_range = exam["exam_time"].split(" ")
                start_time, end_time = time_range.split("~")

                start_datetime = self.tz.localize(
                    datetime.strptime(f"{date_str} {start_time}", "%Y-%m-%d %H:%M")
                )
                end_datetime = self.tz.localize(
                    datetime.strptime(f"{date_str} {end_time}", "%Y-%m-%d %H:%M")
                )

                # 创建事件
                event = Event()
                event.name = f"{exam['course_name']} - {exam['teacher']}"
                event.begin = start_datetime
                event.end = end_datetime
                event.location = exam["location"]
                event.description = (
                    f"序号: {exam['exam_number']}, 校区: {exam['campus']}, "
                    f"场次: {exam['session']}, 课程编号: {exam['course_code']}, "
                    f"座位号: {exam['seat_number']}, 考试时间: {exam['exam_time']}, "
                    f"技术支持: https://www.w1ndys.top"
                )

                calendar.events.add(event)
            except Exception as e:
                print(f"解析考试信息失败: {exam}, 错误: {e}")
                continue

        return calendar

    def generate_from_html(self, html_content: str) -> Calendar:
        """
        从HTML内容直接生成日历
        """
        exams = self.parse_exam_page(html_content)
        return self.create_calendar(exams)

    def save_calendar(self, calendar: Calendar, filename: str) -> str:
        """
        保存日历到文件

        返回: 保存的文件路径
        """
        # 确保输出目录存在
        os.makedirs(self.config.output_dir, exist_ok=True)

        filepath = os.path.join(self.config.output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(calendar.serialize())

        return filepath

    def get_exam_summary(self, exams: List[dict]) -> List[Tuple[str, str, str]]:
        """
        获取考试摘要信息

        返回: [(课程名称, 考试时间, 考场), ...]
        """
        return [(exam["course_name"], exam["exam_time"], exam["location"]) for exam in exams]
