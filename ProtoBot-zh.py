from termcolor import colored
import random, sys, json

fp = json.load(open("wordlist_zh.json"))

con = fp['constraints']
ite = fp['items']
pre = fp['prependText']
flag = ''

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    c = random.choice(con)
    i = random.choice(ite)
    if c.startswith('为'):
        print(colored(c, 'blue'), end='')
        print(pre, end='')
    else:
        print(pre, end='')
        print(colored(c, 'blue'), end='')
    print(colored(i, 'red'))
    if flag != 'c':
        r = getch()
        if r == 'q':
            sys.exit(0)
        elif r == 'c':
            flag = r
