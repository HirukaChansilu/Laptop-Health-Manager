from system import Check
from time import sleep

pc = Check()

pc.notify.base_folder = "[Your Base Folder's Path]"

while(True):
    pc.check_for_a_alert()
    sleep(60)
