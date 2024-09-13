from flask import *
from flask_sqlalchemy import*


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Password.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Password(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    webname=db.Column(db.String(100), nullable=False)
    username=db.Column(db.String(100), nullable=False)
    userpass=db.Column(db.String(100) ,nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno}- {self.username} - {self.userpass}"

with app.app_context():
    db.create_all()


@app.route("/", methods=['POST','GET'])
def hello_world():
    if request.method=='POST':
        webname=request.form['webname']
        username=request.form['username']
        userpass=request.form['pass']
        userinput=Password(webname=webname,username=username,userpass=userpass)
        db.session.add(userinput)
        db.session.commit()
    alluserinput=Password.query.all()
    print(alluserinput)
    return render_template('index.html',alluserinput=alluserinput)

@app.route("/delete/<int:sno>")
def name(sno):
    dinput=Password.query.filter_by(sno=sno).first()
    db.session.delete(dinput)
    db.session.commit()
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True,port=3000)