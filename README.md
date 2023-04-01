# Snowflakes Screensaver

This desktop application can:

- Spawn snowflakes in window mode or fullscreen mode.
- Spawn more of less snowflakes, on your desire.
- Be able to change snowflake parameters, like size, speed and acceleration.

### How to use it

Folowing this instructions to launch this app and set up:

- Download and install the latest Python 3.x from https://www.python.org/downloads/
    - During installation process install Python downloading tool that called `pip`. Or manually install it later by using this commad:
        - in Windows:
            `py get-pip.py`
        - in Linux:
            `python get-pip.py`
        - in MacOS:
            `python get-pip.py`
    - Get some modules by using `pip`, required by this app:
        `pip install simple_draw pyyaml`
- Once you have installed Python and `pip`, go to `src` directory and launch the file named `main.py`.
- If you want to tune some parameters, like change sizes of app screen or set up launch in fullscreen resolution, or change snowflakes parameters, you're up to edit `config.yml` file. You can open it with any text editor: `Notepad, Vim, etc.`, then you can manually change values of the parameters. Save it, relaunch the app, so your changes will take effect.
- You can also build an executable file from the source code, and use given app as your desktop screensaver.