import datetime

x = datetime.datetime.now()
d_t=x.strftime("%d")+"_"+x.strftime("%b")+"_"+x.strftime("%Y") 

while (1):
    e = input("enter the details: y/n")
    if(e=='y'):
        name=input("enter the name")
        phno=int(input("enter the phone nummber"))
        place=input("enter place")
        temp=float(input("enter temperature"))
        list = [('Name: ', name),('PhNo: ',phno),('place: ',place),('Temperature: ',temp),('Date_time: ', datetime.datetime.now())]
        with open(d_t+".txt", "a") as f:
            f.write("-----------------------------\n")
            f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in list))   
            f.write("\n-----------------------------\n")
            f.close()
    else:
        break     
