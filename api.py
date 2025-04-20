from fastapi import APIRouter
from pydantic import BaseModel
from models import load_model_and_encoder, predict_category
from utils import mask_pii, preprocess_email

# Initialize API Router
router = APIRouter()

# Load Model and Label Encoder once
model, label_encoder, sentence_model = load_model_and_encoder()

# Request Body
class EmailRequest(BaseModel):
    email_body: str

@router.post("/predict")
def predict_email(request: EmailRequest):
    email_body = request.email_body
    
    # Step 1: Mask PII
    masked_email, masked_entities = mask_pii(email_body)
    
    # Step 2: Preprocessing
    processed_email = preprocess_email(masked_email)
    
    # Step 3: Predict
    category = predict_category(processed_email, model, label_encoder, sentence_model)
    
    # Step 4: Return formatted response
    return {
        "input_email_body": email_body,
        "list_of_masked_entities": masked_entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
