# Laptop-Health-Manager

A python Program that runs on Background and Reminds you to keep your Laptop Healthy.

> Reference: [Whatsbyte.com](https://whatsabyte.com/40-80-battery-rule-laptops)

<hr>

### To Use You Have to change some Paths in the Code

(If Your Folder which holds these files is "C:\Documents\Laptop-Health")

- In main.py

replace

```
pc.notify.base_folder = "[Your Base Folder's Path]"
```

with

```
pc.notify.base_folder = "C:\Documents\Laptop-Health"
```

<hr>

- In main.bat

replace

```
[Your Base Folder's Drive]:
cd [Your Base Folder's Path]
```

with

```
C:
cd C:\Documents\Laptop-Health
```

<hr>

- In launcher.vbs

replace

```
WshShell.Run chr(34) & "[Your Base Folder's Path]\main.bat" & Chr(34), 0
```

with

```
WshShell.Run chr(34) & "C:\Documents\Laptop-Health\main.bat" & Chr(34), 0
```

Likewise...

<hr>

Then Copy the Launcher_of_notifications.vbs and paste in the startup Folder to Run the Program On Startup

- To get the startup Folder

> Press Win + R and type, shell:startup

> Then Paste the Shortcut of the launcher.vbs there and It will run with the Startup

<hr>

### Important!

To Run this Program You Must have to install Python and install plyer and psutil libraries

- [Download Python](https://www.python.org/)

After Installing python open cmd and run these commands, It'll install plyer and psutil Libraries

```
pip install plyer
```

```
pip install psutil
```

<hr>

![alert](https://i.ibb.co/0MbGD5z/Screenshot-2022-02-11-074654.jpg)

![alert](https://i.ibb.co/CwtnjC4/Screenshot-2022-02-11-074627.jpg)

A Project by [Hiruka Chansilu](https://hirukachansilu.tk)©
