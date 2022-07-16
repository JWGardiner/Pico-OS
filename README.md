# Pico-OS
A small operating system for the Pi Pico W.

This allows you to interact with the hardware in a much easier way, and requires much less time for development for the board.

The structure is simple:

- `bin` 
- `usr`
- `startup` 
- `main.py` 

main.py is the main part of the OS.

bin is all of the installed programs.

usr is for configuration.

files in startup are run just after it's finished init.

Upon starting, it will generate these files.

Once you boot it up for the first time, you are greeted by a CLI interface; you can access any commands in /bin and to keep the OS lightweight on the limiting hardware; only a package manager is installed

By default the only commands you can use are:

- `pkg-rm`
- `pkg-add`

# Usage

Files in `startup` are ran just before the cli starts, which is useful for doing stuff early on.

Files in `bin` are run when you type the name of the command in the cli.

Files in `usr` are for configuration.

# Installation

The program is unfinished and as such you cannot install it yet.

**PLEASE DO NOT MAKE BUG REPORTS ABOUT THIS**

Releases will be in the releases tab along with instructions on how to install it. Different versions could vary slightly

# Support

Support me on Ko-Fi with the link on the right or the link below!

https://ko-fi.com/JWGardiner
