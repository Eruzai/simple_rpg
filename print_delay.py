import time

class PrintText:
  def __init__(self) -> None:
    pass

  def Print_with_delay(string):
    for char in string:
      print(char, end='', flush=True)
      time.sleep(0.02)