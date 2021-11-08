from flask import render_template, request


from flask_login import login_required


from .import bp as shop


@shop.route('/view', methods=['GET'])  
@login_required
def view():
    return render_template('view.html.j2') 

@shop.route('/cart', methods=['GET'])  
@login_required  
def cart():
    return render_template('cart.html.j2')




