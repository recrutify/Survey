# -*- coding: utf-8 -*-
from app import db

class Typ_osobowosci(db.Model):
	__tablename__ = 'typy_osobowosci'

	id_typu_osobowosci = db.Column('id_typu_osobowosci', db.Integer, primary_key = True)
	opis = db.Column('opis', db.String())

	def __repr__(self):
		return '<Typ_osobowosci %d>' % (self.id_typu_osobowosci)

class Grupa_wiekowa(db.Model):
	__tablename__ = 'grupy_wiekowe'

	id_grupy_wiekowej = db.Column('id_grupy_wiekowej', db.Integer, primary_key = True)
	przedzial = db.Column('przedzial', db.String())

	def __repr__(self):
		return '<Grupa_wiekowa %d>' %(self.id_grupy_wiekowej)

class Pytanie(db.Model):
	__tablename__ = 'pytania'

	id_pytania = db.Column('id_pytania', db.Integer, primary_key = True)
	tresc = db.Column('tresc', db.String())
	id_typu = db.Column('id_typu', db.Integer, db.ForeignKey(Typ_osobowosci.id_typu_osobowosci))
	def __repr__(self):
		return '<Pytanie %d>' %(self.id_pytania)

class Zawod(db.Model):
	__tablename__ = 'zawody'

	id_zawodu = db.Column('id_zawodu', db.Integer, primary_key = True)
	opis = db.Column('opis', db.String())
	def __repr__(self):
		return '<Zawod %d>' %(self.id_zawodu)


class Odpowiedz(db.Model):
	__tablename__ = 'odpowiedzi'

	nr_pytania = db.Column('nr_pytania', db.Integer, db.ForeignKey(Pytanie.id_pytania))
	tak = db.Column('tak', db.Integer)
	nie = db.Column('nie', db.Integer)
	gr_wiekowa = db.Column('gr_wiekowa', db.Integer, db.ForeignKey(Grupa_wiekowa.id_grupy_wiekowej)) 
	id_zawodu = db.Column('id_zawodu', db.Integer, db.ForeignKey(Zawod.id_zawodu))
	id_odpowiedzi = db.Column('id_odpowiedzi', db.Integer, primary_key = True, autoincrement = True)
	

	def __repr__(self):
		return '<Odpowiedz %d>' % (self.id_odpowiedzi)