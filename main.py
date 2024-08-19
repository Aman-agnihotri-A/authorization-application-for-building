from flask import Flask , render_template, request , url_for , redirect
import DB
from Users import Users as user

app = Flask(__name__)



def printword(word):
    print(word)


@app.route('/postlogin.html',methods=["GET","POST"])
def insertVisitor():
    loginType="Visitor"
    if request.method=="POST":
        userid=request.form["userid"]
        firstname=request.form["firstname"]
        lastname=request.form.get("lastname")
        address=request.form.get("address")
        Phone=request.form.get("phone")
        visitflat=request.form.get("visitflat")
        Item=user(userid,firstname,lastname,address,loginType,visitflat,Phone)
        Items=Item.visitior_to_dict()
        print(Items)
        DB.insert_user(Items)
    return render_template('/postlogin.html')

@app.route('/postlogin<values>')
def postlog(values):
    print(values)
    username=values[0]
    print(username)
    return render_template('postlogin.html',username=username)


@app.route('/login',methods=["GET","POST"])
def login():
    userid=""
    if request.method=="POST":
        userid=request.form["username"]
        pwd=request.form["password"]
        print(userid+" "+pwd)
        list1=[]
        list1.append(userid)
        list1.append(pwd)
    if userid !="" and pwd !="":
        return redirect(url_for('postlog',values=list1))
    else:
        return render_template('/index.html')
    


if __name__ == "__main__":
    app.run(port=5000,debug=True)