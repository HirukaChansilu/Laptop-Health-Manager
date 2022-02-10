# Laptop-Health-Manager

A python Program that runs on Background and Reminds you to keep your Laptop Healthy.

> Reference: [Wired](https://www.wired.com/2013/09/laptop-battery/#:~:text=Keeping%20Your%20Laptop%20Plugged%20in%20All%20the%20Time%20Will%20Kill%20Its%20Battery%20Faster,-Laptops%20are%20our&text=In%20order%20to%20squeeze%20as,should%20unplug%20it%20before%20that)

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

Then Create a Shortcut of launcher.vbs and put it in the startup Folder to Run the Program On Startup

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

A Project by [Hiruka Chansilu](https://hirukachansilu.tk)©
