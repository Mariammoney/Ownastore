from extensions import db

class Product(db.Model):
    
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(200), nullable=False)
    
    slug = db.Column(db.String(200), unique=True, nullable=False)
    
    description = db.Column(db.Text, nullable=True)

    price = db.Column(db.Float, nullable=False)
    
    stock = db.Column(db.Integer, default=0, nullable=False)
    
    image_url = db.Column(db.String(500), nullable=False)
    
    category = db.Column(db.String(100), nullable=True)
    
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
        
    