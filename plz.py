from multiprocessing import Process

from DataProcess import *

VIDEO_FOLDER = 'C:/Users/MSI/Desktop/videos/'

def save_multiple_streams(streams):
    processes = []

    for stream in streams:
        hls_url = streams[stream]
        output_file = stream

        process = Process(target=convert_hls_to_mp4, args=(hls_url, output_file))
        processes.append(process)

        if len(processes) >= 6:
            for process in processes:
                process.start()
            for process in processes:
                process.join()
            processes = []

    for process in processes:
        process.start()
    for process in processes:
        process.join()

if __name__ == "__main__":
    data = request_data()
    save_multiple_streams(data)
