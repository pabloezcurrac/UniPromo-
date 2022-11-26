#FUNCTIONS
def login():
  "Let's Log in the UniPromo Beta App for first time, with just your name, surname and university mail is enough!"
  name = input("Name: ")
  surname = input("Surname: ")
  mail = input("Mail: ")

  user = (name, surname, mail)


def categories_creator():   
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

def categories_prefered_from_more_to_less():
  print("\n These are your new preferences from more to less \n")
  print("From prefered to less prefered:")
  User.adjacencylist.extend([TRAVELLING, SPORTS, RESTAURANTS, ELECTRONIC_GADGETS, LEISURE, BOOKS, TRANSPORTS, ACCOMODATION, WORK_OPPORTUNITIES])
  print(User.bfs())

def preferences_changer():
  print("Let's change yout preferences! ")
  categories_creator()   
  print("These are your preferences updated! ")
  categories_prefered_from_more_to_less()



def promotions_displayer():
  n=5
  print("Promotions Available:")
  while n>0:  
    if TRAVELLING.rating == n:
      print(f"\n Destiny: {Rome1.destiny} ||\n Info: {Rome1.info} ||\n Discount: {Rome1.discount} ||\n Link: {Rome1.link}\n\n")

    if RESTAURANTS.rating == n:
      print(f"\n Name: {Bel_mondo1.name} ||\n Restaurant:{Bel_mondo1.type_of_restaurant} ||\n Location: {Bel_mondo1.location} ||\n Discount: {Bel_mondo1.discount} ||\n Link: {Bel_mondo1.link} \n\n")

    if SPORTS.rating == n:
      print(f"\n Brand: {Sports_Equipment1.brand} ||\n Accessory: {Sports_Equipment1.accessory} ||\n Information: {Sports_Equipment1.information} ||\n Discount: {Sports_Equipment1.discount} ||\n Link: {Sports_Equipment1.link} \n\n")

    if ELECTRONIC_GADGETS.rating == n:
      print(f"\n Product: {Headphones1.product} ||\n Shop: {Headphones1.shop} ||\n Brand: {Headphones1.brand} ||\n Discount: {Headphones1.discount} Link: {Headphones1.link} \n\n")

    if LEISURE.rating == n:
      print(f"\n Leisure: {Disco1.leisure} ||\n Info: {Disco1.info} ||\n Discounts: {Disco1.discount} ||\n Link: {Disco1.link} \n\n")

    if BOOKS.rating == n:
      print(f"\n Name: {grokking_algorithms.name} ||\n Author: {grokking_algorithms.author} ||\n Category: {grokking_algorithms.category} ||\n Discount: {grokking_algorithms.discount} ||\n Link: {grokking_algorithms.link} \n\n")

    if TRANSPORTS.rating == n:
      print(f"\n Transport: {Subway1.transport} ||\n Company: {Subway1.company} ||\n Discount: {Subway1.discount} ||\n Link: {Subway1.link} \n\n")

    if ACCOMODATION.rating == n:
      print(f"\n Type of Accomodation: {nh_hotel1.type_acc} ||\n Company: {nh_hotel1.company} ||\n Description: {nh_hotel1.description} ||\n Location: {nh_hotel1.location} ||\n Discount: {nh_hotel1.discount} ||\n Link: {nh_hotel1.link}\n\n")

    if WORK_OPPORTUNITIES.rating == n:
      print(f"\n Postion: {amazon1.position} ||\n Company: {amazon1.company} ||\n Description: {amazon1.description} ||\n Link: {amazon1.link} \n\n")
    n-=1





