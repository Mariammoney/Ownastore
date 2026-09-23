import os
from dotenv import load_dotenv

load_dotenv

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///ecommerce.db"
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args":{
            "timeout": 30
        }
    }
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
    
    PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")
    PAYSTACK_PUBLIC_KEY = os.getenv("PAYSTACK_PUBLIC_KEY")
    
    PAYSTACK_BASE_URL = "https://api.paystack.co"
        