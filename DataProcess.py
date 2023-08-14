import os
import ffmpeg
import requests

# URL 포맷 형식 정하기
# URL 형태가 어떻게 되는지 확인하기
# JSON 형태로 받아오기

# 영상 저장 함수
def convert_hls_to_mp4(hls_url="https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8", output_file="test", duration=10):
    file_path="videos/" + output_file + ".mp4"

    # 파일이 존재하면 삭제
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print(f"File '{file_path}' does not exist.")

    # 영상 저장
    try:
        ffmpeg.input(hls_url, t=duration).output(file_path, c="copy").run()
        print(f"Video saved as {output_file}")
    except ffmpeg.Error as e:
        print(f"Error occurred: {e}")

# API 서버에 데이터 천송
def send_data(url='http://localhost:5000/inteligence/activity/'):

    data = {"state": "start"}

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print('API 요청이 성공적으로 전송되었습니다.')
            return 200
        else:
            print('API 요청 전송에 실패하였습니다.')
            return response.status_code

    except Exception as e:
        print('API 요청 전송에 실패하였습니다.')
        print(e)
        return 404