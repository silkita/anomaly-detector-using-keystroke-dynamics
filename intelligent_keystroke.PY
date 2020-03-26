from pynput import keyboard 
from pynput.keyboard import Key
import time
from operator import add
temp = []
test_vec = []
observation = {}

def callb(key):  #what to do on key-release
    ti1 = str(time.time() - t)[0:5]  #converting float to str, slicing the float
    print("Releasd ",key,"at ",time.time())
    temp.append(time.time())
    test_vec.append(time.time())
    print("The key",key," was holded for",ti1,'seconds')
    if key == Key.enter:
        print(temp)
        return False
    return False #stop detecting more key-releases

def callb1(key): #what to do on key-press
    print("pressed ",key,"at ",time.time())
    test_vec.append(time.time())
    temp.append(time.time())
    if key == Key.enter:
        return False
    return False #stop detecting more key-presses


def manhattan_score(vect):
    res = {}
    for x in observation:
        #print(observation[x])
        min = 1.0
        su = observation[x][0]
        for ob in range(1,len(observation[x])):
            sum=0 
            su = list( map(add, su, observation[x][ob]) )
            print("test",su)
        final_vec = []
        for elem in su:
            final_vec.append(float(elem/len(su)))
        sum = 0
        a_vec = []
        if len(vect)==len(final_vec):
                for i in range(0,len(vect)):
                    sum+=abs(vect[i]-final_vec[i])
        else:
                print("not same")
        res[x] = 1-float(sum/len(vect))
    return res




while 1:
    username = input("Enter the subject name: ")
    observation[username]=list()
    pass_length = input("Enter the Password Length(including Enter Key): ")
    for i in range(0,2):
        print("\nEnter your password again\n")
        temp = []
        for j in range(0,int(pass_length)):
              with keyboard.Listener(on_press = callb1) as listener1: #setting code for listening key-press
                        listener1.join()
                        listener1.stop()

              t = time.time() #reading time in sec

              with keyboard.Listener(on_release = callb) as listener: #setting code for listening key-release
                        listener.join()
                        listener.stop()
        vect = []
        for k in range(0,len(temp)-2):
            hold = temp[k+1]-temp[k]
            dd = temp[k+2]-temp[k]
            ud = temp[k+2]-temp[k+1]
            vect.append(hold)
            vect.append(dd)
            vect.append(ud)
        vect.append(temp[len(temp)-1]-temp[len(temp)-2])
        observation[username].append(vect)
    print(observation)
    time.sleep(3)
    for t in range(0,2):
        option = input()
    option = input("Do you want to Test for a New Subject?(y or n) ")
    if option == 'y':
        while 1:
            print("testing")
            pass_length = input("Enter the Password Length(including Enter Key): ")
            for i in range(0,1):
                print("\nEnter your password:\n")
                test_vec = []
                for j in range(0,int(pass_length)):
                        with keyboard.Listener(on_press = callb1) as listener1: #setting code for listening key-press
                            listener1.join()
                            listener1.stop()

                        t = time.time() #reading time in sec

                        with keyboard.Listener(on_release = callb) as listener: #setting code for listening key-release
                            listener.join()
                            listener.stop()
                vect = []
                time.sleep(3)
                option = input()
                for k in range(0,len(test_vec)-2):
                    hold = test_vec[k+1]-test_vec[k]
                    dd = test_vec[k+2]-test_vec[k]
                    ud = test_vec[k+2]-test_vec[k+1]
                    vect.append(hold)
                    vect.append(dd)
                    vect.append(ud)
                vect.append(test_vec[len(test_vec)-1]-test_vec[len(test_vec)-2])
                print(vect)
                print(manhattan_score(vect))
            option = input("Do you want to Test for a New Subject?(y or n) ")
            if option == 'n':
                break


    

            

