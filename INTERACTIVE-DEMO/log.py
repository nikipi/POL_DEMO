from datetime import datetime

class Log:

  def __init__(self, filename):
    self.filename = filename

  def write(self, message):
    with open(self.filename, "a") as file:
      timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
      file.write(timestamp + " " + message + "\n")