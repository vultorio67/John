# John
This project is a voice assistante with faciale recognition, her goal is to simulate human conversation. You can with him and he can learn.

*This project use opencv and face recognition to identifie user and storage userdata

*He are able to learn and save the new word that you learn to him.

# Installation and launche

To install all library and .exe that you need to launch john, you can execute installation.bat in the install folder. That will install all package you need.

But somtimes the installation of dlib issues to problem, so you can't install face recognition. ( that is my case). If you can't install dlib please :

1) Install anaconda : https://www.anaconda.com/products/individual
2) Open anaconda prompt and create new environment <conda create --name YOURNAME python=PYTHON_VERSION> and activate it < conda activate YOURNAME>
3) Verify that you have install cmake and visual studio c++ dev
  cmake : https://cmake.org/download/
  visual studio c++ dev : https://visualstudio.microsoft.com/fr/
4) Install library, to do that cd the anaconda command prompt to install folder < cd INSTALL_FOLDER > and type < pip install -r requirements.txt > 
5) Open anaconda navigator and go to your environment name, select ALL and search dlib and pyaudio and install it.
6) Type in command prompt pip install face_recognition
  
Now you are normally able to lauche john.
  
The command to start john is < python main.py > if you use anaconda and if you use simple python it is < py main.py >
