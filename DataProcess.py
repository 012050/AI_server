import os
import ffmpeg

# URL 포맷 형식 정하기
# URL 형태가 어떻게 되는지 확인하기
# JSON 형태로 받아오기

def convert_hls_to_mp4(hls_url="https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8", output_file="test", duration=10):
    file_path="videos/" + output_file + ".mp4"
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")
    else:
        print(f"File '{file_path}' does not exist.")
    try:
        ffmpeg.input(hls_url, t=duration).output(file_path, c="copy").run()
        print(f"Video saved as {output_file}")
    except ffmpeg.Error as e:
        print(f"Error occurred: {e}")
