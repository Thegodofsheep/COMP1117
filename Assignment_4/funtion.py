def prep():
    route = dict()
    ex = 0
    num = -1
    stat_name = []
    stat_print = str()
    print("File to initialize the vending machine:")
    fil = open(input())
    stations,num,stat_str = parse_doc(fil)
    return route,ex,num,stat_name,stat_print,stations,stat_str

def parse_doc(fil,route = dict(),num = -1):
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
    stat_print = "Station(s):"+stat_print
    return route,num,stat_print

def input_check(route):
    desorext = input("Please choose a destination or enter 'Exit':"+"\n")
    if desorext == "Exit":
        print("Bye.")
        exit()
    elif desorext in route:
        return desorext
    elif (desorext not in route) or desorext is None:
        input_check(route)

def ticket_serv(num):
    num2buy = int(input("Please enter the number of tickets:"+ "\n"))
    if num2buy > num:
        print("Error: Cannot handle your request.")
        return False

    return num2buy

def payment(num2buy,desorext,route):
    print(desorext)
    price = num2buy*int(route[desorext])
    ins,ins_buf = 0,0
    pay = 0
    coin = []
    while pay != "Cancel":
        str_p = "Destination: {}, Quantity : {}, Price: ${}, Inserted: ${}.".format(desorext,num2buy,price,ins)
        print(str_p)
        pay = input("Please insert a coin or enter 'Cancel':"+ "\n")
        if pay == "Cancel":
            if ins_buf == 0:
                print("Cancelled. Returned no coin.")            
            else:
                coin.sort()
                r_coin = str()
                for i in range(len(coin)):
                    coin[i] = "$"+coin[i]
                for j in coin:
                    r_coin+=j
                    r_coin+=", "
                r_coin-=", "
                print(r_coin)
                print("Cancelled. Returned coin(s):",[coin[i] for i in range(len(coin))])
                ins_buf = 0
            return 0
        else:
            ins += int(pay)
            ins_buf += int(pay)
            coin.append(pay)
            if ins >= price:
                print("Dropped ticket(s). Your change: ",end="")
                print("$",ins - price, sep="")
                ins = 0
                return num2buy

def force_exit():
    ex = input()
    if ex == "Exit":
        print("Bye")
        exit()
    else:
        print("Out of Service. Please enter 'Exit':")
        force_exit()


def main():
    route,ex,num,stat_name,stat_print,stations,stat_str = prep()
    while num != 0:
        print(stat_str)
        desorext = input_check(stations)
        num2buy = ticket_serv(num)
        while num2buy is False:
            print(stat_str)
            desorext = input_check(stations)
            num2buy = ticket_serv(num)
        num -= payment(num2buy,desorext,stations)

    print("Out of Service. Please enter 'Exit':")
    force_exit()

main()