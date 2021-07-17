import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
r = sr.Recognizer()
authenticator = IAMAuthenticator('6S6TUNQa0D8yXdfV6dwmAYgSQ8PQ1EN6ZE-7_RlTSO_c') 
speech_to_text = SpeechToTextV1(authenticator = authenticator)
   
#Insert URL in place of 'API_URL' 
speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/2c29ce92-c572-46ff-b4a1-02769702d7ef')
name = "expert"
with open(name+'.wav', 'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav'
    ).get_result()
out_file = open(name+".json", "w")
json.dump(speech_recognition_results,out_file, indent = 6)
fh = open(name+".txt", "w+")
res_list = speech_recognition_results['results']
for results in res_list:
    print(results['alternatives'][0]['transcript'])
    fh.write(results['alternatives'][0]['transcript']+"\n")
fh.close()