from flask import Flask, redirect ,render_template , request, session, url_for, flash  
from createdb import *  #Alerte,addRows,commit,db,app

app = Flask(__name__)
app.config['SECRET_KEY'] = 'groupe5'  #'vigi-predictive'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:groupe5@localhost/flask' #'postgresql://mg_diop:weuthie@localhost/front'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email') 
        admin = Admin.query.filter_by(login = email).first() 
        if admin is None:
            session['login'] = email
            return redirect('users')
        else:
            # session['login'] = email
            return redirect(url_for('admin'))

    return render_template('accueil.html')



@app.route('/admin', methods=["GET", "POST"])
def admin():
    users = db.session.query(Users).filter(
        Users.archive == -1
        ).all()
    nbuser =len(users)
    if request.method == "POST":
        addUser = Users(
            prenom =request.form["prenom"],
            nom =request.form["nom"],
            login =request.form["email"],
            password =request.form["password"]
        )
        db.session.add(addUser)
        db.session.commit()
        return redirect(url_for("admin"))

    return render_template('admin.html', users = users, nbuser = nbuser)



@app.route('/users/')
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
        return render_template('users.html',nbuser=nbuser,users=users , 
        total_rejeter=total_rejeter,
        total_accepter=total_accepter,
        total_alerte=total_alerte)
    

    

@app.route('/accepter/<int:id>', methods=["POST","GET"])
def accepter(id):
    user =  Alerte.query.get_or_404(id)
    if request.method == "POST":
        user.etat = 1
        commit()
    return redirect('/users')

@app.route('/rejeter/<int:id>', methods=["POST","GET"])
def rejeter(id):
    user =  Alerte.query.get_or_404(id)
    if request.method == "POST":
        user.etat = 0
        commit()
    return redirect('/users')


db.init_app(app)
app.run(debug=True, port=5001)