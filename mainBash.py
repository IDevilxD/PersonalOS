from VARS.vars import copyright
from RESOURCES import function

running = True

print()
print(copyright)
print()

while running:
  UII = input("Personal Bash: ")
  try:
    UII = UII.lower()
    UIIs = UII.split(" ")
    command = UIIs[0]
    com1 = UIIs[1]
    com2 = UIIs[2]
    com3 = UIIs[3]
    com4 = UIIs[4]
    com5 = UIIs[5]
  except:
    print("ERROR : Problem in computing the command")
    pass
  
  if UII == "update":
    function.update()
  if command == "server":
    try:
      if com1 == "":
        com1 = "/storage/emulated/0"
      if com2 == "":
        com2 = "192.168.225.229"
      if com3 = "":
        com3 = "1527"
      function.ssOP(com1,com2,com3)
    except:
      print("ERROR : server <location/●> <ip/●> <port/●>")
    os.system(f"cd {com1}")
    os.system(f"python -m http.server {com3} --bind {com2}")
