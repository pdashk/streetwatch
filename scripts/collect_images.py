import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


INPUT = 'data/jonathan_structures.json'
OUTPATH = 'data/jonathan_images/'


from collect_images.jonathan import get_images as images_jonathan


if __name__== "__main__":
    images_jonathan(INPUT, OUTPATH)