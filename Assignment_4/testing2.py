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
    print("Station(s):",stat_print)
    return route,num


fil= open("/Users/conrad/Desktop/COMP1117/Assignment_4/"+input())
stations = parse_doc(fil)