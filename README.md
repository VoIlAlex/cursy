# Cursy

Little and simple wrapper for curses application.

## Getting started

The `@curses_application` decorator is a util built upon `curses.wrapper` function.
This decorator adds `stdscr` to `self` object on execution time of `start` method
of the class under `@curses_application` decorator, so it can be used within the
method to access the initialized curses screen.

## Installation

```bash
pip install cursy
```

## Usage

```python
@cursy.curses_application
class Application:
    def start(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, 'Hello world')
        self.stdscr.getch()

if __name__ == "__main__":
    app = Application()
    app.start()
```

## License

[MIT](LICENSE.md)