import fcntl
import sys
import termios


proc="/dev/tty"+input("Enter TTY Number: ")
with open('/dev/tty1', 'w') as fd:
    command=input("Enter the command: ")+"\n"
    for char in command:
        fcntl.ioctl(fd, termios.TIOCSTI, char)