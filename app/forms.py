from wtforms import (SelectField, StringField, SubmitField, PasswordField, FileField , EmailField)
from wtforms.validators import InputRequired, Length, ValidationError, Optional
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from flask_wtf.file import (FileField, FileAllowed)
from app.models import User


class RegisterForm(FlaskForm):

    username = StringField(
        validators=[InputRequired(), Length(min=6, max=70)], 
        render_kw={"placeholder": "Username", "class": "form-control"}
    )
    password = PasswordField(
        validators=[InputRequired(), Length(min=7, max=20)], 
        render_kw={"placeholder": "Password", "class": "form-control"}
    )
    confirm_password = PasswordField(
        validators=[InputRequired(), Length(min=7, max=20)], 
        render_kw={"placeholder": "Confirm Password", "class": "form-control"}
    )
    email = EmailField(
        validators=[InputRequired(), Length(min=6, max=70)], 
        render_kw={"placeholder": "Email", "class": "form-control"}
    )

    submit = SubmitField("Register", render_kw={"class": "btn btn-primary form-control"})

    def validate_username(self, username):
        existing_user = User.query.filter_by(username=username.data).first()
        if existing_user:
            raise ValidationError("Verification Error : Username already exists , please chose another one.")
        
    def validate_password(self, password):
        if self.password.data != self.confirm_password.data:
            raise ValidationError("Verification Error : password must match its confirmation.")
    
    def validate_email(self , email):
        existing_user = User.query.filter_by(email=email.data).first()
        if existing_user:
            raise ValidationError("Verification Error : email already exists , please chose another one.")
        





class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired(), Length(min=4, max=70)], render_kw={
        "placeholder": "Email", "class": "form-control"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=7, max=20)], render_kw={"placeholder": "Password", "class": "form-control"})
    submit = SubmitField("Login", render_kw={
                         "class": "btn btn-primary form-control"})


class PostForm(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(
        min=4, max=70)], render_kw={"placeholder": "Title", "class": "form-control"})
    story = CKEditorField(validators=[InputRequired(), Length(
        min=4, max=5000)], render_kw={"placeholder": "Story"})
    category = SelectField(validators=[InputRequired()], render_kw={
                           "class": "form-control"})
    submit = SubmitField("Post", render_kw={
                         "class": "btn btn-primary form-control"})

class ReplyForm(FlaskForm):
    story = CKEditorField(validators=[InputRequired()])
    submit = SubmitField(label='Reply' , render_kw={'class' : 'form-control btn btn-primary'})


class EditForm(FlaskForm):
    edit_title = StringField(render_kw={"placeholder": "Title", 'class': 'form-control'})
    edit_story = CKEditorField()
    edit_category = SelectField(render_kw={'class': 'form-control'})
    edit_submit = SubmitField("Modify", render_kw={'class': 'btn btn-primary form-control'})


class ProfileForm(FlaskForm):
    username = StringField(render_kw={"placeholder": "Username", 'class': "form-control"})
    email = EmailField(render_kw={"placeholder": "Email", 'disabled': True  , 'class' : 'form-control'})
    profile_picture = FileField(
        'File', validators=[Optional() , FileAllowed(['jpg', 'png' , 'jpeg' , 'webp'])] ,
        render_kw={'class' : 'form-control' , 'accept' : 'image/x-png,image/jpeg,image/jpg,/image/webp'})
    
    about = CKEditorField()


    submit = SubmitField("Modifier" , render_kw={'class' : 'btn btn-primary'})

    

class CategoryForm(FlaskForm):
    title = StringField(render_kw={"placeholder": "Title", 'class': "form-control"} , 
                        validators=[InputRequired('Please Provide A Title Before Submiting')])
    submit = SubmitField(render_kw={"class" : "btn btn-primary"})
