import os
import threading
from multiprocessing import Process

from DataProcess import convert_hls_to_mp4, send_data
from TimeControl import TimeChecker

VIDEO_FOLDER = os.getcwd() + "\\videos\\"
# 영상 저장 폴더 생성
if not os.path.exists(VIDEO_FOLDER):
    os.makedirs(VIDEO_FOLDER)

if __name__ == '__main__':

    # 시간 확인 객체 생성
    time_checker = TimeChecker()

    # 시간 확인 스레드 시작
    time_check_thread = threading.Thread(target=time_checker.time_check)
    time_check_thread.start()

    while True:
        if time_checker.video_data is not None:
            video_data = time_checker.video_data
            time_checker.video_data = None
            time_checker.trans_list = []

            streams = video_data
            processes = []

            # 영상 처리
            for stream in streams:
                hls_url = streams[stream][0]
                output_file = streams[stream][1]

                process = Process(target=convert_hls_to_mp4, args=(hls_url, output_file, 180))
                processes.append(process)

                # 20개로 나눠서 실행
                if len(processes) >= 20:
                    for process in processes:
                        process.start()
                    for process in processes:
                        process.join()
                        
                    processes = []

            # 나머지 프로세스 실행
            for process in processes:
                process.start()
            for process in processes:
                process.join()

            processes = []

            # 인공지능 실행
            for data in streams:
                url = 'http://localhost:5001/object_detection'
                filename = VIDEO_FOLDER + streams[data][1]
                id = streams[data][2]
                userdevice = streams[data][1]
                # 인공지능 서버에 데이터 전송
                process = Process(target=send_data, args=(url, filename, id, userdevice))
                processes.append(process)

                if len(processes) >= 2:
                    for process in processes:
                        process.start()
                    for process in processes:
                        process.join()

                    processes = []

            for process in processes:
                process.start()
            for process in processes:
                process.join()
            processes = []
