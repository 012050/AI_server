import os
import threading
from multiprocessing import Process

from DataProcess import convert_hls_to_mp4, send_data
from TimeControl import TimeChecker

VIDEO_FOLDER = 'videos'

if not os.path.exists(VIDEO_FOLDER):
    os.makedirs(VIDEO_FOLDER)

if __name__ == '__main__':

    # 시간 확인 객체 생성
    time_checker = TimeChecker()

    # 시간 확인 스레드 시작
    time_check_thread = threading.Thread(target=time_checker.time_check)
    time_check_thread.start()
