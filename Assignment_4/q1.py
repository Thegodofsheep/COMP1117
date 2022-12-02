route = dict()
num = 0
ins = 0

def parse_doc():
    global route
    global num
    stat_name = []
    stat_print = str()
    for i in fil:
        if len(list(i.strip())) == 1:
            num = int(i.strip())
        else:
            stat,cost = i.split()
            route[stat] = cost
            stat_name.append(" "+stat+",")

    stat_name[-1] = stat_name[-1].replace(",",".",1)

    for j in stat_name:
        stat_print += j
    return stat_print

print("File to initialize the vending machine:")
fil = open("/Users/conrad/Desktop/COMP1117/Assignment_4/"+input())
print("Station(s):",parse_doc())
print("tickets avalible: ",num)

while num != 0:
    print("Please choose a destination or enter 'Exit':")
    desorext = input()
    if desorext == "Exit":
        print("Bye.")
        exit()
    else:
        print("Please enter the number of tickets:")
        num2buy = int(input())
        if num2buy > num:
            print("Error: Cannot handle your request.")
            exit()
        else:
            price = num2buy*int(route[desorext])
            print("Destination: ",desorext,", Quantity: ",num2buy," Price: $",price,", Inserted: $",ins,".", sep="")
            print("Please insert a coin or enter 'Cancel':")
            pay = input()
            ins += int(pay)
            if ins >= price:
                print("Dropped ticket(s). Your change: ",)
                break
            while pay != "Cancel":
                print("Destination: ",desorext,", Quantity: ",num2buy," Price: $",num2buy*int(route[desorext]),", Inserted: $",ins,".", sep="")
                print("Please insert a coin or enter 'Cancel':")
                pay = input()
                ins += int(pay)
                if ins >= price:
                    print("Dropped ticket(s). Your change: ",)

print("Out of Service. Please enter 'Exit':")
input()
print("Bye")


