echo off
set /p id=Do you want to install library for this program ( yes ; no) :
IF %id%=="yes" goto install(
    py -m pip install gTTS
    py -m pip install pyttsx3
    py -m pip install speech_recognition
    py -m pip install opencv-python
    py -m pip install numpy

    set /p cmake=To install face_recognition you need to install cmake, I can do it for you, do you want (yes ; no) :
    IF %cmake%=="yes" echo saluts
    	start https://github.com/Kitware/CMake/releases/download/v3.21.0/cmake-3.21.0-windows-x86_64.msi

    set /p cmake=To install face_recognition you need to install visual studio c++ developement, I can do it for you, do you want (yes ; no) :
    IF %cmake%=="yes" echo saluts
    	start https://visualstudio.microsoft.com/fr/thank-you-downloading-visual-studio/?sku=Community&rel=16

    set /p cmake=Do you have finish to install this 2 application (yes ; no) :
    IF %cmake%=="yes" echo saluts
    	py -m pip install dlib
    	py -m pip install cmake
    	py -m pip install face_recognition

)


pause