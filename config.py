import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "postgres://pcnmttlwrgfoot:NrjpptFdJyAl1NgQAN7iatybfW@ec2-54-225-223-40.compute-1.amazonaws.com:5432/d13hrgrra1vfjc"

WTF_CSRF_ENABLED = True
SECRET_KEY = 'walczyk'