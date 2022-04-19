from VARS import vars
from RESOURCES import function

running = True

while running:
  UII = input("Personal Bash: ")
  if UII == "update":
    function.update()
