import time
from DataProcess import reqeust_data
from flask import request

def now_time():
    return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))

def time_check():
    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        current_second = current_time.tm_sec
        print(f"현재 시간: {current_hour}시 {current_minute}분 {current_second}초")

        # 타겟 시간에 도달하면 사용자 함수 호출
        if current_second%20 == 0:
            video_data = reqeust_data(url='http://localhost:5000/inteligence/activity/')
            video_data = video_data.get("message")
            print("20초마다 호출되는 함수")

        time.sleep(1)
