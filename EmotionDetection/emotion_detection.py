import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named emotion_detector that takes a string input (text_to_analyze)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    json_dict = json.loads(response.text)['emotionPredictions'][0]['emotion'] # convert the response text into a dictionary
    
    if response.status_code == 200:
        # create dictionary for store specific values from JSON response
        formatted_response =  {
            'anger': json_dict['anger'],
            'disgust': json_dict['disgust'],
            'fear': json_dict['fear'],
            'joy': json_dict['joy'],
            'sadness': json_dict['sadness']
        }

        # get the dominant emotion
        dominant_emotion = 'anger'
        highest_score = json_dict['anger']
        for key in formatted_response:
            score = formatted_response[key]
            if score > highest_score:
                dominant_emotion = key
                highest_score = score

        # store dominant emotion in formatted response
        formatted_response['dominant_emotion'] = dominant_emotion

        return formatted_response  # Return formatted response
    else:
        return { 
            'anger': None, 
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }