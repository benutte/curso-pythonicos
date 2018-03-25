""" for x in range(5, -1, -1):
  ip = "192.168.0.%d" % x
  print ip
  if ip == "192.168.0.3":
      break
"""

for y in range(1,5):
    for x in range(20,25):
        print "Scan sendo realizado no ip 192.168.0.%d na porta %d" %(y,x)
        ip = "192.168.0.%d" % x
        print ip
        if ip == "192.168.0.3":
            break
