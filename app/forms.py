from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired
from datetime import datetime

app.config["SECRET_KEY"] = "mlody"

class AuthorForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    origin = StringField("origin", validators=[DataRequired()])

class BookForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    series = StringField("series")
    pages = IntegerField("pages", validators=[DataRequired()])
    author_id = StringField("title", validators=[DataRequired()])

class BorrowForm(FlaskForm):
    book_id = StringField("book_id", validators=[DataRequired()])
    status = StringField("series", validators=[DataRequired()])
    date = DateField("date", validators=[DataRequired()], default=datetime.utcnow)