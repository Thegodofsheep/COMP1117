route = dict()
ex = 0
num = -1
stat_name = []
stat_print = str()

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
    while num != 0:
        desorext = input("Please choose a destination or enter 'Exit':"+"\n")
        if desorext == "Exit":
            print("Bye.")
            exit()
        elif desorext != "Exit" or desorext not in route:
            test1()
        else:
            print("Please enter the number of tickets:")
            num2buy = int(input())
            if num2buy > num:
                print("Error: Cannot handle your request.")
                exit()
            else:
                price = num2buy*int(route[desorext])
                while pay != "Cancel":
                    print("Destination: ",desorext,", Quantity: ",num2buy," Price: $",num2buy*int(route[desorext]),", Inserted: $",ins,".", sep="")
                    print("Please insert a coin or enter 'Cancel':")
                    pay = input()
                    if pay != "Cancel":
                        ins += int(pay)
                        ins_buf += int(pay)
                        coin.append(pay)
                        if ins >= price:
                            coin.sort()
                            for i in range(0, len(coin)):
                                coin[i] = "$"+coin[i]
                            num = num - num2buy
                            print("Dropped ticket(s). Your change: ",end="")
                            print("$",ins - price, sep="")
                            ins = 0
                            break
                    else:
                        break
            if ins_buf == 0:
                print("Cancelled. Returned no coin.")
            else:
                print("Cancelled. Returned coin(s):", coin)
                ins_buf = 0

while ex != "Exit":
    print("Out of Service. Please enter 'Exit':")
    ex = input()
    if ex == "Exit":
        print("Bye")
        exit()


