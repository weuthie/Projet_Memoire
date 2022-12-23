from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:groupe5@localhost/flask' #'postgresql://mg_diop:weuthie@localhost/front'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
db.init_app(app)

class Alerte(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    motif = db.Column(db.String(255),nullable=False)
    plateau = db.Column(db.String(255),nullable = False)
    jour = db.Column(db.Integer)
    mois = db.Column(db.Integer)
    annee = db.Column(db.Integer)
    heure = db.Column(db.Integer)
    comment = db.Column(db.String(255))
    etat = db.Column(db.Integer,default=-1)

class Users(db.Model):
    userid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nom = db.Column(db.String(15),nullable=False)
    prenom = db.Column(db.String(55),nullable = False)
    login = db.Column(db.String(255))
    password = db.Column(db.String(255),nullable = False)
    profil = db.Column(db.String(55),nullable = False,default="user")
    archive = db.Column(db.Integer,default=-1)

class Admin(db.Model):
    adminid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    login = db.Column(db.String(100),nullable=False,default="ousseynou@sa.com")
    motdepasse = db.Column(db.String(55),nullable = False,default="mansour")
    profil = db.Column(db.String(55),nullable = False,default="admin")
    archive = db.Column(db.Integer,default=-1)


def commit():
    return db.session.commit()

def addRows(dataForTable):
    try:
        db.session.add(dataForTable)
        
    except:
        db.session.rollback()
        return "erreur"

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        new_alerte = Alerte(motif="test",plateau="1314",jour=2,mois=12,annee=2022,heure=10)
        new_alerte_1 = Alerte(motif="test_2",plateau="141",jour=2,mois=12,annee=2022,heure=10)
        new_ = Alerte(motif="om",plateau="1441",jour=5,mois=12,annee=2022,heure=11)
        addRows(new_alerte)
        addRows(new_alerte_1)
        addRows(new_)

        commit()



