import os

import ffmpeg
import requests

# 영상 저장 함수
def convert_hls_to_mp4(hls_url="https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8", output_file="test", duration=10):
    file_path=os.getcwd() +  "\\videos\\" + output_file + ".mp4"

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

# 인공지능 서버에 데이터 전송
def send_data(url='http://127.0.0.1:5001/object_detection', file_name=os.getcwd() + "/videos/TEST_00001"):

    try:
        response = requests.get(url+file_name)

        if response.status_code == 200:
            print('API 요청이 성공적으로 전송되었습니다.')
            return response.text
        else:
            print('API 요청 전송에 실패하였습니다.')
            return response.status_code

    except Exception as e:
        print('API 요청 전송에 실패하였습니다.')
        print(e)
        return 404

def request_data(url='http://localhost:5000/inteligence/activity/'):

    try:
        response = requests.post(url)

        if response.status_code == 200:
            print('영상 데이터 요청이 성공적으로 전송되었습니다.')
            return response.json()
        else:
            print('영상 데이터 요청에 전송에 실패하였습니다.')
            return response.status_code

    except Exception as e:
        print('API 요청 전송에 실패하였습니다.')
        print(e)
        return None

def delete_all_files_in_folder(target_folder):
    try:
        for filename in os.listdir(target_folder):
            file_path = os.path.join(target_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting files: {e}")

if __name__ == "__main__":
    # convert_hls_to_mp4(output_file="TEST_00001")
    result = send_data(url="http://localhost:5001/object_detection", file_name=os.getcwd() + "/videos/TEST_00001")
    print(result)
