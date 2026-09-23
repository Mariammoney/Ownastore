# import uuid


# from flask import Blueprint, render_template, redirect, url_for, flash


# from extensions import db

# from models.product import Product
# from forms import ProductForm
# # from utils.decorators import product_required
# from utils.cloudinary import upload_image


# product = Blueprint("product", __name__)

# @product.route("/product/add", methods=["GET", "POST"])
# def add_product():

#     form = ProductForm()

#     if form.validate_on_submit():

#         image_url = None

#         if form.image.data:
#             image_url = upload_image(form.image.data)
#             # image_url = upload_image(file)

#         if not image_url:
#             return {"error": "Image upload failed"}, 500


#         slug = (
#             f"{form.name.data.lower().replace(' ', '-')}"
#             f"-{uuid.uuid4().hex[:8]}"
#         )

#         new_product = Product(
#             name=form.name.data,
#             slug=slug,
#             description=form.description.data,
#             price=form.price.data,
#             stock=form.stock.data,
#             category=form.category.data,
#             image_url=image_url
#         )

#         db.session.add(new_product)
#         db.session.commit()

#         flash(
#             "Product added successfully",
#             "success"
#         )

#         return redirect(url_for("products"))

#     return render_template(
#         "products/products.html",
#         form=form
#     ) 
    
# @product.route("/products")
# def get_all_products():
    
#     products = Product.query.order_by(
#         Product.created_at.desc()
#     ).all()
    
    
#     return render_template(
#         "products/products.html",
#         products=products
#     )
    
# @product.route("/product")
# def get_a_product():
    
#     product = Product.query.order_by(
#         Product.created_at.desc()
#     )
    
#     return render_template(
#         "products/aproduct.html",
#         products=product
#     )
    
    
# @product.route(
#     "/product/<int:product_id>/edit",
#     methods=["GET", "POST"]
# )
# def edit_product(product_id):
    
#     product = Product.query.get_or_404(product_id)
    
#     form = ProductForm(obj=product)
    
#     if form.validate_on_submit():
        
#         product.name = form.name.data
#         product.description = form.description.data
#         product.price = form.price.data
#         product.stock = form.stock.data
#         product.category = form.category.data
        
#         if form.image.data:
#             product.image_url = upload_image(
#                 form.image.data
#             )
            
#         db.session.commit()
        
#         flash(
#             "Product updated successfully",
#             "success"
#         )
        
#         return redirect(
#             url_for("product.get_all_products")
#         )
        
#     return render_template(
#         "products/edit_product.html",
#         form=form,
#         product=product
#     )
    
    
# @product.route(
#     "/product/<int:product_id>/delete",
#     methods=["POST"]
# )
# def delete_product(product_id):
    
#     product = Product.query.get_or_404(product_id)
    
#     db.session.delete(product)
#     db.session.commit()
    
#     flash(
#         "product deleted successfully",
#         "success"
#     )
    
#     return redirect(
#         url_for("product.products")
#     )
    









import uuid

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from extensions import db
from models.product import Product
from forms import ProductForm
from utils.cloudinary import upload_image
from flask_login import  login_required

product = Blueprint("product", __name__)




@product.route("/product/add", methods=["GET", "POST"])
# @product_required
# @login_required
def add_product():

    form = ProductForm()

    if form.validate_on_submit():

        image_url = None

        if form.image.data:
            image_url = upload_image(form.image.data)

        slug = (
            f"{form.name.data.lower().replace(' ', '-')}"
            f"-{uuid.uuid4().hex[:8]}"
        )

        product = Product(
            name=form.name.data,
            slug=slug,
            description=form.description.data,
            price=form.price.data,
            stock=form.stock.data,
            category=form.category.data,
            image_url=image_url
        )

        db.session.add(product)
        db.session.commit()

        flash(
            "Product added successfully.",
            "success"
        )

        return redirect(
            url_for("product.get_all_products")
        )

    return render_template(
        "products/add_products.html",
        form=form
    )



@product.route("/products")
# @product_required
def get_all_products():

    products = Product.query.order_by(
        Product.created_at.desc()
    ).all()

    return render_template(
        "products/products.html",
        products=products
    )


@product.route(
    "/products/<int:product_id>/edit",
    methods=["GET", "POST"]
)
def edit_product(product_id):

    product = Product.query.get_or_404(product_id)

    form = ProductForm(obj=product)

    if form.validate_on_submit():

        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.stock = form.stock.data
        product.category = form.category.data

        if form.image.data:
            product.image_url = upload_image(
                form.image.data
            )

        db.session.commit()

        flash(
            "Product updated successfully.",
            "success"
        )

        return redirect(
            url_for("product.products")
        )

    return render_template(
        "product/edit_product.html",
        form=form,
        product=product
    )

@product.route(
    "/products/<int:product_id>/delete",
    methods=["POST"]
)
# @product_required
def delete_product(product_id):

    product = Product.query.get_or_404(product_id)

    db.session.delete(product)
    db.session.commit()

    flash(
        "Product deleted successfully.",
        "success"
    )

    return redirect(
        url_for("product.products")
    )
    
    


@product.route("/product")
# @product_required
def get_a_product(product_id):

    product = Product.query.get_or_404(product_id)
  

    return render_template(
        "product/product_details.html",
        product=product
    )
