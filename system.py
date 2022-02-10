import psutil
from notifications import Notifications
from time import sleep


class Check():
    def __init__(self) -> None:
        self.notify = Notifications()
        self.notify.base_folder = ""
        self.times1 = 0
        self.times2 = 0

    def check_for_a_alert(self):
        if psutil.sensors_battery().power_plugged == True and psutil.sensors_battery().percent >= 80:
            while self.times1 >= 5:
                self.notify.percentage = psutil.sensors_battery().percent
                self.notify.plug_out()
                self.times1 += 1
                sleep(60)

        else:
            self.times1 = 0

        if psutil.sensors_battery().power_plugged == False and psutil.sensors_battery().percent <= 40:
            while self.times2 >= 5:
                self.notify.percentage = psutil.sensors_battery().percent
                self.notify.plug_in()
                self.times2 += 1
                sleep(60)

        else:
            self.times2 = 0
