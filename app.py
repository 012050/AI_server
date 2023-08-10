from flask import Flask, request, jsonify
import threading
import time
import requests
import json
import os

from DataProcess import convert_hls_to_mp4
from TimeControl import time_check
from plz import save_multiple_streams

program_counter = 0

app = Flask(__name__)
video_folder = 'videos'
app.config['VIDEO_FOLDER'] = video_folder

if not os.path.exists(video_folder):
    os.makedirs(video_folder)

# 사용자 함수: 데이터를 전송하는 함수
def send_data(UserID='abcd', VideoID='test_video_id', VideoURL='https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8', VideoTime='10'):
    global program_counter
    program_counter += 1
    print("영상 다운로드 시작")
    print(f"hls_url='{VideoURL}', output_file='{VideoID}', duration='{VideoTime}'")
    convert_hls_to_mp4(hls_url=VideoURL, output_file=UserID+VideoID+str(program_counter), duration=int(VideoTime))

# 타겟 시간 설정
target_hour = 1
target_minute = 30
target_second_0 = 0
target_second_1 = 30

# 라우트 생성 (실제로 사용하지 않지만 Flask 서버를 동작시키기 위해 빈 라우트 추가)
@app.route('/')
def home():
    return "Flask Server is Running"

# 스레드로 동작할 함수

if __name__ == '__main__':
    # Flask 서버 스레드 시작
    server_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000, 'debug': False, 'threaded': True})
    server_thread.start()

    # 시간 확인 스레드 시작
    time_check_thread = threading.Thread(target=time_check)
    time_check_thread.start()
