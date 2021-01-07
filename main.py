import sys
from os import system, name
from tqdm import tqdm
from colorama import Fore, Back, Style


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def is_armstrong_number(number):
    temp = 0
    NumberLength = len(str(number))

    for n in str(number):
        temp += pow(int(n), NumberLength)

    return (temp == number)


def main():
    clear()

    print(Fore.GREEN, Style.BRIGHT,"""
    
                                  _                                                 _               
         /\                      | |                                               | |              
        /  \   _ __ _ __ ___  ___| |_ _ __ ___  _ __   __ _   _ __  _   _ _ __ ___ | |__   ___ _ __ 
       / /\ \ | '__| '_ ` _ \/ __| __| '__/ _ \| '_ \ / _` | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
      / ____ \| |  | | | | | \__ \ |_| | | (_) | | | | (_| | | | | | |_| | | | | | | |_) |  __/ |   
     /_/    \_\_|  |_| |_| |_|___/\__|_|  \___/|_| |_|\__, | |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                       __/ |                                        
                                                      |___/                                                                          
    """)
    print(Fore.BLUE,"""
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    For example:
    
    9 is an Armstrong number, because 9 = 9^1 = 9
    10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
    153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    
    For more information on this subject, refer to the following link:
    https://en.wikipedia.org/wiki/Narcissistic_number


    """, Style.RESET_ALL)
    armstrongs = []
    t = 0
    try:
        rangeNumber = int(sys.argv[1])
        for i in tqdm(range(rangeNumber)):
            if is_armstrong_number(i):
                armstrongs.append(i)

        print(f"\nThere are {Fore.GREEN + str(len(armstrongs))}  {Style.RESET_ALL} Armstrongs in the range of 0 to {Fore.GREEN + str(rangeNumber)}{Style.RESET_ALL}.\n")
        print(armstrongs)
        print("\n")



    except IndexError:
        print(Fore.RED, 'You must provide a number as input to the command line!\n', Style.RESET_ALL)
        sys.exit(1)
    except ValueError:
        print(f"{Fore.RED}Input must be an int, no {Fore.YELLOW + sys.argv[1]}\n", Style.RESET_ALL)
        sys.exit(1)


if __name__ == '__main__':
    main()
