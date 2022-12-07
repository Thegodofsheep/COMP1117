route = {"L":20, "q":3456}
def input_check(route):
    desorext = input("Please choose a destination or enter 'Exit':"+"\n")
    if desorext == "Exit":
        print("Bye.")
        exit()
    elif desorext in route:
        return desorext
    elif (desorext not in route):
        input_check(route)
    
def ticket_serv(num):

    num2buy = int(input("Please enter the number of tickets:"))
    if num2buy > num:
        print("Error: Cannot handle your request.")
        exit()
    return num2buy

def payment(num2buy,desorext,ins_buf,ins = 0):
    price = num2buy*int(route[desorext])
    pay = 0
    coin = []
    while pay != "Cancel":
        #print("Destination: ",desorext,", Quantity: ",num2buy," Price: $",price,", Inserted: $",ins,".", sep="")
        str_p = "Destination: {}, Quantity : {}, Price: ${}, Inserted: ${}.".format(desorext,num2buy,price,ins)
        print(str_p)
        pay = input("Please insert a coin or enter 'Cancel':")
        if pay == "Cancel":
            if ins_buf == 0:
                print("Cancelled. Returned no coin.")
            else:
                print("Cancelled. Returned coin(s):", coin)
                ins_buf = 0
        else:
            ins += int(pay)
            ins_buf += int(pay)
            coin.append(pay)
            if ins >= price:
                coin.sort()
                for i in range(len(coin)):
                    coin[i] = "$"+coin[i]
                #num = num - num2buy
                print("Dropped ticket(s). Your change: ",end="")
                print("$",ins - price, sep="")
                ins = 0
                return num2buy
            

payment(2,'L',0)
