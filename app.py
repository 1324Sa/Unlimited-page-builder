from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pages_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class WebPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    pages = WebPage.query.all()
    return render_template('dashboard.html', pages=pages)

@app.route('/create', methods=['POST'])
def create():
    slug = request.form.get('slug').replace(" ", "-") # تحويل المسافات لشرطات
    new_page = WebPage(
        slug=slug,
        title=request.form.get('title'),
        content=request.form.get('content')
    )
    db.session.add(new_page)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/site/<slug>')
def view_site(slug):
    page = WebPage.query.filter_by(slug=slug).first_or_404()
    return render_template('page_template.html', page=page)

@app.route('/delete/<int:id>')
def delete(id):
    page = WebPage.query.get(id)
    db.session.delete(page)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)