#!/usr/bin/env/python3
import time
import os
import random
import subprocess
from passwordmeter import test



def menu():
    mainBanner()
    print("\t\t\033[1;34m[+] 1.\tCreate a Strong Password (Automatically)\033[1;m")
    print("\t\t\033[1;34m[+] 2.\tCreate a WordList\033[1;m")
    print("\t\t\033[1;34m[+] 3.\tAbbreviation a Big Wordlist which Has More Than (15GB) Of Size!\033[1;m")
    print("\t\t\033[1;34m[+]\033[1;m \033[1;91m0.\tExit!\033[1;m")

def mainBanner():
    print("""
  sSSs  .S   S.          sSSs    sSSs_sSSs     .S_sSSs      sSSs    sSSs_sSSs    S.        sSSs  
 d%%SP .SS   SS.        d%%SP   d%%SP~YS%%b   .SS~YS%%b    d%%SP   d%%SP~YS%%b   SS.      d%%SP  
d%S'   S%S   S%S       d%S'    d%S'     `S%b  S%S   `S%b  d%S'    d%S'     `S%b  S%S     d%S'    
S%S    S%S   S%S       S%S     S%S       S%S  S%S    S%S  S%|     S%S       S%S  S%S     S%S     
S&S    S%S   S%S       S&S     S&S       S&S  S%S    S&S  S&S     S&S       S&S  S&S     S&S     
S&S_Ss  SS   SS        S&S     S&S       S&S  S&S    S&S  Y&Ss    S&S       S&S  S&S     S&S_Ss  
S&S~SP   S   S         S&S     S&S       S&S  S&S    S&S  `S&&S   S&S       S&S  S&S     S&S~SP  
S&S       SSS          S&S     S&S       S&S  S&S    S&S    `S*S  S&S       S&S  S&S     S&S     
S*b       S*S          S*b     S*b       d*S  S*S    S*S     l*S  S*b       d*S  S*b     S*b     
S*S.      S*S          S*S.    S*S.     .S*S  S*S    S*S    .S*P  S*S.     .S*S  S*S.    S*S.    
 SSSbs    S*S           SSSbs   SSSbs_sdSSS   S*S    S*S  sSS*S    SSSbs_sdSSS    SSSbs   SSSbs  
  YSSP    S*S            YSSP    YSSP~YSSY    S*S    SSS  YSS'      YSSP~YSSY      YSSP    YSSP  
          SP                                  SP                                                 
          Y                                   Y                                                  
                                                                                                 
                                                                                                 
                            ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 @𝕖𝕙𝕤𝟜𝕟𝕟𝕟 & @𝕪𝟜𝕙𝕪𝕒𝟘𝟘
                            𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻𝓼 𝓣𝓮𝓪𝓶: 𝓢𝓬𝓸𝓻𝓹𝓲𝓸𝓷 𝓢𝓱𝓲𝓮𝓵𝓭
    """)

def banner1():
    print("""
██████╗  █████╗ ███████╗███████╗       ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔════╝      ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝███████║███████╗███████╗█████╗██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║╚════╝██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║     ██║  ██║███████║███████║      ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝       ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                                                                                                      
                                    ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 @𝕖𝕙𝕤𝟜𝕟𝕟𝕟 & @𝕪𝟜𝕙𝕪𝕒𝟘𝟘
                                    𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻𝓼 𝓣𝓮𝓪𝓶: 𝓢𝓬𝓸𝓻𝓹𝓲𝓸𝓷 𝓢𝓱𝓲𝓮𝓵𝓭
""")


def banner3():
    print("""
                                                                                                                              
@@@  @@@  @@@  @@@                   @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@@@@   @@@@@@@   
@@@  @@@  @@@  @@@                  @@@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@!  @@!  @@!                  !@@        @@!       @@!@!@@@  @@!       @@!  @@@  @@!  @@@    @@!    @@!  @@@  @@!  @@@  
!@!  !@!  !@!  !@!                  !@!        !@!       !@!!@!@!  !@!       !@!  @!@  !@!  @!@    !@!    !@!  @!@  !@!  @!@  
@!!  !!@  @!@  @!!       @!@!@!@!@  !@! @!@!@  @!!!:!    @!@ !!@!  @!!!:!    @!@!!@!   @!@!@!@!    @!!    @!@  !@!  @!@!!@!   
!@!  !!!  !@!  !!!       !!!@!@!!!  !!! !!@!!  !!!!!:    !@!  !!!  !!!!!:    !!@!@!    !!!@!!!!    !!!    !@!  !!!  !!@!@!    
!!:  !!:  !!:  !!:                  :!!   !!:  !!:       !!:  !!!  !!:       !!: :!!   !!:  !!!    !!:    !!:  !!!  !!: :!!   
:!:  :!:  :!:   :!:                 :!:   !::  :!:       :!:  !:!  :!:       :!:  !:!  :!:  !:!    :!:    :!:  !:!  :!:  !:!  
 :::: :: :::    :: ::::              ::: ::::   :: ::::   ::   ::   :: ::::  ::   :::  ::   :::     ::    ::::: ::  ::   :::  
  :: :  : :    : :: : :              :: :: :   : :: ::   ::    :   : :: ::    :   : :   :   : :     :      : :  :    :   : :  
                                                                                                                              
                                    ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 @𝕖𝕙𝕤𝟜𝕟𝕟𝕟 & @𝕪𝟜𝕙𝕪𝕒𝟘𝟘
                                    𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻𝓼 𝓣𝓮𝓪𝓶: 𝓢𝓬𝓸𝓻𝓹𝓲𝓸𝓷 𝓢𝓱𝓲𝓮𝓵𝓭
    """)

