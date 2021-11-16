from flask import render_template, request
from app.models import Item, Category


from flask_login import login_required


from .import bp as shop

@shop.route('/category3', methods=['GET'])  
@login_required
def category3():
    return render_template('category3.html.j2') 

@shop.route('/category2', methods=['GET'])  
@login_required
def category2():
    return render_template('category2.html.j2') 

@shop.route('/category', methods=['GET'])  
@login_required
def category():
    return render_template('category.html.j2') 

@shop.route('/success', methods=['GET'])  
@login_required
def success():
    return render_template('specific.html.j2') 

@shop.route('/view', methods=['GET'])  
@login_required
def view():
    return render_template('view.html.j2') 

@shop.route('/cart', methods=['GET'])  
@login_required  
def cart():
    return render_template('checkout.html.j2')


@shop.route('/checkout', methods=['GET'])
@login_required
def checkout():
    return render_template('checkout.html.j2')


@shop.route('/add_item', methods=['GET'])
def add_item():
    item_id = request.get('id')  
    item = Item.query.filter_by(id=item_id).first()
    item.add_item()
    return  render_template('cart.html.j2')


@shop.route('/remove_item',  methods=['GET'])
def remove_item():
    item_id = request.get('id')  
    item = Item.query.filter_by(id=item_id).first()
    item.remove_item()
    return  render_template('cart.html.j2')

@shop.route('/view_item',  methods=['GET'])
def view_item():
    item_id = request.get('id')  
    item = Item.query.filter_by(id=item_id).first()
    item.view_item()
    return  render_template('cart.html.j2')




