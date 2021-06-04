#Install Library
#!pip install speedtest-cli


#Speed Test Now
import speedtest
sp = speedtest.Speedtest()
print(f"Downlaod Speed : { sp.download() }")
print(f"Upload Speed : { sp.upload() }")