def banner2():
    print("""
 ▄█     █▄   ▄█        ▄████████    ▄████████    ▄████████    ▄████████     ███      ▄██████▄     ▄████████ 
███     ███ ███       ███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄ ███    ███   ███    ███ 
███     ███ ███       ███    █▀    ███    ███   ███    █▀    ███    ███    ▀███▀▀██ ███    ███   ███    ███ 
███     ███ ███       ███         ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
███     ███ ███       ███        ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   
███     ███ ███       ███    █▄  ▀███████████   ███    █▄    ███    ███     ███     ███    ███ ▀███████████ 
███ ▄█▄ ███ ███▌    ▄ ███    ███   ███    ███   ███    ███   ███    ███     ███     ███    ███   ███    ███ 
 ▀███▀███▀  █████▄▄██ ████████▀    ███    ███   ██████████   ███    █▀     ▄████▀    ▀██████▀    ███    ███ 
            ▀                      ███    ███                                                    ███    ███ 
            
                                     ℂ𝕣𝕖𝕒𝕥𝕖𝕕 𝔹𝕪 @𝕖𝕙𝕤𝟜𝕟𝕟𝕟 & @𝕪𝟜𝕙𝕪𝕒𝟘𝟘
                                    𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻𝓼 𝓣𝓮𝓪𝓶: 𝓢𝓬𝓸𝓻𝓹𝓲𝓸𝓷 𝓢𝓱𝓲𝓮𝓵𝓭
    """)


def crunch_wl_gen():
    print("""
  ____                       _      __        ___           ____            
 / ___|_ __ _   _ _ __   ___| |__   \ \      / / |         / ___| ___ _ __  
| |   | '__| | | | '_ \ / __| '_ \   \ \ /\ / /| |   _____| |  _ / _ \ '_ \ 
| |___| |  | |_| | | | | (__| | | |   \ V  V / | |__|_____| |_| |  __/ | | |
 \____|_|   \__,_|_| |_|\___|_| |_|    \_/\_/  |_____|     \____|\___|_| |_|

    """)

def wl_options():
    print("\t\t\033[1;34m[+] 1.\tCreate a Wordlist With [Crunch] - Linux\033[1;m")
    print("\t\t\033[1;34m[+] 2.\tCreate a WordList Manually With [EY Console]\033[1;m")
    print("\t\t\033[1;34m[+]\033[1;m \033[1;91m0.\tBack!\033[1;m")

def strong_pass_options():
    print("\t\t\033[1;34m[+] 1.\tCreate a Strong Password (Manually With Your Info With Random Special Chars!)\033[1;m")
    print("\t\t\033[1;34m[+] 2.\tCreate a Strong Password (Automatically With External Words File!)\033[1;m")
    print("\t\t\033[1;34m[+]\033[1;m \033[1;91m0.\tBack!\033[1;m")
def CLS():
    if os == "nt":
        os.system("cls")
    else:
        os.system("reset")

