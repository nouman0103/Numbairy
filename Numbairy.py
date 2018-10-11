# Copyright Black Thunder (BT).
hdata = """
# # # # # # # # # # # # # # # # # # 
#   Copyright Black Thunder (BT)  #
# # # # # # # # # # # # # # # # # #

Numbairy:
    "Numbairy" is a new simple programming language made for fun which only consists and work for numbers.
Version : 1.1

Commands:

--} 000  :  exit
--} 001  :  help
--} 002  :  version
--} 003  :  copyright
--} 004  :  clear
--} 123  :  sum
--} 111  :  subtraction
--} 135  :  multiplication
--} 975  :  division
--} 963  :  floor division
--} 010  :  modulus
--} 789  :  power
--}  =   :  used for seperation`
--}  :>  :  bracket (
--}  <:  :  bracket )
--}  >>  :  comment

Usage:

--} numbers should be seperated by `
--} there should be equal(=) sign between each numbers and commands
--} numbers without ` will result in error
--} spaces will be dismissed
--} everything after comment (>>) will be dismissed

Examples:

--} `1`=123=`2`  >> returns 3
--} `2`=123=`2`  >> returns 4
--} :>=:>=`1`=123=`2`=<:=111=`2`=<:=123=`4` >> returns 5 because ((1+2)-2)+4 = 5
--} :>=`2`=123=`2`=<:=135=`3`  >> returns 12 because (2+2)*3 = 12


Examples with comparison:
___________________________________________________
           Numbairy                 |         Real
`1`=123=`2`                         |    1+2
`5`=111=`3`                         |    5-3
`5`=135=`2`                         |    5*2
`2`=789=`2`                         |    2^2
`2`=975=`2`                         |    2/2
`2`=963=`2`                         |    2//2
`3`=010=`2`                         |    3%2
:><:                                |    ()
:>=`2`=<:                           |    (2)
:>=`1`=123=`2`=<:                   |    (1+2)
:>=`1`=111=`2`=<:                   |    (1-2)
:>=:>=`1`=123=`2`=<:=111=`3`=<:     |    ((1+2)-3)
:>=:>=`10`=975=`2`=<:=123=`1`=<:    |    ((10/2)+1)


For bugs or feature-request, please contact me on this repo (https://github.com/BlackThunder01001/numbairy).


"""


import os
os.system("title Numbairy")   #Setting title
os.system("color 70")         #Setting color

import signal
def IKI(signal, frame):       #function to run on keyboardinterrupt
    print("".format(signal))
    return signal.SIG_IGN
signal.signal(signal.SIGINT,IKI)     #registering keyboardinterrupt ignore
from colorama import Fore, Back, Style, init    #syntax-highlighting....
init(autoreset=True)    #initializing colorama
def prin(text,end="\n"):   #function to print colored
    print(Style.DIM + Fore.CYAN + str(text),end=end)     #Dim and Cyan colored text


copyr = "Copyright Black Thunder (BT)."
def start():   #When started
    prin("Numbairy Version 1.1  (For Windows)")
    prin("Type \"001\" for help or \"003\" for copyright.\n")
start()
def prin2(text,end="\n"):    #function to print colored
    print(Style.DIM + Fore.BLUE + str(text),end=end)    #Dim and Cyan colored text

def help():    #help
    prin2(hdata)
def serror(err = ""):   #Syntax error function
    error = "S4nt4x3rr0r"
    error += ": " if err != "" else "!"
    error += err
    print(Fore.RED+error)
inval = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_,}|{;\"'?/[]()!@#$%^&*" #Chars not allowed
def lerror(err = ""):   #Length error
    error = "L3nth3rr0r"
    error += ": " if err != "" else "!"
    error += err
    print(Fore.RED+error)
def isval(w):   #function to check if input string is a number
    if w[0] == "`" and w[-1] == "`" and w.count("`") == 2:return True
    return False
def calc(cm):     #function to calculate an equation
    cm,stop = cm.split("="),False
    cm = [x for x in cm if x]
    for i,c in enumerate(cm):
        if c in bg:cm[i] = bg[c]
        elif isval(c):cm[i] = c[1:-1]
        elif c in "()":pass
        else:serror("Incorrect Usage of '=' !");stop = True;break
    if stop == True:return False
    try:out = eval("".join(cm));prin2(int(out) if int(out) == float(out) else float(out))
    except ZeroDivisionError:print(Fore.RED+"Z3r0D1v1510n3rr0r: division by zero")
    except:serror("Incorrect Usage of '=' !");return False
def funcs(cm,o=False):    #builtin functins
    if cm == "002":prin2("V3R510N V1.1");return 99
    elif cm == "123":prin2("Typ3 <4dd1t10n>");return 99
    elif cm == "111":prin2("Typ3 <5ubtr4ct10n>");return 99
    elif cm == "135":prin2("Typ3 <Mult1pl1c4t10n>");return 99
    elif cm == "975":prin2("Typ3 <D1v1510n>");return 99
    elif cm == "963":prin2("Typ3 <Fl00R-D1v1510n>");return 99
    elif cm == "010":prin2("Typ3 <M0dul0u5>");return 99
    elif cm == "789":prin2("Typ3 <P0W3R>");return 99
    elif cm == "003":prin2(copyr);return 99
    else:
        if c == True:return 123
    return True

bg = {",":" ","123":"+","111":"-","135":"*","975":"/","963":"//","010":"%","789":"**"}   #Chars with background
while True:
    try:prin("--> ",end="");cm = input().replace(" ","")  #Taking command
    except:continue
    try:cm = cm[0:cm.index('>>')]   #removing everything after comment
    except:pass
    if cm == "":continue
    if len(cm) <= 2:lerror("Command Length too short!");continue
    if True:
        stop = False
        for c in cm:
            if c in inval:serror("Unknown Characters used!");stop = True;break
        if stop == True:stop = False;continue
    if cm == "004":os.system("cls");start();continue
    if isval(cm):prin2(cm[1:-1])
    elif funcs(cm) == 99:continue
    elif cm == "000":break
    elif cm == "001":help()
    elif ":>" in cm:   #If brackets are used
        if (cm.count(":>")+cm.count("<:")) % 2 == 1:serror("Incorrect usage of \"<:>\" !");continue
        cm = cm.replace(":>","(").replace("<:",")")
        if "=" in cm:calc(cm)
        else:
            try:
                if funcs(cm.replace("(","").replace(")",""),True) == 123:raise Exception
            except:
                try:
                    if isval(cm.replace("(","").replace(")","")):prin2(cm.replace("(","").replace(")","")[1:-1])
                    else:raise Exception
                except:
                    serror("Unknown Command!")
                    continue
    elif "=" in cm:calc(cm)   #if =s are used
    else:serror("Unknown Command!")
