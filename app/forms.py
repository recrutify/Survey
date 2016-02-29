# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import RadioField, BooleanField, StringField, SelectField, SubmitField
from app import db
from .models import Pytanie

class SurveyForm(Form):

	submit = SubmitField("Do boju!")

class BasicInfoForm(Form):
	profession = SelectField("Profesja: ", coerce=int, choices=[(0,"Programista"), (1,"Tester"), (2,"Analityk/Projektant"),
		(3,"Wdrozeniowiec"), (4, "Sieciowiec"), (5,"PM"), (6,"Technik"), (7, "Helpdesk")], default=0)
	age = SelectField("Wiek: ", coerce=int, choices=[(0,"18-25 lat"),(1,"26-30 lat"),(2,"31-35 lat"),
	 (3,"36-45 lat"),(4,"> 46 lat")], default=0)

	submit = SubmitField("Dalej!")


class QuestionForm(Form):
	
	#question = RadioField('pytanie', choices = [('tak', 'Tak'), ('nie', 'Nie')])
	yes = SubmitField("Tak")
	no = SubmitField("Nie")