def BigFun():
    choice = ("1")
    CLS()
    while choice != ("0"):
        try:
            menu()
            choice = input("\n\n\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Enter Your Choice:\u001b[37m ")
        except KeyboardInterrupt:
            print("\n\n\t\tPlease Wait For 3 Seconds...")
            time.sleep(3)
            print("\n\n\t\t\tGood By :)")
            exit()


        if choice == ("1"):
            CLS()
            choice_type = ("1")
            while choice_type != ("0"):
                try:
                    banner1()
                    strong_pass_options()
                    choice_type = input("\n\n\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Enter Your Choice:\u001b[37m ")
                except KeyboardInterrupt:
                    print("\n\n\t\tPlease Wait For 3 Seconds...")
                    time.sleep(3)
                    print("\n\n\t\t\tGood By :)")
                    exit()
                if choice_type == ("1"):
                    try:
                        CLS()
                        banner1()
                        ehsan = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Type The Number Of Password Size: ")
                        longer = int(ehsan)
                        name = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Type Your Name To Make A Pass With:\u001b[37m ")
                        print("\u001b[37m[i] Starting time: %s \u001b[37m" % time.strftime('\u001b[34;1m[%H:%M:%S]\u001b[34;1m'))
                        time.sleep(4)
                        char = "`!?$?%^&*()_-+={[}]:;@'~#|\<,>.?/"
                        number = "1234567890"
                        Alfabet = "AaBbCcDdEefFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
                        marge = char + name + number + Alfabet
                        create_pass = [random.choice(marge) for word in range(longer)]
                        passwis = "".join(create_pass)
                        time.sleep(3)
                        print("\n\u001b[m➡️ Your Password Is:\u001b[m " + "\u001b[37m" + str(passwis))
                        print('\n\u001b[37m[i] End time: %s\u001b[37m' % time.strftime('\u001b[34;1m[%H:%M:%S]\u001b[34;1m'))
                        time.sleep(1)
                        print("\n\t\t\t\u001b[32m[◉] This Password Is Protect Your Social Accounts Of Cyber Attacks!\u001b[32m")
                        input("\n\n\t\t\t\t\t\033[1;34m▶️ Completed, click return to go back")
                        CLS()
                    except KeyboardInterrupt:
                        print("\n\n\t\t\t\t\t\tPlease Wait For 3 Seconds...")
                        time.sleep(3)
                        CLS()
                        print("\n\t\t\t\033[1;34m[+]\033[1;m \033[1;91mUser KeyboardInterrupt(CTRL+C) Exception!\033[1;m ")
                elif choice_type == ("2"):
                    try:
                        CLS()
                        banner1()
                        words = open('words.txt', 'r').read().split("\n")
                        special_chars = ['?', '!', '@', '#', '%', '*', '^', '$', '&']

                        def create_password(num_words=5, num_numbers=4, num_special=5):
                            password_str = ""

                            for _ in range(num_words) and range(num_numbers) and range(num_special):
                                password_str += random.choice(words).lower().capitalize()
                                password_str += str(random.randint(0, 9))
                                password_str += random.choice(special_chars)
                            print("\u001b[37m[i] Starting time: %s \u001b[37m" % time.strftime('\u001b[34;1m[%H:%M:%S]\u001b[34;1m'))
                            time.sleep(3)
                            return password_str

                        def main():
                            password_str = create_password()
                            strength, _ = test(password_str)

                            print("\n\n\u001b[37m➡️ Your Password: %s \u001b[37m" % password_str)
                            print("\u001b[37m➡️ Strength Of A Computer To Crack This Password:\u001b[37m %0.5f" % strength + " \033[1;34m{OK Not So Bad}\033[1;m")
                            time.sleep(3)
                            print('\n\u001b[37m[i] End time: %s\u001b[37m' % time.strftime('\u001b[34;1m[%H:%M:%S]\u001b[34;1m'))
                            print("\n\n\t\t\u001b[32m[◉] Be Carefull It's Not Mean You're Protected! Use The First Option To Create Your Password.\u001b[32m")
                            input("\n\n\t\t\t\t\t\033[1;34m▶️ Completed, click return to go back")
                            CLS()
                        if __name__ == "__main__":
                            main()
                    except KeyboardInterrupt:
                        print("\n\n\t\t\t\t\t\tPlease Wait For 3 Seconds...")
                        time.sleep(3)
                        CLS()
                        print("\n\t\t\t\033[1;34m[+]\033[1;m \033[1;91mUser KeyboardInterrupt(CTRL+C) Exception!\033[1;m ")

                elif choice_type == ("0"):
                    try:
                        print("\n\n\t\tPlease Wait For 2 Second...")
                        time.sleep(2)
                        CLS()
                    except KeyboardInterrupt:
                        print("\n\n\t\t\t\t\t\tPlease Wait For 3 Seconds...")
                        time.sleep(3)
                        CLS()
                        print("\n\t\t\t\033[1;34m[+]\033[1;m \033[1;91mUser KeyboardInterrupt(CTRL+C) Exception!\033[1;m ")

        elif choice == ("2"):
            CLS()
            banner2()
            choicess = ("1")
            while choicess != ("0"):
                try:
                    wl_options()
                    choicess = input("\n\n\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Enter Your Choice:\u001b[37m ")
                except KeyboardInterrupt:
                    print("\n\n\t\tPlease Wait For 3 Seconds...")
                    time.sleep(3)
                    print("\n\n\t\t\tGood By :)")
                    exit()
                if choicess == ("1"):
                    CLS()
                    try:
                        print("\033[1;91mInstalling The Crunch Tool...\033[1;m")
                        subprocess.call(["sudo", "apt-get", "install", "crunch"])
                        time.sleep(2)
                        CLS()
                        crunch_wl_gen()
                        charsss = input("\n\n\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Type Some Special Chareckters:\u001b[37m ")
                        fname = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# First Name:\u001b[37m ")
                        lname = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Last Name:\u001b[37m ")
                        age = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Age:\u001b[37m ")
                        min_len = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Min Length:\u001b[37m ")
                        max_len = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Max Length:\u001b[37m ")
                        create_password_A = fname + lname + charsss + age
                        randomly_create = [random.choice(create_password_A) for x in create_password_A]
                        joiner_A = "".join(randomly_create)
                        wordlist_name = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Type The Name Of The Output File With (.txt) extension:\u001b[37m ")
                        subprocess.call(["sudo", "crunch", min_len, max_len, joiner_A, "-o", wordlist_name])
                        input("\n\n\t\t\t\t\t\033[1;34m▶️ Completed, click return to go back")
                        CLS()
                        banner2()
                    except KeyboardInterrupt:
                        print("\n\n\t\t\t\t\t\tPlease Wait For 3 Seconds...")
                        time.sleep(3)
                        CLS()
                        banner2()
                        print("\n\t\t\t\t\033[1;34m[+]\033[1;m \033[1;91mUser KeyboardInterrupt(CTRL+C) Exception!\033[1;m \n\n")
                elif choicess == ("2"):
                    try:
                        CLS()
                        print("\n\n\n\n\n\t\t\t\t\tThis Option Doesn't Available Right Now But It Will Be In Future :)")
                        input("\n\n\t\t\t\t\t\t\t\033[1;34m▶️ Completed, click return to go back")
                        CLS()
                        banner2()
                    except KeyboardInterrupt:
                        print("\n\n\t\t\t\t\t\t\t\tPlease Wait For 3 Seconds...")
                        time.sleep(3)
                        CLS()
                        banner2()
                        print("\n\t\t\t\t\033[1;34m[+]\033[1;m \033[1;91mUser KeyboardInterrupt(CTRL+C) Exception!\033[1;m \n\n")
                elif choicess == ("0"):
                    try:
                        print("\n\n\t\tPlease Wait For 2 Second...")
                        time.sleep(2)
                        CLS()
                    except KeyboardInterrupt:
                        print("\n\n\t\t\t\t\t\tPlease Wait For 3 Seconds...")
                        time.sleep(3)
                        CLS()
                        print("\n\t\t\t\033[1;34m[+]\033[1;m \033[1;91mUser KeyboardInterrupt(CTRL+C) Exception!\033[1;m ")

        elif choice == ("3"):
            try:
                CLS()
                banner3()
                print("""
                \n\n\t\t\t\u001b[37m[i] Note: This Option Is Using For Abbreviation a Big Wordlist 
                \n\t\t\t Which Has a 15GB - 1TB - 1PB size! To Make it Easy To Run And To Protect Your Computer To Be Crush\u001b[37m"
                """)
                wordlistok = input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# Type The Wordlist (Name) or (Location): \u001b[37m")
                lines_per_file = int(input("\033[1;91mroot@TheXerr0r\033[1;m\u001b[37m:~# How Many Lines Do You Want To Copy? \u001b[37m"))
                smallfile = None
                print("\u001b[37m[i] Starting Time: %s \u001b[37m" % time.strftime('\u001b[34;1m[%H:%M:%S]\u001b[34;1m'))
                time.sleep(4)
                with open(wordlistok, 'r') as bigfile:
                    for lineno, line in enumerate(bigfile):
                        if lineno % lines_per_file == 0:
                            if smallfile:
                                smallfile.close()
                            small_filename = 'Small_File_{}.txt'.format(lineno + lines_per_file)
                            smallfile = open(small_filename, "w")
                        smallfile.write(line)
                    if smallfile:
                        smallfile.close()
                        time.sleep(5)
                        print("The Big File Is Shorted Successfully :)")
                        print('\n\u001b[37m[i] End time: %s\u001b[37m' % time.strftime('\u001b[34;1m[%H:%M:%S]\u001b[34;1m'))
                        time.sleep(1)
                input("\n\n\t\t\t\t\t\033[1;34m       ▶️ Completed, click return to go back")
                CLS()
            except KeyboardInterrupt:
                print("\n\n\t\t\t\t\t\tPlease Wait For 3 Seconds...")
                time.sleep(3)
                CLS()
                print("\n\t\t\t\033[1;34m[+]\033[1;m \033[1;91mUser KeyboardInterrupt(CTRL+C) Exception!\033[1;m ")

        elif choice == ("0"):
            print("\n\n\t\tPlease Wait For 4 Second...")
            time.sleep(4)
            print("\n\n\n\t\t\tGood By :)")

if __name__ == "__main__":
    BigFun()
