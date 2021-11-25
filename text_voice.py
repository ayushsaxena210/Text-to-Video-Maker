from gtts import gTTS
import os
import secrets
import string


def generate_random_names():
    N = 7
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(N))
    return str(res)


def text_to_voice(text, language='en'):
    obj = gTTS(text=text, lang=language, slow=False)
    file_name = generate_random_names()+".mp3"
    obj.save(file_name)
    #os.system("start welcome.mp3")
    return obj, file_name

text_to_voice(text="Modi chutiya")
