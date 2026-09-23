# import cloudinary
# from cloudinary import uploader

# from flask import current_app
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def configure_cloudinary():
#     cloudinary.config(
#         # cloud_name="anar2jmi",

#         # api_key="433638385394926",
        
#         # api_secret="9vuKLGnAvOK21OZtIiT3-2ACYbY",
        
#         # secure=True
        
#         cloud_name="dq1gwv2y8",
        
#         api_key="111157147187142",
                
#         api_secret="BY2-hXpJUr80KIVEEkPq_Kb-GiY",
                
#         secure=True
    
#     )
    
    
# def upload_image(file):
#     try:
#         result = uploader.upload(
#             file,
#             folder="flask_ecommerce/products"
#         )

#         return result["secure_url"]

#     except Exception as e:
#         print(f"Cloudinary upload failed: {e}")
#         return None
    
    
import cloudinary
from cloudinary import uploader

from flask import current_app
import os
from dotenv import load_dotenv

load_dotenv()

def configure_cloudinary():
    cloudinary.config(
        # cloud_name=os.getenv["CLOUDINARY_CLOUD_NAME"],
        cloud_name="dqlgwv2y8",
        
        # api_key=os.getenv["CLOUDINARY_API_KEY"],
        api_key="111157147187142",
        
        # api_secret=os.getenv["CLOUDINARY_API_SECRET"],
        api_secret="BY2_hXpJUr8OKIVEEkPq_Kb-GiY",
        
        secure=True
    )


def upload_image(file):
    configure_cloudinary()

    result = cloudinary.uploader.upload(
        file,
        folder="flask_ecommerce/products"
    )

    return result["secure_url"]