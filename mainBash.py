from VARS.vars import copyright
from RESOURCES import function

running = True

print()
print(copyright)
print()

while running:
  UII = input("Personal Bash: ")
  if UII == "update":
    function.update()
