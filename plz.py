from multiprocessing import Process
from DataProcess import convert_hls_to_mp4

def save_multiple_streams():
    streams = [
        {"url": "https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8", "output_file": "output1"},
        {"url": "https://klivecon-orig.fastedge.net/webrtc/test/playlist.m3u8", "output_file": "output2"},
        # 추가 스트림을 여기에 추가할 수 있습니다.
    ]
    
    processes = []
    
    for stream in streams:
        hls_url = stream["url"]
        output_file = stream["output_file"]
        
        process = Process(target=convert_hls_to_mp4, args=(hls_url, output_file))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
