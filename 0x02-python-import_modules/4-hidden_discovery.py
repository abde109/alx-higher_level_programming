#!/usr/bin/python3.8

if __name__ == "__main__":
    """Prints all the names defined by the compiled module hidden_4.pyc (please download it locally)."""
    import hidden_4

    names = [name for name in dir(hidden_4) if name[:2] != '__']
    for name in sorted(names):
        print(name)
