from mutagen.mp3 import MP3
from moviepy import editor
class MP3ToMP4:
    def __init__(self, all_images_list, audio):
        self.all_images_list = all_images_list
        self.audio = audio
        self.create_video()
    def get_length(self):
        song = MP3(self.audio)
        return int(song.info.length)
    def create_video(self):
        length_audio = self.get_length()
        image_list = self.all_images_list
        duration = int(length_audio / len(image_list)) * 1000
        image_list[0].save("temp.gif", save_all=True, append_images=image_list[1:], duration=duration)
        self.combine_audio()

    def combine_audio(self):
        video = editor.VideoFileClip("temp.gif")
        audio = editor.AudioFileClip(self.audio)
        final_video = video.set_audio(audio)
        final_video.write_videofile('test.mp4', fps=60)


if __name__ == '__main__':
    all_images_list= [] #images to be added
    text="""
    In this tutorial, we will see how to convert an Audio File (MP3) to a Video File (MP4) using static images in Python. In other words, convert Audio to Video.
We are going to follow the procedure mentioned below to implement it:
Installing and Loading the Dependencies required.
Creating a class MP3ToMP4.
Getting the length of the MP3 File and list of Images.
Creating a GIF File.
Combining GIF File with MP3.
    """
    audio = "add audio"
    MP3ToMP4(all_images_list, audio)