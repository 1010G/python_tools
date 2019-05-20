# -*- coding: utf-8 -*-
# Add colors to your terminal or to your string
# pwhite("hello") will print normally
# pwhite("hello",1) will print and reset the line, print will display
# on the same line every times


class printColor:

    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'
    white = "\033[1;37m"

    colors = [
        '\033[30m',  # black
        '\033[31m',  # red
        '\033[32m',  # green
        '\033[33m',  # orange
        '\033[34m',  # blue
        '\033[35m',  # purple
        '\033[36m',  # cyan
        '\033[37m',  # lightgrey
        '\033[90m',  # darkgrey
        '\033[91m',  # lightred
        '\033[92m',  # lightgreen
        '\033[93m',  # yellow
        '\033[94m',  # lightblue
        '\033[95m',  # pink
        '\033[96m',  # lightcyan
        "\033[1;37m",  # white
    ]

    end = "\033[m"

    def pwhite(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().white, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().white, input, printColor().end), end='\r')

    def pblack(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().black, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().black, input, printColor().end), end='\r')

    def pred(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().red, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().red, input, printColor().end), end='\r')

    def pgreen(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().green, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().green, input, printColor().end), end='\r')

    def porange(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().orange, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().orange, input, printColor().end), end='\r')

    def pblue(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().blue, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().blue, input, printColor().end), end='\r')

    def ppurple(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().purple, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().purple, input, printColor().end), end='\r')

    def pcyan(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().cyan, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().cyan, input, printColor().end), end='\r')


    def plightgrey(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().lightgrey, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().lightgrey, input, printColor().end), end='\r')

    def pdarkgrey(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().darkgrey, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().darkgrey, input, printColor().end), end='\r')

    def plightred(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().lightred, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().lightred, input, printColor().end), end='\r')

    def plightgreen(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().lightgreen, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().lightgreen, input, printColor().end), end='\r')

    def pyellow(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().yellow, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().yellow, input, printColor().end), end='\r')

    def plightblue(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().lightblue, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().lightblue, input, printColor().end), end='\r')

    def ppink(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().pink, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().pink, input, printColor().end), end='\r')

    def plightcyan(input: str, clear=0):
        if clear == 0:
            print("{0}{1}{2}".format(printColor().lightcyan, input, printColor().end))
        else:
            print("{0}{1}{2}".format(printColor().lightcyan, input, printColor().end), end='\r')

    def prand(input: str, clear=0):
        if clear == 0:
            print(printColor.str_rand_color(input))
        else:
            print(printColor.str_rand_color(input),end='\r')

    def str_rand_color(str):
        """
            Return string with code colors
        """
        from random import randint
        rnd = randint(0, len(printColor.colors)-1)
        return "{0}{1}{2}".format(printColor.colors[rnd], str, printColor().end)
