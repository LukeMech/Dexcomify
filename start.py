import os, sys, platform
script_dir=os.path.dirname(os.path.realpath(__file__))

try: from colorama import init, Fore, Style
except: 
    os.system('pip install colorama')
    os.system(F'python {script_dir}/start.py')

quiet=False
if len(sys.argv) > 1:
    if sys.argv[1] == 'quiet': quiet=True

init()
print()
infoMsg = Fore.GREEN + "[LAUNCH] " + Style.RESET_ALL
warningMsg = Fore.YELLOW + "[LAUNCH] " + Style.RESET_ALL
startscriptMsg = Fore.YELLOW + "--------------------" + Style.RESET_ALL
endScriptMsg = Fore.BLUE + "--------------------" + Style.RESET_ALL

print(infoMsg + "Tak będą wyglądać informacje,")
print(Fore.YELLOW + "[LAUNCH]" + Style.RESET_ALL + " tak ostrzeżenia,")
print(Fore.RED + "[LAUNCH]" + Style.RESET_ALL + " a tak błędy.")
print()

# Update

print(infoMsg + "Aktualizowanie kodu używając polecenia " + Fore.YELLOW + "git pull")
print(startscriptMsg)
try: os.system(F'cd {script_dir}&& git pull')
except: print(warningMsg + "Aktualizowanie kodu nieudane - git niewykryty")
print(endScriptMsg)
print()

print(infoMsg + "Aktualizowanie bibliotek używając polecenia " + Fore.YELLOW + "pip install -U")
print(startscriptMsg)
os.system("pip install -r requirements.txt -U")
print(endScriptMsg)
print()

# Run
if quiet:
    print(infoMsg + "Uruchamianie programu" + Fore.RED + " w tle" + Style.RESET_ALL + " - " + Fore.YELLOW + "main.py")
    if platform.system() == 'Windows': pass# os.system(F'setsid python {script_dir}/app/main.py >nul 2>&1 < nul &')
    else: os.system(F'setsid python {script_dir}/app/main.py >/dev/null 2>&1 < /dev/null &')
 
else: 
    print(infoMsg + "Uruchamianie programu - " + Fore.YELLOW + "main.py" + Style.RESET_ALL + " - użyj " + Fore.RED + "Ctrl + C" + Style.RESET_ALL + ", aby zakończyć.") 
    print(startscriptMsg)

    if platform.system() == 'Windows': os.system(F'python {script_dir}/app/main.py 2> nul')
    else: os.system(F'python {script_dir}/app/main.py 2> /dev/null')
    print(endScriptMsg)