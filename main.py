from our_classes import *
from our_functions import *
from promotions import *

def main():
  print('\n-------------------- Welcome to UniPromo! --------------------')
  print("We want to know which topics are you interested in! \n Log In with your Name, Surname and university mail to\n know your university and show the promotions you have avalable.\n Then, you will show your interests in the differrent topics of the promotions" 
  )
  login()
  print("Let's customize for first time your favourite type of promotions!")

  User = Node("User", 0)
  print("TRAVELLING")
  answer = input("Give your preference from 1 to 5: ")
  answer = int(answer)
  TRAVELLING = Node("TRAVELLING", answer)

  print("RESTAURANTS")
  answer = int(input("Give your preference from 1 to 5: "))
  RESTAURANTS = Node("RESTAURANTS", answer)

  print("SPORTS")
  answer = int(input("Give your preference from 1 to 5: "))
  SPORTS = Node("SPORTS", answer)

  print("ELECTRONIC_GADGETS")
  answer = int(input("Give your preference from 1 to 5: "))
  ELECTRONIC_GADGETS = Node("ELECTRONIC_GADGETS", answer)

  print("LEISURE")
  answer = int(input("Give your preference from 1 to 5: "))
  LEISURE = Node("LEISURE", answer)

  print("BOOKS")
  answer = int(input("Give your preference from 1 to 5: "))
  BOOKS = Node("BOOKS", answer)

  print("TRANSPORTS")
  answer = int(input("Give your preference from 1 to 5: "))
  TRANSPORTS = Node("TRANSPORTS", answer)

  print("ACCOMODATION")
  answer = int(input("Give your preference from 1 to 5: "))
  ACCOMODATION = Node("ACCOMODATION", answer)

  print("WORK_OPPORTUNITIES")
  answer = int(input("Give your preference from 1 to 5: "))
  WORK_OPPORTUNITIES = Node("WORK_OPPORTUNITIES", answer)
    
  User.adjacencylist.extend([TRAVELLING, SPORTS, RESTAURANTS, ELECTRONIC_GADGETS, LEISURE, BOOKS, TRANSPORTS, ACCOMODATION, WORK_OPPORTUNITIES])

  print("Let's discover your promotions! \n Click the link of the promotion you \n are interested in, you'll be redirected to the page with the discount applied. \n")
  promotions_displayer()


  ans = input("Do you want to change your preferences? (yes/no): ")
  ans.lower()
  if ans == "yes":
    preferences_changer()
    print("These are your preferences from more to less:")
    print(User.bfs())
  elif ans == "no":
    None
  else:
    print("Invalid input") 



  print('\n---Thank you for using UniPromo! We hope you enjoyed your promos---\n')

main()
