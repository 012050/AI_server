import time

from flask import request

from DataProcess import request_data


class TimeChecker:
    def __init__(self):
        self.video_data = None
        self.trans_list = []

    def now_time(self):
        return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))

    def time_check(self):


        check = 1
        while True:
            current_time = time.localtime()
            current_hour = current_time.tm_hour
            current_minute = current_time.tm_min
            current_second = current_time.tm_sec
            print(f"현재 시간: {current_hour}시 {current_minute}분 {current_second}초")

            # 타겟 시간에 도달하면 사용자 함수 호출
            if current_minute == 54:
            # if current_second == 0:
            # if current_second == 0 and check == 1:
            # if current_second % 10 == 0 and check == 1:

                video_data = request_data(url='http://localhost:5000/inteligence/activity/')

                # 리스트로 변환
                for data in video_data:
                    self.trans_list.append([data, video_data[data]])

                self.video_data = self.trans_list
                # check = 0
                # break

            time.sleep(1)

if __name__ == '__main__':
    time_checker = TimeChecker()
    time_checker.time_check()
