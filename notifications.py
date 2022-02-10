from plyer import notification


class Notifications():
    def __init__(self) -> None:
        self.timeout = 15
        self.base_folder = ""
        self.percentage = 0

    def plug_out(self):
        notification.notify(
            title="Plug Out!",
            message=f"Your Battery has Reached {self.percentage}%, Plug It Out to Save Your Battery Lifespan.",
            app_icon=self.base_folder.replace(
                "\\", "/") + "/Assests/plug_out.ico",
            timeout=self.timeout
        )

    def plug_in(self):
        notification.notify(
            title="Plug In!",
            message=f"Your Battery has Reached {self.percentage}%, Plug It In.",
            app_icon=self.base_folder.replace(
                "\\", "/") + "/Assests/plug_in.ico",
            timeout=self.timeout
        )
