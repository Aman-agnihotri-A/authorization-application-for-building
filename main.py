from flask import Flask , render_template, request
import DB
from Users import Users as user

app = Flask(__name__)



def printword(word):
    print(word)


@app.route('/',methods=["GET","POST"])
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
    return render_template('/index.html')


if __name__ == "__main__":
    app.run(port=5000,debug=True)