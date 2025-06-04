from mouse import get_position as mouse_get_pos, move as mouse_move
from keyboard import wait
import colorama
from colorama import Back, Fore

colorama.init(autoreset=True)

COLORS = {
    "important" : Fore.LIGHTRED_EX,
    "highlight" : Fore.BLACK + Back.WHITE
    }

OUTPUTS = [
f"""{COLORS['important']}Initialization...{Fore.RESET}
Please move your mouse to the {COLORS['important']}BOTTOM_LEFT{Fore.RESET} corner
And Press {COLORS['highlight']}-Ctrl+F12-{Fore.RESET + Back.RESET} to continue.\n""",

f"""{COLORS['important']}Initialization...{Fore.RESET}
Set the steering wheel in the {COLORS['important']}middle{Fore.RESET}
And Press {COLORS['highlight']}-Ctrl+F12-{Fore.RESET + Back.RESET} to continue.\n""",

f"""Choose the version {COLORS['highlight']}(enter only a number){Fore.RESET + Back.RESET}
   1.V1 {COLORS['important']}( X axis Steering | Z axis +50% Throttle | Z axis -50% Break )
Or{Fore.RESET} 5.QUIT Application.\n""",

f"""{COLORS['important']}Invalid version selected.{Fore.RESET}\n""",

f"""{COLORS['important']}Initialization Done.{Fore.RESET} Press {COLORS['highlight']}-Ctrl+F12-{Fore.RESET + Back.RESET} to start Emulating.\n""",

f"""{COLORS['important']}Steering Wheel Emulating...{Fore.RESET}\n""",

f"""{COLORS['important']}Exiting Emulation...{Fore.RESET}\n"""
]

try:
    print(OUTPUTS[0])
    wait("ctrl+f12")
    MaxMouseRng = mouse_get_pos()

    mouse_Center = (MaxMouseRng[0]//2,MaxMouseRng[1]//2)
    #print(mouse_Center)

    print(OUTPUTS[1])
    wait("ctrl+f12")
    mouse_move(mouse_Center[0], mouse_Center[1], absolute=True) #reset the mouse cusor to the center
    while True:
        version = input(OUTPUTS[2])
        match version:
            case "1":
                from Versions import v1 as code
            
            case '5':
                exit()

            case _:
                print(OUTPUTS[3])
                continue
        
        print(OUTPUTS[4])
        wait("ctrl+f12")
        
        try:
            print(OUTPUTS[5])
            code.Main()
        except KeyboardInterrupt:
            code.VjoyReset_input()
            print(OUTPUTS[6]) #reset the inputs to nutural values on KeyboardInterrupt s .

except KeyboardInterrupt:
    quit()
