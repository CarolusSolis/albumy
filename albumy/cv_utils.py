from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
from dotenv import load_dotenv
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
# Load environment variables from .env file in parent folder
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

if not subscription_key or not endpoint:
    raise Exception("VISION_KEY or VISION_ENDPOINT not set in environment variables")

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

def get_caption_local(image_path, verbose=False):
    if verbose:
        print("===== Describe an image - local ===== at " + image_path)
    local_image = open(image_path, "rb")
    description_result = computervision_client.describe_image_in_stream(local_image)
    captions = description_result.captions
    if len(captions) == 0:
        if verbose:
            print("No description detected.")
            print()
        return None
    caption = description_result.captions[0].text
    if verbose:
        print(caption)
        print()
    return caption


if __name__ == "__main__":  # this is for testing purposes
    get_caption_local(sys.argv[1], True)