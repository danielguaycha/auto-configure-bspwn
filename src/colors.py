from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[0;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[0;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[0;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[0;37m"
    stdout.write(WHITE)

def orange():
    ORANGE = "\033[38;5;214m"
    stdout.write(ORANGE)

def aqua():
    AQUA = "\033[0;36m"
    stdout.write(AQUA)
    

def log(message: str, color: str = "white"):
    if color == "red" :
        red()
    if color == "green" :
        green()
    if color == "blue" :
        blue()
    if color == "yellow" :
        yellow()
    if color == "purple" :
        purple()
    if color == "white" :
        white()
    if color == "orange" :
        orange()
    if color == "aqua" :
        aqua()
    
    print(f"{message}\033[0m")
    

    