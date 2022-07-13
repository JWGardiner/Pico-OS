# Pico-OS
A small operating system for the Pi Pico W.

This allows you to interact with the hardware in a much easier way, and requires much less time for development for the board.

The structure is simple:

- bin
- usr
- Startup
- main.py

main.py is the main part of the OS.

bin is all of the installed programs.

usr is for configuration.

Upon starting, it will generate these files.

Once you boot it up for the first time, you are greeted by a CLI interface; you can access any commands in /bin and to keep the OS lightweight on the limiting hardware; only a few things are installed.

- Package Manager (WIP)
- Network Tools

By default the only commands you can use are:

- `pkg`
- `net-connect`
- `net-disconnect`


# Usage

Files in startup are ran just before the cli starts, which is useful for doing stuff early on.

Files in bin are run when you type the name of the command in the cli.

Files in usr are for configuration.

# Support

WIP
