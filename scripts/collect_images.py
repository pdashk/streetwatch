
#%%
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


INPUT = 'data/Q1ProjectStructureList.xlsx'
OUTPATH = 'data/images/'

from collect_images.phi import create_images as images_phi
from collect_images.alex import get_dataset as images_alex
from collect_images.brandon import collect_imgs as images_brandon
from collect_images.kevin import create_images as images_kevin
from collect_images.sunny import collect_struct_json as images_sunny


if __name__== "__main__":
    images_phi(INPUT, OUTPATH)
    images_alex()
    images_brandon(OUTPATH)
    images_kevin('data/kevin_structures.json', OUTPATH)
    images_sunny('data/structure_coordinates.json', OUTPATH)
