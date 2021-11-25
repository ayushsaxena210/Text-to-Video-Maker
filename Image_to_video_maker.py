# Loading all the packages required
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
from moviepy import editor
from gtts import gTTS
import os
import secrets
import string

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')

def get_words(lines):
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(lines)
    nouns = [''.join(re.sub('[^a-zA-Z]', ' ', word).split()) for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    nouns = [word for word in nouns if word!='']
    return(nouns)

def generate_random_names():
    N = 7
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    return str(res)


def text_to_voice(text, language='en'):
    obj = gTTS(text=text, lang=language, slow=False)
    file_name = generate_random_names()+".mp3"
    obj.save(file_name)
    #os.system("start welcome.mp3")
    return file_name



import requests
import io
try:
    import Image
except ImportError:
    from PIL import Image

def get_image(keywords):
    src = "https://source.unsplash.com/1200x500/?"+keywords
    response = requests.get(src)
    image_bytes = io.BytesIO(response.content)
    img = Image.open(image_bytes).resize((800, 800), Image.ANTIALIAS)
    #img.show()
    return img


'''
Creating class MP3ToMP4 which contains methods to convert
an audio to a video using a list of images.
'''


class MP3ToMP4:

    def __init__(self, all_images_list, audio):
        """
        :param folder_path: contains the path of the root folder.
        :param audio_path: contains the path of the audio (mp3 file).
        :param video_path_name: contains the path where the created
                                video will be saved along with the
                                name of the created video.
        """
        self.all_images_list = all_images_list
        self.audio = audio
        self.create_video()

    def get_length(self):
        """
        This method reads an MP3 file and calculates its length
        in seconds.

        :return: length of the MP3 file
        """
        song = MP3(self.audio)
        return int(song.info.length)

    def get_images(self):
        """
        This method reads the filenames of the images present
        in the folder_path of type '.png' and stores it in the
        'images' list.

        Then it opens the images, resizes them and appends them
        to another list, 'image_list'

        :return: list of opened images

        path_images = Path(self.folder_path)
        images = list(path_images.glob('*.png'))
        image_list = self.folder_path
        for image_name in images:
            image = Image.open(image_name).resize((800, 800), Image.ANTIALIAS)
            image_list.append(image)
        return image_list"""
        pass

    def create_video(self):
        """
        This method calls the get_length() and get_images()
        methods internally. It then calculates the duration
        of each frame. After that, it saves all the opened images
        as a gif using the save() method. Finally it calls the
        combine_method()

        :return: None
        """
        length_audio = self.get_length()
        image_list = self.all_images_list
        duration = int(length_audio / len(image_list)) * 1000
        image_list[0].save("temp.gif", save_all=True, append_images=image_list[1:], duration=duration)
        # Calling the combine_audio() method.
        self.combine_audio()

    def combine_audio(self):
        """
        This method attaches the audio to the gif file created.
        It opens the gif file and mp3 file and then uses
        set_audio() method to attach the audio. Finally, it
        saves the video to the specified video_path_name

        :return: None
        """
        video = editor.VideoFileClip("temp.gif")
        audio = editor.AudioFileClip(self.audio)
        final_video = video.set_audio(audio)
        final_video.write_videofile('test.mp4', fps=60)


if __name__ == '__main__':
    all_images_list=[]
    text="""
    In this tutorial, we will see how to convert an Audio File (MP3) to a Video File (MP4) using static images in Python. In other words, convert Audio to Video.
We are going to follow the procedure mentioned below to implement it:
Installing and Loading the Dependencies required.
Creating a class MP3ToMP4.
Getting the length of the MP3 File and list of Images.
Creating a GIF File.
Combining GIF File with MP3.
    """

    audio = text_to_voice(text)
    keywords = get_words(text)
    for keyword in keywords:
        all_images_list.append(get_image(keywords=keyword))
    MP3ToMP4(all_images_list, audio)