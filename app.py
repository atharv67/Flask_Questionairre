from flask import Flask,render_template,url_for,request,redirect
import random 
import os
from flask_sqlalchemy import SQLAlchemy
clothes=os.listdir(os.path.join(os.path.join("static","images"),"upper_body"))
final_list=[]
for i in range(10):
    option=random.choice(clothes)
    clothes.remove(option)
    final_list.append(option)
print(final_list)
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
db=SQLAlchemy(app)
class Entries(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    upper_body_img=db.Column(db.String(50))
    pant1=db.Column(db.Integer)
    pant2=db.Column(db.Integer)
    pant3=db.Column(db.Integer)
    pant4=db.Column(db.Integer)
    pant5=db.Column(db.Integer)
    pant6=db.Column(db.Integer)
    pant7=db.Column(db.Integer)
    pant8=db.Column(db.Integer)


@app.route('/',methods=['POST','GET'])
def homepage1():
    if request.method=='POST':
        user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        print(user,pants_liked)
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[0],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()

        except:
            pass
        finally:
            return redirect(url_for('homepage2'))
    path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[0])
    return render_template('homepage1.html',path=path)
@app.route('/homepage2',methods=['POST','GET'])
def homepage2():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[1],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('homepage3'))
    path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[1])
    return render_template('homepage2.html',path=path)
@app.route('/homepage3',methods=['POST','GET'])
def homepage3():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[2],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('homepage4'))
    path=path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[2])
    return render_template('homepage3.html',path=path)
@app.route('/homepage4',methods=['POST','GET'])
def homepage4():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[3],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('homepage5'))
    path=path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[3])
    return render_template('homepage4.html',path=path)
@app.route('/homepage5',methods=['POST','GET'])
def homepage5():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
       
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[4],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('homepage6'))
    path=path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[4])
    return render_template('homepage5.html',path=path)
@app.route('/homepage6',methods=['POST','GET'])
def homepage6():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[5],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('homepage7'))
    path=path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[5])
    return render_template('homepage6.html',path=path)
@app.route('/homepage7',methods=['POST','GET'])
def homepage7():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[6],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('homepage8'))
    path=path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[6])
    return render_template('homepage7.html',path=path)
@app.route('/homepage8',methods=['POST','GET'])
def homepage8():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[7],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('homepage9'))
    path=path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[7])
    return render_template('homepage8.html',path=path)
@app.route('/homepage9',methods=['POST','GET'])
def homepage9():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[8],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('homepage10'))
    path=path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[8])
    return render_template('homepage9.html',path=path)
@app.route('/homepage10',methods=['POST','GET'])
def homepage10():
    if request.method=='POST':
        # user=request.form['user_name']
        pants_liked=request.form.getlist('pants')
        if 'pant1' in pants_liked:
            pant1=1
        else:
            pant1=0
        if 'pant2' in pants_liked:
                pant2=1
        else:
            pant2=0
        if 'pant3' in pants_liked:
                pant3=1
        else:
            pant3=0
        if 'pant4' in pants_liked:
                pant4=1
        else:
            pant4=0
        if 'pant5' in pants_liked:
                pant5=1
        else:
            pant5=0
        
        if 'pant6' in pants_liked:
                pant6=1
        else:
            pant6=0
        if 'pant7' in pants_liked:
                pant7=1
        else:
            pant7=0
        if 'pant8' in pants_liked:
                pant8=1
        else:
            pant8=0
        new_row=Entries(upper_body_img=final_list[9],pant1=pant1,pant2=pant2,pant3=pant3,pant4=pant4,pant5=pant5,pant6=pant6,pant7=pant7,pant8=pant8)
        try:
            db.session.add(new_row)
            db.session.commit()
        except:
            pass
        finally:
            return redirect(url_for('thankyou'))
    path=path=os.path.join(os.path.join(os.path.join("static","images"),"upper_body"),final_list[9])
    return render_template('homepage10.html',path=path)
@app.route('/thankyou')
def thankyou():
    return "Thank you"


if __name__=="__main__":

    app.run(debug=True)