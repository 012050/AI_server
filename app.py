import os
import threading
from multiprocessing import Process

from TimeControl import time_check

VIDEO_FOLDER = 'videos'

if not os.path.exists(VIDEO_FOLDER):
    os.makedirs(VIDEO_FOLDER)

if __name__ == '__main__':

    # 시간 확인 스레드 시작
    time_check_thread = threading.Thread(target=time_check)
    time_check_thread.start()
