import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://skills.network'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    try:
        response = requests.post(url, json=myobj, headers=headers)
        if response.status_code == 400 or response.status_code == 500:
            return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        formatted_response = response.json()
        emotion_predictions = formatted_response['emotionPredictions']['emotion']
        emotions_dict = {
            'anger': emotion_predictions['anger'],
            'disgust': emotion_predictions['disgust'],
            'fear': emotion_predictions['fear'],
            'joy': emotion_predictions['joy'],
            'sadness': emotion_predictions['sadness']
        }
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)
        emotions_dict['dominant_emotion'] = dominant_emotion
        return emotions_dict
    except:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
