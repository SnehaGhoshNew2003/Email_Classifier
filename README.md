# Email Classifier

This project is an **Email Classifier** that classifies emails into predefined categories and detects and masks Personally Identifiable Information (PII) within email content. It uses **machine learning** and **text processing** techniques to extract useful insights and protect sensitive information.

## Features
- **PII Masking:** Detects and masks personal information such as email addresses, phone numbers, and names.
- **Email Classification:** Classifies the email into categories like "Change", "Inquiry", and more.
- **Text Processing:** Preprocesses raw email content to extract insights and classify them accurately.
- **Category Prediction:** Uses machine learning models to predict the category of the email.

## Technologies Used
- **FastAPI**: API framework to create the web service.
- **scikit-learn**: For training and using machine learning models for email classification.
- **sentence-transformers**: For text embeddings to process and classify the email text.
- **pydantic**: Data validation for API input and output.
- **pickle**: For serializing models and encoders.

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/email-classifier.git
cd email-classifier
```
### Step 2: Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Running the API Server
2. To start the FastAPI server locally, run the following command:
```bash
uvicorn app_name:app --reload
```
This will start the API server at http://localhost:8000.

## Example Usage

- Input an email body.
  ```json
  {
  "input_email_body": "string containing the email"
  }
  ```

- The app will classify the email and mask PII information (e.g., emails, phone numbers).
- The masked email and its category will be shown.
  ```json
  {
  "input_email_body": "string containing the email",
  "list_of_masked_entities": [
    {
      "position": [start_index, end_index],
      "classification": "entity_type",
      "entity": "original_entity_value"
    }
  ],
  "masked_email": "string containing the masked email",
  "category_of_the_email": "string containing the class"
  }
  ```
## Requirements file
```bash
pip install -r requirements.txt
```
```txt
fastapi
uvicorn
scikit-learn
sentence-transformers
numpy
pydantic
```

## Contributing

Feel free to submit issues or pull requests to improve the project. Contributions are welcome, and any improvements to the classifier model or masking accuracy are highly appreciated.
