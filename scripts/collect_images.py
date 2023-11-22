import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


INPUT = 'data/Q1ProjectStructureList.xlsx'
OUTPATH = 'data/images/'
JOSHUA_INPUT = 'data/joshua_structures.json'


from collect_images.phi import create_images as images_phi
from collect_images.joshua import create_images as images_joshua


if __name__== "__main__":
    images_phi(INPUT, OUTPATH)
    images_joshua(JOSHUA_INPUT, OUTPATH)