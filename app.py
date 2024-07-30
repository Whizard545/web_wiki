from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, info_data

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
db.init_app(app)

@app.route('/')
def index():
    info = info_data.query.all()
    return render_template('index.html', info=info)

@app.route('/add', methods=['GET', 'POST'])
def add_info():
    if request.method == 'POST':
        wmname = request.form['wmname']
        company_name = request.form['company_name']
        status = request.form['status']
        address = request.form['address']
        host = request.form['host']
        info= info_data(wmname=wmname, company_name=company_name, status=status, address=address, host=host)
        db.session.add(info)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_info(id):
    info = info_data.query.get_or_404(id)
    if request.method == 'POST':
        info.wmname = request.form['wmname']
        info.company_name = request.form['company_name']
        info.status = request.form['status']
        info.address = request.form['address']
        info.host = request.form['host']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', info=info)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_info(id):
    info = info_data.query.get_or_404(id)
    db.session.delete(info)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='10.10.77.27', port=8000, debug=False)
