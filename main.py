import os
from flask import Flask, render_template, request, redirect
from data import db_session
from data import tovar

app = Flask(__name__)

@app.route('/')
@app.route('/about')
def about():
    return render_template("site.html")


@app.route('/shop', methods=['POST', 'GET'])
def shop():
    db_session.global_init("db/shop.sqlite")
    session = db_session.create_session()
    object = session.query(tovar.Tovar)
    session.commit()
    if request.method == 'GET':
        return render_template("site-tovar.html", obj=object, selected=[], flag=0, flag2=1)
    elif request.method == 'POST':
        x = 0
        list = []
        for i in object:
            x += 1
            y = str(x)
            if request.form.get(y) != None:
                list.append(i)
                print(i.Name)
        fl=1
        if request.form.get('name') != None:
            print("Имя: "+request.form['name'])
            print("Email: "+request.form['email'])
            print("Телефон: "+request.form['telefon'])
            fl=0

        return render_template("site-tovar.html", obj=object, selected=list, flag=fl, flag2=fl)


@app.route('/letter', methods=['POST', 'GET'])
def letter():
    if request.method == 'GET':
        return render_template("site-letter.html")
    elif request.method == 'POST':
        print("Телефон: "+request.form['telefon'])
        print("Имя: "+request.form['name'])
        print("Заявка: "+request.form['text'])
        return redirect("/#send")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
