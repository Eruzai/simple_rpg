import os

class ConsoleCommands:
  def __init__(self) -> None:
    pass

  def clear_console():
    if os.name == 'nt':
      os.system('cls')
    else:
      os.system('clear')