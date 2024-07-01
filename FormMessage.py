def form(data):
    count = data[0]
    max_speed = 0
    max_diam = 0
    min_dist = float('inf')
    for i in range(1,len(data)):
        max_speed = max(max_speed,data[i][6])
        max_diam = max(max_diam,(data[i][2] + data[i][3])/2)
        min_dist = min(min_dist,data[i][7])
    record = [max_speed,max_diam,min_dist]
    name = [0,0,0]
    id = [0,0,0]
    for i in range(1,len(data)):
        if max_speed == data[i][6]:
            name[0] = data[i][0]
            id[0] = data[i][1]
        if max_diam == ((data[i][2] + data[i][3])/2):
            name[1] = data[i][0]
            id[1] = data[i][1]
        if min_dist == data[i][7]:
            name[2] = data[i][0]
            id[2] = data[i][1]
    return record,name,id,count
def message(record,name,id,count):
    string0 = "There are " + str(count) + " asteroids near Earth\n"
    string1 = "Asteroid with maximum speed has name and id:" + str(name[0])+ " "+ str(id[0])+" has speed of "+ str(record[0]) + "\n"
    string2 = "Asteroid with maximum diametr has name and id:" + str(name[1])+ " "+ str(id[1])+" has diametr of "+ str(record[1])+  "\n"
    string3 = "Asteroid with minimum distance has name and id:" + str(name[2])+ " "+ str(id[2])+" has distance of "+ str(record[2])
    string = string0 + string1 + string2 + string3
    return string