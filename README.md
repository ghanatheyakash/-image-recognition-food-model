# -image-recognition-food-model
for visual recognition use ibm_watson
https://cloud.ibm.com/apidocs/visual-recognition/visual-recognition-v3


from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
visual_recognition = VisualRecognitionV3(
    version='{version}',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.eu-de.visual-recognition.watson.cloud.ibm.com')
   
