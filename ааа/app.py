from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import data

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('index.html', products=data.products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in data.products if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return redirect(url_for('index'))

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    product = next((p for p in data.products if p['id'] == product_id), None)
    if product:
        cart_item = next((item for item in session['cart'] if item['id'] == product_id), None)
        if cart_item:
            cart_item['quantity'] += 1
        else:
            product_copy = product.copy()
            product_copy['quantity'] = 1
            session['cart'].append(product_copy)
        session.modified = True
    
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item['id'] != product_id]
        session.modified = True
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/update_cart', methods=['POST'])
def update_cart():
    if 'cart' in session:
        product_id = int(request.form['product_id'])
        quantity = int(request.form['quantity'])
        
        for item in session['cart']:
            if item['id'] == product_id:
                item['quantity'] = quantity
                break
        session.modified = True
    
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)