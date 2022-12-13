from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mg_diop:weuthie@localhost/front'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Alerte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    motif = db.Column(db.String(255),nullable=False)
    plateau = db.Column(db.String(255),nullable = False)
    jour = db.Column(db.Integer)
    mois = db.Column(db.Integer)
    annee = db.Column(db.Integer)
    heure = db.Column(db.Integer)
    etat = db.Column(db.Integer,default=-1)

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
        new_alerte = Alerte(id= 1,motif="test",plateau="1314",jour=2,mois=12,annee=2022,heure=10)
        new_alerte_1 = Alerte(id= 2,motif="test_2",plateau="141",jour=2,mois=12,annee=2022,heure=10)
        addRows(new_alerte)
        addRows(new_alerte_1)
        commit()



