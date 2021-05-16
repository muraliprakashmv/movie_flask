from flask import *
app=Flask(__name__)
import pymysql

app.secret_key='qwerty'
con=pymysql.connect(host='localhost',port=3308,user='root',password='root',db='rating')
cmd=con.cursor()
@app.route('/')
def main():
      return render_template('index_login.html')

@app.route('/log')
def log():
      return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()

    return redirect('/')
@app.route('/login',methods=['post','get'])
def login():
    username=request.form['textfield']
    password=request.form['textfield2']
    print(username)
    print(password)
    cmd.execute("select * from login where username='"+username+"' and password='"+password+"'")
    s=cmd.fetchone()
    print(s)
    if s is None:
        return '''<script>alert("invalid user");window.location="/"</script>'''
    elif(s[3]=="admin"):
        session['lid']=s[0]
        return  '''<script>alert("SUCCESSFULLY LOGIN");window.location="/adhome"</script>'''
    elif (s[3] == "Director"):
        session['lid'] = s[0]
        return '''<script>alert("SUCCESSFULLY LOGIN");window.location="/drhome"</script>'''
    else:
       return '''<script>alert("invalid user");window.location="/"</script>'''
@app.route('/adhome')
def adhome():
    if 'lid' in session:
        return render_template('ad_home.html')
    else:
        return redirect('/')

@app.route('/approve_dr')
def approve_dr():
    if 'lid' in session:

        cmd.execute("select director.* from director join login on login.id=director.loginid where login.type='pending' ")
        s = cmd.fetchall()
        return render_template('approve_dr.html', val=s)
    else:
        return redirect('/')


@app.route('/approvedr',methods=['post','get'])
def approvedr():
    if 'lid' in session:
        id = request.args.get('id')
        cmd.execute("update login set type='Director' where Id='"+str(id)+"'")
        con.commit()
        return'''<script>alert("Approved");window.location="/approve_dr"</script>'''
    else:
        return render_template("login.html")

@app.route('/rejectdr',methods=['post','get'])
def rejectdr():
    if 'lid' in session:
        id=request.args.get('id')
        cmd.execute("delete from director where loginid='"+str(id)+"'")
        cmd.execute("delete from login where id='" + str(id) + "'")
        con.commit()
        return '''<script>alert("Rejected");window.location="/approve_dr"</script>'''
    else:
        return render_template("login.html")

@app.route('/view_movies')
def view_movies():
    if 'lid' in session:

        cmd.execute("SELECT `movie`.*,`director`.`directorname` FROM `movie` JOIN `director` ON `movie`.`director`=`director`.`loginid`")
        s = cmd.fetchall()
        return render_template('view_movies.html', val=s)
    else:
        return redirect('/')
@app.route('/drhome')
def drhome():
    if 'lid' in session:
        return render_template('dr_home.html')
    else:
        return redirect('/')
@app.route('/add_movie')
def add_movie():
    if 'lid' in session:

        cmd.execute("select director.* from director join login on login.id=director.loginid where login.type='Director' ")
        s = cmd.fetchall()
        return render_template('admin.html', val=s)
    else:
        return redirect('/')

@app.route('/director')
def director():
    if 'lid' in session:

        return render_template("director.html")
    else:
        return redirect('/')
@app.route('/storyboard')
def storyboard():
    if 'lid' in session:

        cmd.execute("select * from movie")
        s=cmd.fetchall()
        return render_template("storyboard.html", val=s)
    else:
        return redirect('/')
@app.route('/storyboard2',methods=['post'])
def storyboard2():
    if 'lid' in session:

        mid=request.form['select']
        strttime = request.form['textfield']
        endtime = request.form['textfield2']
        emotion = request.form['textfield3']
        cmd.execute("insert into storyboard values(null,'"+mid+"','"+strttime+"','"+endtime+"','"+emotion+"')")
        con.commit()
        return '''<Script>alert('registerd');window.location='/drhome'</script>'''
    else:
        return redirect('/')


@app.route('/addirector',methods=['post'])
def addirector():
    if 'lid' in session:

        DIRECTORNAME=request.form['textfield1']
        HOUSENAME=request.form['textarea1']
        PLACE=request.form['textfield2']
        POST=request.form['textfield3']
        PIN=request.form['textfield4']
        GENDER=request.form['radiobutton']
        PHONE=request.form['textfield5']
        EMAIL=request.form['textfield6']
        USERNAME=request.form['textfield7']
        PASSWORD=request.form['textfield8']


        cmd.execute("insert into login values(null,'"+USERNAME+"','"+PASSWORD+"','pending')")
        login_id=con.insert_id()
        cmd.execute("insert into director values(null,'"+str(login_id)+"','"+DIRECTORNAME+"','"+HOUSENAME+"','"+PLACE+"','"+POST+"','"+PIN+"','"+GENDER+"','"+PHONE+"','"+EMAIL+"')")
        con.commit()
        return '''<Script>alert('registerd');window.location='/'</script>'''
    else:
        return redirect('/')


@app.route('/addmovie',methods=['post'])
def addmovie():
    if 'lid' in session:

        MOVIENAME=request.form['textfield1']
        DIRECTOR=request.form['select']
        RELEASEDATE=request.form['date']
        ACTORS=request.form['textarea1']
        RELEASELOCATION=request.form['textarea2']

        cmd.execute("insert into movie values(null,'"+MOVIENAME+"','"+DIRECTOR+"','"+RELEASEDATE+"','"+ACTORS+"','"+RELEASELOCATION+"')")
        con.commit()
        return '''<Script>alert('registerd');window.location='/drhome'</script>'''
    else:
        return redirect('/')



@app.route('/success_rate')
def success_rate():
    if 'lid' in session:
        cmd.execute("select * from movie")
        s= cmd.fetchall()
        return render_template("viewsuccess_rate.html", val=s)
    else:
        return redirect('/')


@app.route('/success_rate2',methods=['post'])
def success_rate2():
    if 'lid' in session:
        mid= request.form['movie']
        cmd.execute("SELECT `movie`.`moviename`,`director`.`directorname`,round(AVG(`rating_tbl`.`rate`)) FROM `rating_tbl` JOIN `movie` ON `movie`.`id`=`rating_tbl`.`mid` JOIN `director` ON `director`.`loginid`=`movie`.`director` WHERE `rating_tbl`.`mid`='"+mid+"'")
        s2= cmd.fetchall()
        cmd.execute("select * from movie")
        s = cmd.fetchall()
        return render_template("viewsuccess_rate.html", val2=s2, val=s)
    else:
        return redirect('/')


if(__name__)=='__main__':
    app.run(debug='True')

