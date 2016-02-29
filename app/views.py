# -*- coding: utf-8 -*-
from app import app, db
from flask import session, render_template, request, redirect, url_for
from .forms import SurveyForm, BasicInfoForm, QuestionForm
from .models import Pytanie, Odpowiedz
from random import *
from wtforms import RadioField
import os

questions = []
profession1 = 0
age1 = 0
i = 0
def setQuestions():
	global questions
	pom = 0
	print("w setQuestions")
	for k in range (0,8):
		if(k % 2 == 0):
			pom = pom +1
		question = Pytanie.query.filter_by(id_typu = pom)
		newQuestion = question[randrange(0,13,1)]
		while (checkIfValueInList(newQuestion)):
			newQuestion = question[randrange(0,13,1)]
		if len(questions) >= (k+1):
			questions[k] = newQuestion;
		else:
			questions.append(newQuestion)
	session['quest'] = []
	session['quest'] = questions
def checkIfValueInList(question):
	global questions
	if (question in questions):
		return True
	else:
		return False
@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
	global questions, profession1, age1, i
	form = SurveyForm()
	if request.method == 'POST':
		questions = []
		profession1 = 0
		age1 = 0
		i = 0
		return redirect(url_for('basicInfo'))
	elif request.method == 'GET':
		platform = request.user_agent.platform
		platformTable = ["android","iphone","ipad"] 
		if (request.user_agent.platform in platformTable):
			session['mobile'] = 't'
		else:
			session['mobile'] = 'n'
		if (session['mobile'] == 'n'):
			return render_template('index.html', form = form)
		else:
			return render_template('indexm.html', form = form)

