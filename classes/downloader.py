import subprocess
import time
import sys

from pytube import YouTube, Stream
from pytube.cli import on_progress

counter = 1

class Downloader(YouTube):
    def __init__(self, url: str, *args, **kwargs):
        super().__init__(url, *args, **kwargs)
        # self.register_on_complete_callback(self.complete_function)
        # self.register_on_progress_callback(self.progress_function)

    def donwload_highest_quality(self):
        highest = 0
        itag = 0
        v_streams = self.streams.filter(type='video', subtype='mp4')
        for s in v_streams:
            res = int(s.resolution[:-1])
            if res > highest:
                highest = res
                itag = s.itag
        
        to_download = self.streams.get_by_itag(itag)

        to_download.download()

    def complete_function(self, stream: Stream, file_path):
        print(f'Download of {stream.title} complete')

    @classmethod
    def progress_function(cls, stream: Stream, chunk, bytes_remaining):
        global counter

        subprocess.call('cls', shell=True)

        total_b = stream.filesize
        total_mb = total_b/(1024**2)
        downloaded_b = total_b - bytes_remaining
        donwloaded_mb = downloaded_b/(1024**2)
        downloaded_per = round(100*downloaded_b/total_b)

        print(f'Downloading {stream.title}...')
        print(f'Dowloaded {donwloaded_mb}MB out of {total_mb}MB ({downloaded_per}%)\n{counter}\n')

    def print_streams(self):
        for s in self.streams:
            print(s)

# import os
# path = 'Busta Rhymes Feat Eminem - Ill Hurt You.mp4'
# path2 = 'Trying to do Simple Tasks on Linux lol.mp4'

# link = 'https://www.youtube.com/watch?v=WgEtUuEK-to'
# link2 = 'https://www.youtube.com/watch?v=TtsglXhbxno'

# d = Downloader('https://www.youtube.com/watch?v=-SrrC9jMbjU')
# print(d.thumbnail_url)

# def main(path, link):
#     if os.path.exists(path):
#         os.remove(path)

#     yt = Downloader(link, on_progress_callback=Downloader.progress_function)

    # yt.donwload_highest_quality()

# main(path, link)