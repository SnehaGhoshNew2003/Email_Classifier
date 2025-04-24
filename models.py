import joblib
from sentence_transformers import SentenceTransformer

def load_model_and_encoder():
    model = joblib.load('email_classifier_model.joblib')
    label_encoder = joblib.load('label_encoder.joblib')
    sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
    return model, label_encoder, sentence_model

def predict_category(processed_email, model, label_encoder, sentence_model):
    embedding = sentence_model.encode([processed_email])
    prediction = model.predict(embedding)
    category = label_encoder.inverse_transform(prediction)[0]
    return category
