from flask import Flask, request
import Math

limit = 10

data = [
        {"name": "らーめん飛粋", "price": 1000, herf="/らーめん 飛粋.html"}]

app = Flask(__name__)

@app.route('/')
def index():
    page_s = request.args.get('page', '0')
    page = int(page_s)

    index = page * limit

    s = '<div>'
    for i in data[index : index+limit]:
        s += '<div class="item">'
        s += ' 品名 : ' + i['name'] + '<br>'
        s += ' 値段 : ' + str(i['price']) + '円'
        s += '</div>'
    s += '</div>' 

    s += make_pager(page, len(data), limit)
    return '''
    <html><meta charset="utf-8">
    <meta name="viewport"
        content="width=device-width, initial-scale=1">
    <link rel</html>