# Snowflakes Screensaver

This desktop application can:

- Spawn snowflakes in window mode or fullscreen mode.
- Spawn more of less snowflakes, on your desire.
- Be able to change snowflake parameters, like size, speed and acceleration.

![v0_1](https://user-images.githubusercontent.com/36193247/230888007-9ea05445-092b-4c35-87f1-091f63fa6337.png)

# How to use it

- Download and install the latest Python 3.x from https://www.python.org/downloads/
    - During installation process install Python downloading tool that called `pip`. Or manually install it later by using this commad:
        - in Windows:
            `py get-pip.py`
        - in Linux:
            `python get-pip.py`
        - in MacOS:
            `python get-pip.py`
    - Get some modules by using `pip`, required by this application:
        `pip install simple_draw pyyaml`
- Once you have installed Python and `pip`, launch the file named `main.py` in the application directory.
- If you want to tune parameters, like change sizes of application screen or set up launch in fullscreen resolution, or change snowflakes parameters, you're up to edit file `config.yml`. You can open it with an any text editor: `Notepad, Vim, etc.`, then you can manually change values of the parameters. Save it, relaunch the application, so your changes will take effect.
- You can also build an executable file from the source code, and use given application as your desktop screensaver.
