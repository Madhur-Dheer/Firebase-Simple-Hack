# Firebase-Simple-Hack
A simple but useful Web-App designed to work with firebase for storing images and downloading it.

It is a useful simple web-app designed for the hackathon-enthusiast out there who are working in uploading images in firebase and downloading it.

Currently the functions this system can perform are :

1. Upload an image in the cloud storage of firebase.
2. During downloading any image there is a dropdown list which is dynamically updated based on the changes made in the cloud storage.

## How to run:

Install the dependencies - pyrebase,flask
run python app.py


# How the System Works ?

Steps involved on how the system will work are:

## Uploading steps :

Click on the upload , and upload the image from the local storage . Its done !!!.

As soon as the image is uploaded , a url of the same it stored in the realtime database of the firebase.
It will also ensure that each image stored has different name before storing it in the cloud storage database.


## Downloading steps :

All the urls stored in the RealTime database of the firebase are parsed and the image names are dynamically updates in the dropdown list.
User can selected any image from the list and press "Download" button to download and store it in the local system.

