
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

get_image(keywords="soil")