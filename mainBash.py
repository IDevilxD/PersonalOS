from VARS.vars import copyright
from RESOURCES import function

running = True

print(copyright)

while running:
  UII = input("Personal Bash: ")
  if UII == "update":
    function.update()
