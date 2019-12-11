import pyrebase

config={

    '''
    Input the firebase credentials here
    Create a Realtime Database for Storing the URL of the images that is stored
    in the Storage of Firebase.

    '''
 }


'''
Functions used are :-

retrieveimagename(passurl)-> It parses the image name from the url. The url
is the url of every image that is stored in the cloud storage in firebase.

testingavailibility(imagename)-> A function to test if the image name exists in the
database or not. If an image stored with same name available then a flash prompt
will be displayed stating "Change the name of the Image before storing in the database".


getlistofimages()-> List of all the images whose urls are stored in the realtime database. 


'''
firebase=pyrebase.initialize_app(config)

db=firebase.database()
storage=firebase.storage()


def retrieveimagename(passurl):
    end=passurl.find('?')
    start=passurl.find('%')
    ansstring=passurl[start+3:end]
    return ansstring

def testingavailibility(imagename):
    users=db.child("allurls").get()
    if users.val() is None :
        return False
    test=dict(users.val())
    anslist=[]
    for element in test.values():
        for testelement in element.values():
            result=retrieveimagename(testelement)
            anslist.append(result)
    if imagename in testelement:
        return True
    else:
        return False
    
def getlistofimages():
    users=db.child("allurls").get()
    test=dict(users.val())
    option_list=[]
    
    for element in test:
        adict=test[element]
        stringname=retrieveimagename(adict['URL'])
        adict['URL']=stringname
        option_list.append(adict)
    return option_list
        


from flask import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Oh So Secret'



@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        upload = request.files['upload']
        filename=upload.filename
        aval=testingavailibility(filename)
        if(aval==True):
            flash("An image is already stored in the database with same name")
            return render_template('index.html')
        else:
            teststring="images/"+filename
            storage.child(teststring).put(filename)
            url=storage.child(teststring).get_url(None)
            adict={"URL":url}
            db.child("allurls").push(adict)
            flash("Successfully Uploaded")
            return render_template('index.html')
    return render_template('index.html')


@app.route('/downloads', methods=['GET', 'POST'])
def downloads():
    option_list=getlistofimages()
    print(option_list)
    return render_template('download.html',option_list=option_list)

@app.route('/results',methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        imagename=request.form['option']
        astring="images/"+imagename
        storage.child(astring).download(imagename)
        return "Successfully Downloaded"
        

    

if __name__ == '__main__':
    app.run(debug=True)
