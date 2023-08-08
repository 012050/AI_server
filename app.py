from flask import Flask, request, jsonify
import threading, time
from DataProcess import now_time, convert_hls_to_mp4
import requests
import json
import os

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

@app.route('/count', methods=['POST'])
def count():
    data = request.get_json()
    print(data)
    count = data.get('count')
    fin = data.get('check')
    if fin == "fin":
        print("데이터 전송 완료")
    else:
        print(f"\n\n\n\n{count}")
    return jsonify({'message': 'Success'})


# 스레드로 동작할 함수
def time_check_thread():
    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        current_second = current_time.tm_sec
        print(f"현재 시간: {current_hour}시 {current_minute}분 {current_second}초")

        # 타겟 시간에 도달하면 사용자 함수 호출
        if current_minute == target_minute or current_second == target_second_0 or current_second == target_second_1:
            send_data()

        time.sleep(1)

if __name__ == '__main__':
    # Flask 서버 스레드 시작
    server_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000, 'debug': False, 'threaded': True})
    server_thread.start()

    # 시간 확인 스레드 시작
    time_check_thread = threading.Thread(target=time_check_thread)
    time_check_thread.start()
