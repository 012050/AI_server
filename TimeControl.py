import time

from DataProcess import request_video_data


class TimeChecker:
    def __init__(self):
        self.video_data = None

        self.disable = False
        self.present_time = time.localtime().tm_min

    def now_time(self):
        return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))

    def time_check(self):

        while True:
            current_time = time.localtime()
            current_hour = current_time.tm_hour
            current_minute = current_time.tm_min
            current_second = current_time.tm_sec
            print(f"time_check: 현재 시간: {current_hour}시 {current_minute}분 {current_second}초")

            # 타겟 시간이 되면 데이터 요청
            if (current_minute == 0 or current_minute == 30) and self.disable is False:

                video_data = request_video_data(url='http://localhost:5000/video/server/')

                self.video_data = video_data
                self.disable = True

            if self.present_time != current_minute:
                self.disable = False
                self.present_time = current_minute

            time.sleep(1)

if __name__ == '__main__':
    time_checker = TimeChecker()
    time_checker.time_check()
