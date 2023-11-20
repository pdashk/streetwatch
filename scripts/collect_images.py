
#%%
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


INPUT = '../data/structure_coordinates.json'
OUTPATH = '../data/images/'


from collect_images.sunny import collect_struct_json as images_sunny

#%%
if __name__== "__main__":
    images_sunny(INPUT, OUTPATH)