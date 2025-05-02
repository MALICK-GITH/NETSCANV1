import os
import subprocess
import shutil

RED = "\033[1;91m"
GREEN = "\033[1;92m"
BLUE = "\033[1;94m"
CYAN = "\033[1;96m"
YELLOW = "\033[1;93m"
MAGENTA = "\033[1;95m"
RESET = "\033[0m"

logo = f"""{MAGENTA}
  _    _    ___     _____  _  __
 | |  | |  / _ \   / ____|| |/ /
 | |__| | | | | | | |     | ' / 
 |  __  | | |_| | | |____ | . \ 
 |_|  |_|  \___/   \_____||_|\_\\
{RESET}"""

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def banner():
    print(f"{RED}╔══════════════════════════════════════════════╗")
    print(f"{GREEN}║        SOLITAIRE HACK NETWORK SCAN           ║")
    print(f"{RED}╚══════════════════════════════════════════════╝{RESET}")

def check_nmap():
    if shutil.which("nmap") is None:
        print(f"{RED}[!] Nmap n'est pas installé. Utilise : pkg install nmap{RESET}")
        return False
    return True

def execute_nmap(command):
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        print(f"{GREEN}{result}{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{RED}[!] Erreur Nmap :\n{e.output}{RESET}")
    input(f"{MAGENTA}\nAppuie sur Entrée pour continuer...{RESET}")

def apropos():
    clear()
    print(f"{RED}╔══════════════════════════════════════════════╗")
    print(f"{GREEN}║              À PROPOS DE L'OUTIL             ║")
    print(f"{RED}╚══════════════════════════════════════════════╝{RESET}")
    print(f"""
Nom de l'outil : {GREEN}SOLITAIRE HACK NETWORK SCAN{RESET}
Développé pour : {GREEN}utilisation sur Termux sans root{RESET}
Langage        : Python
Utilisation    : Interface simplifiée de Nmap

Créé par       : {CYAN}SOLITAIRE HACK{RESET}
Contact        : {BLUE}+2250500448208{RESET}, {BLUE}+2250501945735{RESET}
""")
    input(f"{MAGENTA}Appuie sur Entrée pour revenir au menu...{RESET}")

def manuel():
    clear()
    print(f"{RED}╔══════════════════════════════════════════════╗")
    print(f"{GREEN}║         MANUEL : SOLITAIRE HACK TOOL         ║")
    print(f"{RED}╚══════════════════════════════════════════════╝{RESET}")
    print(f"""
{YELLOW}1. PRÉREQUIS{RESET}
- Python : pkg install python -y
- Nmap   : pkg install nmap -y
- Lancer : python solitaire_hack_nmap.py

{YELLOW}2. FONCTIONS DU MENU{RESET}
 1. Scan rapide (-F)
 2. Scan complet (-p-)
 3. Détection de version (-sV)
 4. Scan avec script NSE (--script)
 5. Scan UDP (-sU)
 6. Scan avec traceroute (--traceroute)
 7. À propos
 8. Quitter

{YELLOW}3. EXEMPLES{RESET}
- Option 1 : google.com
- Option 4 : script=default, cible=scanme.nmap.org

{YELLOW}4. CONSEILS{RESET}
- Utiliser sur des cibles autorisées
- Scanner depuis Wi-Fi pour de meilleurs résultats
- Pas besoin de root !

{GREEN}Développé par : SOLITAIRE HACK{RESET}
{BLUE}Contact : +2250500448208 / +2250501945735{RESET}
""")
    input(f"{MAGENTA}Appuie sur Entrée pour revenir au menu...{RESET}")

def menu():
    while True:
        clear()
        print(logo)
        banner()
        print(f"{CYAN}1.{RESET} Scan rapide (-F)")
        print(f"{CYAN}2.{RESET} Scan complet (-p-)")
        print(f"{CYAN}3.{RESET} Détection de version (-sV)")
        print(f"{CYAN}4.{RESET} Scan avec scripts NSE (--script)")
        print(f"{CYAN}5.{RESET} Scan UDP (-sU)")
        print(f"{CYAN}6.{RESET} Scan avec traceroute (--traceroute)")
        print(f"{CYAN}7.{RESET} À propos")
        print(f"{CYAN}8.{RESET} Quitter")
        print(f"{CYAN}9.{RESET} Manuel d'utilisation")
        choix = input(f"\n{BLUE}Sélectionne une option : {RESET}")

        if not check_nmap():
            input(f"{MAGENTA}\nAppuie sur Entrée pour continuer...{RESET}")
            continue

        if choix in ["1", "2", "3", "4", "5", "6"]:
            cible = input("Cible (ex: site.com ou IP) : ")

        if choix == "1":
            execute_nmap(["nmap", "-F", cible])
        elif choix == "2":
            execute_nmap(["nmap", "-p-", cible])
        elif choix == "3":
            execute_nmap(["nmap", "-sV", cible])
        elif choix == "4":
            script = input("Nom du script NSE (ex: default, vuln) : ")
            execute_nmap(["nmap", "--script", script, cible])
        elif choix == "5":
            execute_nmap(["nmap", "-sU", cible])
        elif choix == "6":
            execute_nmap(["nmap", "--traceroute", cible])
        elif choix == "7":
            apropos()
        elif choix == "8":
            print("À bientôt !")
            break
        elif choix == "9":
            manuel()
        else:
            print(f"{RED}[!] Option invalide.{RESET}")
            input(f"{MAGENTA}\nAppuie sur Entrée pour continuer...{RESET}")

if __name__ == "__main__":
    menu()