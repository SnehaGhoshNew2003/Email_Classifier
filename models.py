import pickle
from sentence_transformers import SentenceTransformer

def load_model_and_encoder():
    with open('email_classifier_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
    return model, label_encoder, sentence_model

def predict_category(processed_email, model, label_encoder, sentence_model):
    embedding = sentence_model.encode([processed_email])
    prediction = model.predict(embedding)
    category = label_encoder.inverse_transform(prediction)[0]
    return category
