"""
██╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗████████╗░█████╗░██████╗░██╗░░░██╗
██║████╗░██║██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
██║██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
██║██║╚████║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░
██║██║░╚███║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ᴮʸ‧ ᴶᵒᵉˡ ᴿᵉˢᵗʳᵉᵖᵒ
"""

All_products = {
      
}

#Creations of functions

def Add_products():
      pass
def Update_prices():
      pass
def Delete_products():
      pass
def Total():
      pass

#We verify that there are at least 5 initial products 
def Verify():
    while len(All_products) < 5:
        try:
            product = input("Insert the name: ")
            if product in All_products:
                print("That product already exists.")
                continue

            price = int(input("Insert the price in USD: "))
            amount = int(input("Insert the amount: "))
            All_products[product] = (price, amount)
        except:
            print("Invalid input. Please try again.")

print("Initial number of products:", len(All_products))
Verify()
print("Final number of products:", len(All_products))

#
def View_products():

      print("")
      for product, (price, quantity) in All_products.items():
                  print(f"""
                        Product: {product}                    
                        Price: {price} dls
                        quantity: {quantity}                                
_________________________""")


def menu():
      
      print("""     
    █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
    █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█

    1. Add products:
    2. View products:
    3. Update prices:
    4. Delete products:
    5. Total inventory value:
          """)
    
      while True:
            try: 
                  Choice = int(input("Choose a number: "))      
                  if Choice > 0 and  Choice < 6:
                        break
                  else:
                        print("The number must be positive and within the range of options.") 
            except:
                  print("What are you doing? only numbers")

      match Choice:
            case 1 :
                  Add_products()
            case 2 :
                  View_products()
            case 3 :
                  Update_prices()
            case 4 :
                  Delete_products()
            case 5 :
                  Total()
            
             
menu()