from vk_part import do_vk
from console_part import do_console
mode = input('Choose mode: ')
if mode.lower() == 'vk':
    do_vk()  
elif mode.lower() == 'console':
    do_console()
 
