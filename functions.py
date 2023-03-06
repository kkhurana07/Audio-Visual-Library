import cmpt120image
import random
from replit import audio
import helper


#dictionary operations
dictionary = {}
file = open("town.csv")


for line in file:
  (key, value) = line.strip().split(",")

  dictionary[str(key)] = value

reversed_dict = {v: k for k, v in dictionary.items()}  
#____________________________________#

#creating new list for reversed dictionary 
new_list = list(reversed_dict.keys())    
    
#question function
def question():
  print("Do you wanna learn the things around you (learn) or move\
  to another scene (move)\n")

  

def input1():
  take = input().lower()

  return take   

def StartingQuestion():
  print("Which scene do you wanna go to? \n")
    

#learning function defined
def learning():
  for i in range(5):
    word = input("Which blackfoot word would you like to learn?\n").lower()\
    .replace(" ","").replace("'","")
    if word in dictionary:
     print("The blackfoot word" 
     " is: ")
     print(dictionary[word]) 
     audio.play_file("sounds/" + word.replace('_','') + ".wav")
    else:
      print("Sorry, this image is not on the screen ") 

  hello = input("Do you want to get tested (test),\
  move to another scene or go directly to the speech synthesis part(speech) \n").lower()

  if hello == "test":
    print("Before starting your test, tell me which scene you are on?")
    testing()

  elif hello == "speech":
    helper.concatenate()

  elif hello == "move":
    move()

  else:
    print("Not a valid request!, please enter again")
    testing()


#move function defined, this helps to move within different scenes
def move():
  print("Which scene do you wanna move to?\n")

  move = input().lower()
  if move == "town":
    town = cmpt120image.getImage("pictures_cmpt/town.PNG")
    cmpt120image.showImage(town,"win")

  elif move == "restaurant":
    restro = cmpt120image.getImage("pictures_cmpt/restaurant.PNG")
    cmpt120image.showImage(restro,"win")

  elif move == "family":
    family = cmpt120image.getImage("pictures_cmpt/family.png")
    cmpt120image.showImage(family,"win")

  elif move == "greeting":
    greeting = cmpt120image.getImage("pictures_cmpt/greeting.PNG")
    cmpt120image.showImage(greeting,"win")

  elif move == "house":
    house = cmpt120image.getImage("pictures_cmpt/house.PNG")
    cmpt120image.showImage(house,"win")

  else:
    print("Sorry, but this scene doesn't exist!")  

  abc = input("To learn blackfoot words from this scene, type 'learn' \n").lower() 
  if abc == "learn":
    learning()     


#testing function defined, this function will test the user in particular scene
#and will also test in a mcq form
def testing():

  new_list = list(reversed_dict.keys())
  second_list = list(dictionary.keys())

  test = input().lower()
  if test == "town":
    new_list = new_list[0:5]
    second_list = second_list[0:5]
  elif test == "restaurant":
    new_list = new_list[6:15]
    second_list = second_list[6:15] 
  elif test == "home":
    new_list = new_list[16:22]
    second_list = second_list[16:22]
  elif test == "family":
    new_list = new_list[23:28]
    second_list = second_list[23:28]
  elif test == "greeting":
    new_list = new_list[29:38] 
    second_list = second_list[29:38] 


  #initializing the test score
  test_score = 0
  for i in range(10):
  
    random_word = random.choice(new_list)

    answer = input("what is the english for the blackfoot word " + random_word + " ? \n").lower().replace(" ","")

    if str(answer) == str(reversed_dict[random_word]):
      test_score += 1
      
      print("Well done, that is the correct answer!! ")
    
    
    else:
      print("Wrong answer")
  print("Your test score is " + str(test_score)) 

  print("Your testing part has finished.")
  test_input =input("Do you wanna get tested in another way?\n").lower()

  if test_input == "yes":
    for i in range(5):
      second_random = random.choice(second_list)

      print("Which is the correct blackfoot word\
      for the following english word?\n"+ second_random + " :\n")

      answer = input(random.choice(list(dictionary.values()))+ " or"\
      + dictionary[second_random]+ "\n").lower()

      if str(answer) == str(dictionary[second_random]).lower():

        print("Congrats, that is the right answer!")


      else:
        print("That is the wrong answer! Hard luck!") 
  
  move()        


  

  

#scene list function  
def Scenelist():

 scene = input1()

 if scene == "town":
   town= cmpt120image.getImage("pictures_cmpt/town.PNG")
   cmpt120image.showImage(town,"window")
      
 elif scene == "restaurant":
   restro = cmpt120image.getImage("pictures_cmpt/restaurant.PNG")
   cmpt120image.showImage(restro,"window")

 elif scene == "home":
    home = cmpt120image.getImage("pictures_cmpt/house.PNG")
    cmpt120image.showImage(home,"window")
    question()
     
 elif scene == "family":
    family=cmpt120image.getImage("pictures_cmpt/family.png")
    cmpt120image.showImage(family,"window")
    
 elif scene == "greeting":
    greet = cmpt120image.getImage("pictures_cmpt/greeting.PNG")
    cmpt120image.showImage(greet, "window")
     
 else:
    print("This scene doesn't exist, sorry please enter the scene again \n")
    Scenelist()

#defining took function, this takes the value for whether learn, move or test
def took():
  take = input().lower()

  if take == "learn":
    learning()
  elif take == "move":
    move()
  elif take == "test":
   testing() 
  else:
    print(" invalid, please enter again \n")
    took()      