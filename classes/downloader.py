import subprocess
import requests
import os
from io import BytesIO
from colorthief import ColorThief
from PIL import Image, ImageQt
from moviepy.editor import VideoFileClip, AudioFileClip

from pytube import YouTube, Stream
from pytube.cli import on_progress

counter = 1

class Downloader(YouTube):
    def __init__(self, url: str, *args, **kwargs):
        super().__init__(url, *args, **kwargs)
        # self.register_on_complete_callback(self.complete_function)
        # self.register_on_progress_callback(self.progress_function)

    @classmethod
    def complete_function(cls, stream: Stream, file_path):
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

    def download_video(self, itag, filename=None, folder=None):
        stream = self.streams.get_by_itag(itag)

        if stream.audio_codec:
            stream.download(filename=filename, output_path=folder)
        else:
            stream.download(filename='temp_video.mp4', output_path='temp')
            fps = stream.fps
            vid_path = os.path.join('temp', 'temp_video.mp4')
            print('+')

            audio = self.get_highest_resolution_audio()
            audio.download(filename='temp_audio.mp4', output_path='temp')
            aud_path = os.path.join('temp', 'temp_audio')
            print('+')

            if filename is not None and folder is not None:
                out_path = os.path.join(folder, filename)
            else:
                out_path = stream.default_filename

            self.combine_audio(vid_path, aud_path, out_path, fps=fps)

    def combine_audio(vidname, audname, outname, fps=30):
        video = VideoFileClip(vidname)
        audio = AudioFileClip(audname)
        final = video.set_audio(audio)
        final.write_videofile(outname, fps=fps)

    def get_equivalent(self):
        dct = {}
        for stream in self.streams.filter(type='video', subtype='mp4'):
            if stream.audio_codec:
                for video in self.get_videos():
                    if stream.resolution == video.resolution:
                        dct[video.itag] = stream.itag

        return dct

    def get_videos(self):
        # return [stream for stream in self.streams.filter(type='video', subtype='mp4') if stream.video_codec.startswith('avc1')]
        streams = []
        for stream in self.streams.filter(type='video', subtype='mp4'):
            if stream.video_codec.startswith('avc1') and not stream.audio_codec:
                streams.append(stream)

        return streams

    def get_highest_resolution_video(self):
        highest = 0
        itag = 0
        for stream in self.streams.filter(type='video', subtype='mp4'):
            res = int(stream.resolution[:-1])
            if res > highest:
                highest = res
                itag = stream.itag

        return self.streams.get_by_itag(itag)

    def get_highest_resolution_audio(self):
        highest = 0
        itag = 0
        for stream in self.streams.filter(type='audio', subtype='mp4'):
            abr = int(stream.abr[:-4])
            if abr > highest:
                highest = abr
                itag = stream.itag

        return self.streams.get_by_itag(itag)

    def load_image_bytes(self):
        response = requests.get(self.thumbnail_url).content

        bytes = BytesIO(response)

        return bytes

    def load_thumbnail(self, qt=True, resize=True):
        bytes = self.load_image_bytes()

        img = Image.open(bytes)
        if resize:
            factor = max(img.size)//162
            img = img.reduce(factor)
        
        if qt:
            return ImageQt.ImageQt(img)
        else:
            return img

    def load_cover(self, qt=True):
        img_init = self.load_thumbnail(qt=False, resize=False)
        bytes = self.load_image_bytes()

        ct = ColorThief(bytes)
        dominant_color = ct.get_color(quality=1)

        wi, hi = img_init.size

        if wi != hi:
            x = max(wi, hi)

            img_blank = Image.new('RGB', (x, x), dominant_color)
            wb, hb = img_blank.size

            xo = abs(wi-wb)//2
            yo = abs(hi-hb)//2
            offset = (xo, yo)

            img_blank.paste(img_init, offset)

            img = img_blank
        else:
            img = img_init

            img = img.resize((162, 162))
        if qt:
            return ImageQt.ImageQt(img)
        else:
            return img

    def print_streams(self):
        for s in self.streams:
            print(s)

# d = Downloader('https://www.youtube.com/watch?v=nJ0aFq1ve0M')
# streams = d.streams.filter(type='video', subtype='mp4')
# stream = streams[0]
# print(stream.fps)
# d.download_video(133)