# Exercise

url = https://github.com/codedthinking/tender-home-bias/releases/download/v1.0/ted-sample.csv



from typing import Protocol


file_name = url[-14:]
print(file_name) # ted_sample.csvpy

protocol = url[0:5]
print(protocol)

host_name = url[8:18]
print(host_name)

