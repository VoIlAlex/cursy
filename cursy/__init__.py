import curses


def curses_main_method(fn):
    def method(self):
        def bound_main_method(stdscr):
            self.stdscr = stdscr
            fn(self)
            self.stdscr = None
        curses.wrapper(bound_main_method)

    return method


def curses_application(cls):
    if not hasattr(cls, 'start'):
        raise AttributeError("Curses main class should have 'start' method")
    wrapped_method = curses_main_method(getattr(cls, 'start'))
    setattr(cls, 'start', wrapped_method)
    return cls
