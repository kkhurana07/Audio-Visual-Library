#Final project
#jaideep singh & Kunal Khurana
#301448987 & 301355396
#April 14th, 2021
#Created an application which helps you learn the translation between
#english words and the blackfoot words. This application will make you
#learn, test, move to 5 different scenes and some more interesting features

#Importing files for running the program
import cmpt120image
import functions

#showing main page
welcome = cmpt120image.getImage("pictures_cmpt/welcome.JPG")
cmpt120image.showImage(welcome, "window")

#asking the user to enter into a particular scene
print(
    "Hi, do you wanna go to the town,restaurant, family, house or greeting? \n"
)

functions.Scenelist()
functions.question()
functions.took()
