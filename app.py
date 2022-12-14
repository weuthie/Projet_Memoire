from flask import Flask, redirect ,render_template , request, session, url_for, flash  
from createdb import Alerte,addRows,commit,db,app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'groupe5'  #'vigi-predictive'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:groupe5@localhost/flask' #'postgresql://mg_diop:weuthie@localhost/front'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def index():
        users = db.session.query(Alerte).filter(
        Alerte.etat == -1
        ).all()
        total_alerte = len(Alerte.query.all())
        total_accepter = len( db.session.query(Alerte).filter(
        Alerte.etat == 1).all())
        total_rejeter = len( db.session.query(Alerte).filter(
        Alerte.etat == 0).all())

        nbuser =len(users)
        print(nbuser)
        print(total_alerte,"total")
        print(total_accepter,"total accpter")
        print(total_rejeter,"total rejeter")
        # data = {"id":user.id,
        # "motif":user.motif,
        # "plateau":user.plateau,
        # "jour":user.jour,
        # "mois":user.mois,
        # "annee":user.annee,
        # "heure":user.heure,
        # "etat":user.etat}
        return render_template('index_admin.html',nbuser=nbuser,users=users , 
        total_rejeter=total_rejeter,
        total_accepter=total_accepter,
        total_alerte=total_alerte)
    

    

@app.route('/accepter/<int:id>', methods=["POST","GET"])
def accepter(id):
    user =  Alerte.query.get_or_404(id)
    if request.method == "POST":
        user.etat = 1
        commit()
    return redirect('/')

@app.route('/rejeter/<int:id>', methods=["POST","GET"])
def rejeter(id):
    user =  Alerte.query.get_or_404(id)
    if request.method == "POST":
        user.etat = 0
        commit()
    return redirect('/')


db.init_app(app)
app.run(debug=True)