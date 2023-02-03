# ----------------------------------------------------- #
# sales management by toliors (last update: 23/01/2023) #
# ----------------------------------------------------- #

# +--- librarys ---+ #

from time        import sleep
from datetime    import datetime
import os
import platform
from prettytable import PrettyTable

# +--- variables n arrays ---+ #

uOption   = 0
qSales    = 0
lProducts = []
lPrices   = []
lHours    = []
lMins     = []

# +--- clear terminal ---+ #

def clear():

    if (platform.system() == "Windows"):
        os.system("cls")

    elif (platform.system() == "Linux"):
        os.system("clear")

    else:
        os.system("clear")

# +--- error no sales ---+ #

def error01():

    clear()
    error01 = PrettyTable()
    error01.field_names = ["\033[31m"+"error: you have no sales "+"\033[0;0m"]
    error01.add_row(["enter any key to continue"])

    print(error01)
    input("| => ")
    print("+"+"-"*27+"+")

# +--- error invalid input ---+ #

def error02():

    clear()
    error02 = PrettyTable()
    error02.field_names = ["\033[31m"+"error: invalid input "+"\033[0;0m"]
    error02.add_row(["enter any key to continue"])

    print(error02)
    input("| => ")
    print("+"+"-"*27+"+")


# +--- loop menu ---+ #

while (uOption != 4):

    sleep(2)
    clear()

    menu = PrettyTable()
    menu.field_names = ["option"]

    menu.add_row(["add"])
    menu.add_row(["remove"])
    menu.add_row(["summary"])
    menu.add_row(["exit"])
    menu.add_autoindex("#")

    menu.title = "sales manager"
    menu.align = "l"
    print(menu)

    uOption = input("| input # => ")
    clear()

    if uOption.isnumeric():

# +--- adding sale ---+ #

        if (uOption == "1"):

            print("+"+"-"*25+"+")
            print("|       adding sale       |")
            print("+"+"-"*25+"+")

            product = input("| name => ")
            lProducts.append(product)
            print("+"+"-"*25+"+")

            price = input("| price => ")
            if (price.isnumeric()):

                lPrices.append(price)
                print("+"+"-"*25+"+")

                lHours.append(datetime.now().hour)
                lMins.append(datetime.now().minute)

                qSales += 1
                print("|"+"\033[32m"+" sale successfully added "+"\033[0;0m"+"|")
                print("+"+"-"*25+"+")

            else:
                error02()

# +--- removing sale ---+ #

        elif (uOption == "2"):
            
            if (qSales > 0):

                box = PrettyTable()
                box.field_names = ["product", "price", "time"]

                for products, prices, hours, mins in zip(lProducts, lPrices, lHours, lMins):
                    box.add_row([f"{products}",f"R${prices}",f"{hours}h{mins}"])
                box.add_autoindex("#")

                box.title = "removing sale"
                box.align = "l"
                print(box)

                index = int(input("| which one? => "))

                if (index > box.rowcount or index <= 0):
                    error02()

                else:
                    
                    lProducts.pop(index-1)
                    lPrices.pop(index-1)
                    lHours.pop(index-1)
                    lMins.pop(index-1)

                    qSales -= 1
                    print("+"+"-"*27+"+")
                    print("|"+"\033[32m"+" sale successfully removed "+"\033[0;0m"+"|")
                    print("+"+"-"*27+"+")

            else:
                error01()
                
# +--- sales sumarry ---+ #

        elif (uOption == "3"):

            if (qSales > 0):
                
                box = PrettyTable()
                box.field_names = ["products", "price", "time"]

                for products, prices, hours, mins in zip(lProducts, lPrices, lHours, lMins):
                    box.add_row([f"{products}",f"R${prices}",f"{hours}h{mins}"])
                box.add_autoindex("#")

                box.title = "sales summary"
                box.align = "l"
                print(box)

                input("| enter any key to continue => ")
                print("+"+"-"*30+"+")

            else:
                error01()
            
            
# +--- exiting ---+ #

        elif (uOption == "4"):
            exit()

# +--- invalid input ---+ #

        elif (uOption not in ["1", "2", "3", "4"]):
            error02()

    else:
        error02()
