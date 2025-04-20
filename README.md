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
