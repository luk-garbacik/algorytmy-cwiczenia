from Horner1 import horner
def bisekcja (wsp,a,b,E):
    # warunek: twierdzenie bolzano cauchy'ego
    if (horner(wsp,a) * horner(wsp,b) >= 0):
        print(horner(wsp,b))
        print("twierdzenie bolzano cauchy'ego nie zostało spełnione")
        return
    while(True):
        # middle point, calc val at f(c)
        c = (a+b)/2
        val = horner(wsp,c)
        #check if done
        if(abs(val) < E):
            print("Result: "+ str(val))
            return
        # check a 
        if(horner(wsp,c) * horner(wsp,a) < 0):
            print(horner(wsp,c))
            b=c
        # check b
        elif(horner(wsp,c) * horner(wsp,b) < 0):
            print(horner(wsp,c))
            a=c
        else:
            print("ERR")
            return
        
wsp = [1,0,1,-1]
bisekcja(wsp,0,1,0.01)