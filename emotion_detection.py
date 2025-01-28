import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL and headers for the Watson NLP Emotion Detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create the input JSON
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    # Make the POST request
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        # Parse the response JSON
        response_data = response.json()
        # Extract emotions and their scores
        emotions = response_data.get('emotion_predictions', {})
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
        
        # Determine the dominant emotion
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Format the output dictionary
        output = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
        return output
    else:
        # Handle errors
        return {"error": f"Error: {response.status_code}, {response.text}"}
