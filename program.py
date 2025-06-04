from mouse import get_position as mouse_get_pos, move as mouse_move
from keyboard import wait
import colorama
from colorama import Back, Fore

colorama.init(autoreset=True)

OUTPUTS = [
f"""{Fore.RED}Initialization...{Fore.RESET}
Please move your mouse to the {Fore.RED}BOTTOM_LEFT{Fore.RESET} corner
And Press {Fore.BLACK + Back.WHITE}-Ctrl+F12-{Fore.RESET + Back.RESET} to continue.\n""",

f"""{Fore.RED}Initialization...{Fore.RESET}
Set the steering wheel in the {Fore.RED}middle{Fore.RESET}
And Press {Fore.BLACK + Back.WHITE}-Ctrl+F12-{Fore.RESET + Back.RESET} to continue.\n""",

f"""Choose the version {Fore.BLACK + Back.WHITE}(enter only a number){Fore.RESET + Back.RESET}
   1.V1 {Fore.RED}( X axis Steering | Z axis +50% Throttle | Z axis -50% Break )
Or{Fore.RESET} 5.QUIT Application.\n""",

f"""{Fore.RED}Invalid version selected.{Fore.RESET}\n""",

f"""{Fore.RED}Initialization Done.{Fore.RESET} Press {Fore.BLACK + Back.WHITE}-Ctrl+F12-{Fore.RESET + Back.RESET} to start Emulating.\n""",

f"""{Fore.RED}Steering Wheel Emulating...{Fore.RESET}\n""",

f"""{Fore.RED}Exiting Emulation...{Fore.RESET}\n"""

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