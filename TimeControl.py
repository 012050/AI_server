import time

from flask import request

from DataProcess import request_data


class TimeChecker:
    def __init__(self):
        self.video_data = None

    def now_time(self):
        return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))

    def time_check(self):
        while True:
            current_time = time.localtime()
            current_hour = current_time.tm_hour
            current_minute = current_time.tm_min
            current_second = current_time.tm_sec
            print(f"현재 시간: {current_hour}시 {current_minute}분 {current_second}초")

            # 타겟 시간에 도달하면 사용자 함수 호출
            if current_second % 20 == 0:
                self.video_data = request_data(url='http://localhost:5000/inteligence/activity/')
                print("20초마다 호출되는 함수")

            time.sleep(1)
