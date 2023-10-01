from caca_coin_random_chooser import *


def welcome(name):
    print(R"""
    Welcome {caca_name}
    ************************************
       _____            _____           
     /  ____|    /\   / ____|     /\    
     | |        /  \  | |        /  \   
     | |       / /\ \ | |       / /\ \  
     | |____  / ____ \| |____  / ____ \ 
      \_____|/_/    \_\\_____|/_/    \_\
    ************************************
    """.format(caca_name=name))


def caca():
    coin_list = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        a = input("please input the {number} coin:".format(number=i + 1))
        coin_list[i] = a
    caca_main = CoinRandomChooser5(roster_file_path="roster.json", coin_list=coin_list)
    output = caca_main.chooser()
    print("Today's lucky dog is {name}!".format(name=output))


if __name__ == '__main__':
    welcome("CACA coin random chooser")

    caca()
    if input("Again?(y/N):") == "Y" or input("Again?(y/N):") == "y":
        caca()
    else:
        print("Bye")
        exit(0)
