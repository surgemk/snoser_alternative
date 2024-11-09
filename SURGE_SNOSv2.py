import pystyle
from pystyle import *
#from colorama import init, Fore
import os
import platform
import subprocess
#init()

def clear_console():
    os_name = platform.system()
    if os_name == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

themes = {
    'Радуга': Colors.rainbow,
    'Зеленый_к_красному': Colors.green_to_red,
    'Зеленый_к_черному': Colors.green_to_black,
    'Зеленый_к_голубому': Colors.green_to_cyan,
    'Зеленый_к_желтому': Colors.green_to_yellow,
    'Зеленый_к_белому': Colors.green_to_white,
    'Зеленый_к_синему': Colors.green_to_blue,
    'Красный_к_синему': Colors.red_to_blue,
    'Красный_к_зеленому': Colors.red_to_green,
    'Красный_к_черному': Colors.red_to_black,
    'Красный_к_желтому': Colors.red_to_yellow,
    'Красный_к_белому': Colors.red_to_white,
    'Красный_к_фиолетовому': Colors.red_to_purple,
    'Синий_к_зеленому': Colors.blue_to_green,
    'Синий_к_белому': Colors.blue_to_white,
    'Синий_к_красному': Colors.blue_to_red,
    'Синий_к_черному': Colors.blue_to_black,
    'Синий_к_фиолетовому': Colors.blue_to_purple,
    'Синий_к_голубому [По умолчанию]': Colors.blue_to_cyan,
}


def select_theme():
    clear_console()
    global current_theme
    clear_console()
    Write.Print("Выберите тему:\n", Colors.green, interval=0.001)
    for idx, (theme, color) in enumerate(themes.items(), 1):
        theme_line = f"{idx}. {theme}"
        if theme == 'Радуга':
            Write.Print(theme_line + "\n", Colors.rainbow, interval=0.001)
        else:
            Write.Print(theme_line + "\n", color, interval=0.001)
    try:
        choice = int(input("Введите номер темы: "))
        if 1 <= choice <= len(themes):
            current_theme = list(themes.values())[choice - 1]
            return current_theme
        else:
            Write.Print("Неверный номер темы. Попробуйте снова.\n", Colors.red, interval=0.001)
            return select_theme()
    except ValueError:
        Write.Print("Пожалуйста, введите число.\n", Colors.red, interval=0.001)
        return select_theme()
    
theme = select_theme()

script_path = os.path.join(os.path.dirname(__file__), 'ass.install.py')
subprocess.run(['python', script_path])

intro = '''



╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃
┃╰━━┳╮╭┳━┳━━┳━━╮┃╰━━┳━╮╭━━┳━━╮╭╮╭╋╯╭╯┃
╰━━╮┃┃┃┃╭┫╭╮┃┃━┫╰━━╮┃╭╮┫╭╮┃━━┫┃╰╯┣━╯╭╯
┃╰━╯┃╰╯┃┃┃╰╯┃┃━┫┃╰━╯┃┃┃┃╰╯┣━━┃╰╮╭┫┃╰━╮
╰━━━┻━━┻╯╰━╮┣━━╯╰━━━┻╯╰┻━━┻━━╯╱╰╯╰━━━╯
╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╰━━╯
                                           
нажми enter  чтобы продолжить!              

                                                                                                 
'''

Anime.Fade(Center.Center(intro), Colors.blue_to_cyan, Colorate.Vertical, interval=0.045, enter=True)

clear_console()
while True:
    select_theme()
    clear_console()
    intw = '''





████████████████████████▀███████
█─▄▄▄▄█▄─██─▄█▄─▄▄▀█─▄▄▄▄█▄─▄▄─█
█▄▄▄▄─██─██─███─▄─▄█─██▄─██─▄█▀█
▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
███████████████████████████████████████
█─▄▄▄▄█▄─▀█▄─▄█─▄▄─█─▄▄▄▄███▄─█─▄█▀▄▄▀█
█▄▄▄▄─██─█▄▀─██─██─█▄▄▄▄─████▄▀▄███▀▄██
▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▀▀▀▀▄▀▀▀▄▄▄▄▀
                                                          
                 VERSION - 2.0.2
              CREATED BY @SURGEEBET
                    PRICE - ?
         Слил без разрешения? - Мать шлюха
                                         
   ┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐ 
   │    1 |  Снос АККАУНТА     │      │     2 |  Снос КАНАЛА      │      │       3 | Снос БОТА       │
   └───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘                     
    '''
    Write.Print(Center.XCenter(intw), theme, interval=0.0000006)
    Asshole = pystyle.Write.Input("\nChoice > ", Colors.blue_to_cyan, interval = 0.001)
    if Asshole == '1':
        script_path = os.path.join(os.path.dirname(__file__), 'SURGE_AKAUNT.py')
        subprocess.run(['python', script_path])
    elif Asshole == '2':
        script_path = os.path.join(os.path.dirname(__file__), 'SURGETGK.py')
        subprocess.run(['python', script_path])
    elif Asshole == '3':
        script_path = os.path.join(os.path.dirname(__file__), 'SURGEBOT.py')
        subprocess.run(['python', script_path])
    elif Asshole == '4':
        select_theme()
