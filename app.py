# step1 - importing flask   
from flask import Flask , request 

#step2 - creating object with parameter __main__
app=Flask(__name__)

#step3 create END point using routes and bind them in function 


@app.route('/uppercase')

def uppercase():
    username = request.args.get('name', '')
    username_upper = username.upper()
    return f'Hi, {username_upper}!, how are you'

if __name__ == '__main__':
    app.run(debug=True)


#step 4 
if __name__ =='__main__':
    app.run()