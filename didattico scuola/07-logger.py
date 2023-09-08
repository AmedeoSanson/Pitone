import datetime as dt

class Logger:
    def __init__(self, level):
        self._level = level

    def log(self, message):
        fileName = f"Logger_oggi"

        with open(fileName, 'a') as f:
            if(self._level == "HIGH"):
                f.write(str(dt.datetime.now()))

            f.write(message + "\n")