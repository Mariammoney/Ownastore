from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed

from wtforms import(
    StringField,
    PasswordField,
    DecimalField,
    TextAreaField,
    SubmitField,
    IntegerField,
    BooleanField,
    FileField
    
)

from wtforms.validators import(
    DataRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
    Optional
)
     



class SignUp(FlaskForm):
     name = StringField(
         "Name",
         validators=[
             DataRequired(),
         ]
     )
     
     
     email = StringField(
            "Email",
            validators=[
                DataRequired(),
            ]
         )
     
     password = PasswordField(
                " enter password",
                validators=[
                 DataRequired(),
            ]
        )
     
     confirm_password = PasswordField(
            "confirm password",
                     validators=[
                      DataRequired(),
                      EqualTo("password", message="passwords must match")
                 ]
             )
     submit = SubmitField("Create Account")
     
    
class Login(FlaskForm):
      
     email = StringField(
                  "Email",
                  validators=[
                      DataRequired(),
                  ]
               )
           
     password = PasswordField(
                      " enter password",
                      validators=[
                       DataRequired(),
                  ]
              )   
     
     submit = SubmitField("Login")
     
     
     
class ProductForm(FlaskForm):
    
    name = StringField(
        "Product Name",
        validators=[
            DataRequired(),
            Length(min=2, max=200)
            
        ]
    )


    description = TextAreaField(
        "Description",
        validators=[
            Optional()
        ]
    )

    price = DecimalField(
        "Price",
        validators=[
            DataRequired(),
            NumberRange(min=0)
            
        ],
        places=2
        
    )

    stock = IntegerField(
        "Stock",
        validators=[
            DataRequired(),
            NumberRange(min=0)
            
        ]
    )

    image = FileField(
        "Image URL",
        validators=[
            Optional(),
            FileAllowed(
                ["jpg", "jpeg", "png", "webp"],
                "Images only!"
            )
            
        ]
    )

    category = StringField(
        "Category",
        validators=[
            Optional(),
            Length(max=100)
            
        ]
    )

    is_active = BooleanField(
        "Active",
        default=True
    )

    submit = SubmitField("Save Product")