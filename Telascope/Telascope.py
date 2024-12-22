import StellariumRC

s = StellariumRC.Stellarium() # you can pass the host, port and password (if any) as parameters
print(s.main.getStatus()) # get the current state of Stellarium
s.main.setFocus(target='polaris',mode='zoom') # focus on moon and auto zoom-in
print(s.objects.getInfo('polaris')) # get info about moon