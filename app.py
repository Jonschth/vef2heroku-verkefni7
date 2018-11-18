from bottle import run, route, get, post, request, template, response, redirect
from  verkefni7_2 import *

from sys import argv

import bottle
from bottle import *
bottle.debug(True)

@route('/')
def val():
    return '''

            <a href="/login"><h2>Skrá inn</h2></a>
            <a href="/ny_skra">Ný skrá</a>
                '''

########################################
#### login 
########################################
@get('/login') # or @route('/login')
def login():
    return '''
        <h1>Inn skráning</h1>
        <form action="/login" method="post">
            <h3>Username:</h3> <input name="username" type="text" />
           <h3> Password:</h3> <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    # hér væri hægt að nota csv skrá til að bera saman við notendur og lykilorð
    # harðkóðuð lausn


    if passa_notendaupplysingar(username,password):
        response.set_cookie("logged", username, secret='some-secret-key')
        return redirect("/restricted")
    else:
        return """
        <h1> rangt username/password</h1>
        """

############################
### lokuð síða
##############################        

@route('/restricted')
def restricted_area():
    username = request.get_cookie("logged", secret='some-secret-key')
    if username:
        return template("admin.tpl", name=username)
    else:
        return redirect ("/ny_skra")
    
########################################
#### nýskrá 
########################################
    
@get('/ny_skra') # or @route('/login')
def ny_skra():
    return '''
        <h1>Ný skráning</h1>
        <form action="/ny_skra" method="post">
           <h3> Username: </h3><input name="username" type="text" />
            <h3>Password: </h3> <input name="password" type="password" />
            <h3>Name:</h3> <input name="name" type="name"/>
            <input value="Ný skrá" type="submit" />
        </form>
    '''

@post('/ny_skra') # or @route('/login', method='POST')
def do_ny_skra():
    username = request.forms.get('username')
    password = request.forms.get('password')
    name = request.forms.get('name')

    # hér væri hægt að nota csv skrá til að bera saman við notendur og lykilorð
    # harðkóðuð lausn


    if er_notandinn_til(username,password):
        return """
        <h1>username/password nú þegar til</h1>
        <h1>sláðu inn nýtt usrename/password</1h>
        """
    else:
        response.set_cookie("logged", username, secret='some-secret-key')
        nyr_notandi(username,password,name)
        return redirect("/restricted")





@route('/logout')
def logout():
    # eyðum cookie
    response.set_cookie("logged", "", expires=0)
    redirect('/')





bottle.run(host='0.0.0.0', port=argv[1], debug=True)
