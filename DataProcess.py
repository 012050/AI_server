import time
import subprocess
import os

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
        # ffmpeg command to convert HLS to MP4
        cmd = ['ffmpeg', '-i', hls_url, '-t', str(duration), '-c', 'copy', "videos/" + output_file + ".mp4"]

        # Run the ffmpeg command
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the conversion was successful
        if result.returncode == 0:
            print(f"Video saved as {output_file}")
        else:
            print(f"Error occurred: {result.stderr}")
        return result.returncode

    except subprocess.CalledProcessError as e:
        print(f"\n\n\nError occurred: {e}\n\n\n")

def now_time():
    return time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))