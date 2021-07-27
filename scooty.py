# print("welcome to RIDER APP")
# print("current location")
# name=input("enter the name")

# driver_names=["srikanth","ravi","sathish","rami","raju"]
# distance=int(input("enter the distance"))
# m=distance*5
# print(m)
import random 
print("*********Hii krishna devi uber service center **********")
name = input("enter your name = ")
print("welcome to my uber app",name)
rider = [1,2,3,4,5]

def booking():
    limit = int(input("enter how much ride we have to do for you = "))
    index = 1
    total = 0
    dict = {}
    while index <= limit:
        distance = int(input("enter how much far you will go distance in km = "))
        place = input("enter any place name = ")
        driver = random.choice(rider)
        print(driver,"this driver is available")
        if driver in rider:
            print("which driver you choice",driver,"he is on that distination",place)
            money = distance*5
            total += money
            print(index,"ride money = ",money)
        else:
            print("driver is not available")
        print(limit,"ride your total amount = ",total)
        dict[driver] = total
        index += 1
    print(dict,"this is all ride data")
    max = 0
    for key in dict:
        if dict[key] > max:
            max = dict[key]
    print(key,"this driver is earn more money",max)




def cancel():
    print("thanks for visit my Rider sharing app  and you cancel the cave safely.")

def main():
    options = int(input("if you want book you give 1 and if you want cancle you give 2  = "))
    if options == 1:
        booking()
        print("thanks to visit my cave service ","\U0001F929")
    else:
        cancel()

main()