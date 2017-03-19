class Color(object):
    RESET   = '\x1b[0m'

    BLACK   = 0
    RED     = 1
    GREEN   = 2
    YELLOW  = 3
    BLUE    = 4
    MAGENTA = 5
    CYAN    = 6
    WHITE   = 7

    NORMAL  = 0
    BOLD    = 1

    @staticmethod
    def to_color_string(string,
                        foreground = 7,
                        background = None,
                        style      = 1):
        style      = '\x1b[0%sm' % style
        foreground = '\x1b[3%sm' % foreground
        background = '' if background is None else '\x1b[4%sm' % background
        preset     = style + foreground + background

        colored    = preset + string + Color.RESET

        return colored

    def warn(string):
        colored = Color.to_color_string(string, foreground = Color.YELLOW)

        return colored