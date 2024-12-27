import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=json_data)
    response_json = response.json()
    
    # Assuming the response JSON structure includes an 'emotions' key with sub-keys for each emotion and their scores
    emotions = response_json.get('emotions', {})
    
    # Extract scores
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Find dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Format output
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    return result

if __name__ == "__main__":
    sample_text = "I am so happy I am doing this."
    result = emotion_detector(sample_text)
    print(result)