@app.route('/basicInfo', methods=['GET','POST'])
def basicInfo():
	form = BasicInfoForm()
	global profession, age, i
	if request.method == 'POST':
		#setQuestions()
		p = form.profession.data +1
		a = form.age.data + 1
		i = 0
		session['prof'] = p
		session['ag'] = a
		return redirect(url_for('question'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('basicInfo.html', form = form)
		else:
			return render_template('basicInfom.html', form = form)
@app.route('/')
@app.route('/question', methods=['GET','POST'])
def question():
	form = QuestionForm()
	question = Pytanie.query.filter_by(id_typu = 1)
	newQuestion = question[randrange(0,7,1)]
	question_id = newQuestion.id_pytania
	prof = session['prof']
	ag = session['ag']
	if request.method == 'POST':
		
		answer = Odpowiedz.query.filter_by(id_zawodu = prof).filter_by(gr_wiekowa = ag).filter_by(nr_pytania = question_id).first()
		if 'yes' in request.form:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 1, nie = 0, id_zawodu = prof, gr_wiekowa = ag)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.tak += 1
				db.session.commit()
		else:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 0, nie = 1, id_zawodu = prof, gr_wiekowa = ag)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.nie += 1
				db.session.commit()
		return redirect(url_for('question2'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('question.html', form = form, question = newQuestion.tresc)
		else:
			return render_template('questionm.html', form = form, question = newQuestion.tresc)
@app.route('/question2', methods=['GET','POST'])
def question2():
	form = QuestionForm()
	question = Pytanie.query.filter_by(id_typu = 1)
	newQuestion = question[randrange(7,13,1)]
	question_id = newQuestion.id_pytania
	profession = session['prof']
	age = session['ag']
	if request.method == 'POST':
		
		answer = Odpowiedz.query.filter_by(id_zawodu = profession).filter_by(gr_wiekowa = age).filter_by(nr_pytania = question_id).first()
		if 'yes' in request.form:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 1, nie = 0, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.tak += 1
				db.session.commit()
		else:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 0, nie = 1, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.nie += 1
				db.session.commit()
		return redirect(url_for('question3'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('question2.html', form = form, question = newQuestion.tresc)
		else:
			return render_template('question2m.html', form = form, question = newQuestion.tresc)
@app.route('/question3', methods=['GET','POST'])
def question3():
	form = QuestionForm()
	question = Pytanie.query.filter_by(id_typu = 2)
	newQuestion = question[randrange(0,7,1)]
	question_id = newQuestion.id_pytania
	profession = session['prof']
	age = session['ag']
	if request.method == 'POST':
		
		answer = Odpowiedz.query.filter_by(id_zawodu = profession).filter_by(gr_wiekowa = age).filter_by(nr_pytania = question_id).first()
		if 'yes' in request.form:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 1, nie = 0, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.tak += 1
				db.session.commit()
		else:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 0, nie = 1, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.nie += 1
				db.session.commit()
		return redirect(url_for('question4'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('question3.html', form = form, question = newQuestion.tresc)
		else:
			return render_template('question3m.html', form = form, question = newQuestion.tresc)
@app.route('/question4', methods=['GET','POST'])
def question4():
	form = QuestionForm()
	question = Pytanie.query.filter_by(id_typu = 2)
	newQuestion = question[randrange(7,13,1)]
	question_id = newQuestion.id_pytania
	profession = session['prof']
	age = session['ag']
	if request.method == 'POST':
		
		answer = Odpowiedz.query.filter_by(id_zawodu = profession).filter_by(gr_wiekowa = age).filter_by(nr_pytania = question_id).first()
		if 'yes' in request.form:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 1, nie = 0, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.tak += 1
				db.session.commit()
		else:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 0, nie = 1, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.nie += 1
				db.session.commit()
		return redirect(url_for('question5'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('question4.html', form = form, question = newQuestion.tresc)
		else:
			return render_template('question4m.html', form = form, question = newQuestion.tresc)
@app.route('/question5', methods=['GET','POST'])
def question5():
	form = QuestionForm()
	question = Pytanie.query.filter_by(id_typu = 3)
	newQuestion = question[randrange(0,7,1)]
	question_id = newQuestion.id_pytania
	profession = session['prof']
	age = session['ag']
	if request.method == 'POST':
		
		answer = Odpowiedz.query.filter_by(id_zawodu = profession).filter_by(gr_wiekowa = age).filter_by(nr_pytania = question_id).first()
		if 'yes' in request.form:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 1, nie = 0, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.tak += 1
				db.session.commit()
		else:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 0, nie = 1, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.nie += 1
				db.session.commit()
		return redirect(url_for('question6'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('question5.html', form = form, question = newQuestion.tresc)
		else:
			return render_template('question5m.html', form = form, question = newQuestion.tresc)
@app.route('/question6', methods=['GET','POST'])
def question6():
	form = QuestionForm()
	question = Pytanie.query.filter_by(id_typu = 3)
	newQuestion = question[randrange(7,13,1)]
	question_id = newQuestion.id_pytania
	profession = session['prof']
	age = session['ag']
	if request.method == 'POST':
		
		answer = Odpowiedz.query.filter_by(id_zawodu = profession).filter_by(gr_wiekowa = age).filter_by(nr_pytania = question_id).first()
		if 'yes' in request.form:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 1, nie = 0, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.tak += 1
				db.session.commit()
		else:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 0, nie = 1, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.nie += 1
				db.session.commit()
		return redirect(url_for('question7'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('question6.html', form = form, question = newQuestion.tresc)	
		else:
			return render_template('question6m.html', form = form, question = newQuestion.tresc)		
@app.route('/question7', methods=['GET','POST'])
def question7():
	form = QuestionForm()
	question = Pytanie.query.filter_by(id_typu = 4)
	newQuestion = question[randrange(0,7,1)]
	question_id = newQuestion.id_pytania
	profession = session['prof']
	age = session['ag']
	if request.method == 'POST':
		
		answer = Odpowiedz.query.filter_by(id_zawodu = profession).filter_by(gr_wiekowa = age).filter_by(nr_pytania = question_id).first()
		if 'yes' in request.form:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 1, nie = 0, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.tak += 1
				db.session.commit()
		else:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 0, nie = 1, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.nie += 1
				db.session.commit()
		return redirect(url_for('question8'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('question7.html', form = form, question = newQuestion.tresc)	
		else:
			return render_template('question7m.html', form = form, question = newQuestion.tresc)		
@app.route('/question8', methods=['GET','POST'])
def question8():
	form = QuestionForm()
	question = Pytanie.query.filter_by(id_typu = 4)
	newQuestion = question[randrange(7,13,1)]
	question_id = newQuestion.id_pytania
	profession = session['prof']
	age = session['ag']
	if request.method == 'POST':
		
		answer = Odpowiedz.query.filter_by(id_zawodu = profession).filter_by(gr_wiekowa = age).filter_by(nr_pytania = question_id).first()
		if 'yes' in request.form:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 1, nie = 0, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.tak += 1
				db.session.commit()
		else:
			if(answer is None):
				answer = Odpowiedz(nr_pytania = question_id, tak = 0, nie = 1, id_zawodu = profession, gr_wiekowa = age)
				db.session.add(answer)
				db.session.commit()
			else:
				answer.nie += 1
				db.session.commit()
		return redirect(url_for('end'))
	elif request.method == 'GET':
		if (session['mobile'] == 'n'):
			return render_template('question8.html', form = form, question = newQuestion.tresc)
		else:
			return render_template('question8m.html', form = form, question = newQuestion.tresc)
@app.route('/')
@app.route('/end', methods=['GET'])
def end():
	if (session['mobile'] == 'n'):
		return render_template('end.html')
	else:
		return render_template('endm.html')