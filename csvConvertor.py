"""
A simple scrite useful for switch to Bitwarden from Dashlane by converting the password file to the good format
Author : Floréal RISSO 
"""

import csv
from operator import delitem
from traceback import print_tb
from typing import List



# The original field : 
dash_fields = ["username","username2","username3","title","password","note","url","category","otpSecret"]
# The new field 
bit_fields = ["folder","favorite","type","name","notes","fields","reprompt","login_uri","login_username","login_password","login_totp"]



# The conversion needed : (according to the specification given by the Bitwarden website)
# username(1)-> login_username 9th
# username2(2) -> "username2: second_username" in filds 6th
# username3(3) -> "username3: second_username" in filds 6th
# title(4) -> name 4th 
# password(5) -> login_password 10th 
# note(6) -> notes 5th
# url(7) -> login_uri 8th
# category(8) -> folder 1st 
# otpSecret(9) -> login_totp 11th 
# favorite -> 2nd 
# type -> 3rd (enter login forall)
# reprompt -> 7th 

def idex_conversion(elem : int) -> int:
    """[Convert the field position from Dashlane format to Bitwarden format]

    Args:
        x ([int]): [the field position]

    Returns:
        int: [the new field position]
    """
    return {
        0 : 8,
        1 : 5,
        2 : 5,
        3 : 3,
        4 : 9,
        5 : 4,
        6 : 7,
        7 : 0,
        8 : 10     
    }.get(elem, 9)   

def add_into_line(line : List) -> List:
    """[Create a new line whitch respect the Bitwarden format]

    Args:
        line (List): [A line of the Dashlane format]

    Returns:
        List: [A line of the Bitwarden format]
    """
    other_userlogin = ""
    new_line = [''] * 11
    #new_line[1] = 1 #Create in 2nd column and enter a 1 for any item you want in your Favorites.
    new_line[2] = 'login' # Create in 3rd column and enter login for all items.
    i = 0
    for elem in line:
        new_index : int = idex_conversion(i)
        # A specific traitment...
        if(new_index==5):
            if(elem!=''):
                other_userlogin += "other_username:"+" "+elem+"\n"
        else:
            new_line[new_index]=elem  
        i+=1
    
    if(other_userlogin!=""):
        new_line[5] = other_userlogin
    return new_line


def format_to_bitwarden(dash_filename : str) -> List:
    """[Creat a list with the element at the good place for the bitwarden format]

    Args:
        dash_filename ([str]): [name of the file]

    Returns:
        [List of List]: [a List of List whitch contains all elements]
    """
    bitwarden_lists = [bit_fields];
    with open(dash_filename,newline='') as csvfile:
        print("[Info] : ",dash_filename," opened")
        reader = csv.reader(csvfile)
        reader.__next__()
        for line in reader:
            new_line = add_into_line(line)      
            bitwarden_lists.append(new_line)
        return bitwarden_lists


def debug_print(list : List) :
    for elem in list:
        print(elem,",",end="")
    print("")
    
    
def save_bitwarden_csv(bitwarden_lists : List ,file_name : str = "./bitwarden.csv"): 
    """[Make and save the file create]

    Args:
        bitwarden_lists (List): [The content of the file]
        file_name (str, optional): [The file name]. Defaults to "./bitwarden.csv".
    """
    with open(file_name,"w") as csvfile:
        print("[Info] : ",file_name," created")
        writter = csv.writer(csvfile)
        for line in bitwarden_lists:
            writter.writerow(line)
    

    
def main():
    dash_filename = input("Enter the path of the source _.csv (./credentials.csv by default)") or "./credentials.csv";
    bit_filename = input("Enter the path of the destination _.csv (./bitwarden.csv by default)") or "./bitwarden.csv";
    bitwarden_lists = format_to_bitwarden(dash_filename)
    save_bitwarden_csv(bitwarden_lists,file_name=bit_filename)
    print("[Info] : ",bit_filename,"filled")
        
    


if(__name__=="__main__"):
    main()
