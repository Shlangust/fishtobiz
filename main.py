from flask import Flask, render_template, request
app = Flask(__name__)
lnk = ''

# goods = {
#         "Лосось":{"pict":"static/salmon.png",
#                   "goods":[{"name":"хребет лосося", "article":1,"price_item":999,"price_kilo":229,"desription":"Sample", "count": 0},
#                           {"name":"брюшко лосося", "article":2,"price":859,"price_kilo":200,"desription":"Sample", "count": 0}]
#                   },
#         "Форель": {"pict":"static/forel.png",
#                   "goods":[{"name": "хребет форели", "article":3, "price": 199,"price_kilo":19, "desription": "Хребет форели", "count": 0},
#                            {"name":"брюшко форели", "article":4,"price":259,"price_kilo":49,"desription":"брюшко форели", "count": 0}]
# }
# }

goods = {
    "Лосось": {
        "pict": "static/salmon.png",
        "goods": {
            "хребет лосося": {"article": 1, "name": "хребет лосося", "price": 999, "price_item": 229, "description": "Sample", "count": 0},
            "брюшко лосося": {"article": 2, "name": "брюшко лосося", "price": 859, "price_item": 200, "description": "Sample", "count": 0}
        }
    },
    "Форель": {
        "pict": "static/forel.png",
        "goods": {
            "хребет форели": {"article": 3, "name": "хребет форели", "price": 199, "price_item": 19, "description": "Хребет форели", "count": 0},
            "брюшко форели": {"article": 4, "name": "брюшко форели", "price": 259, "price_item": 49, "description": "брюшко форели", "count": 0}
        }
    }
}

cart = []
@app.route("/")
def index():
    return render_template("index.html", is_home=True,goods=goods)

@app.route('/documentation')
def documentation():
    return render_template("documentation.html")

@app.route('/none')
def none():
    return 'In work'

@app.route('/adm')
def adm():
    return render_template("adm.html")



@app.route('/category_<category_name>')
def category(category_name):
    return render_template("category.html",is_cat=True,category_name=category_name,categorise=goods[category_name]["goods"],is_from=True)

@app.route('/category')
def category_vergin():
    for i in goods:
        print(goods[i]['goods'])
    return render_template("category.html",is_cat=True,goods=goods)


@app.route('/product_<product_name>')
def product(product_name):

    category_name = request.args.get('category_name')
    return render_template("product.html" ,is_cat=True,product_info=goods[category_name]["goods"][product_name],goods=goods)

@app.route('/cart')
def cart():
    
    return render_template("cart.html")

@app.route('/test')
def fdf():
    return render_template("/test.html")

if __name__ == "__main__":
    app.run(debug=True)