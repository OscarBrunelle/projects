@echo off

netsh wlan set hostednetwork mode=allow ssid=ssid key=key
netsh wlan start hostednetwork

pause