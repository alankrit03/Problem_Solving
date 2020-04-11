import subprocess
inp = ['netsh','wlan','show','network']

result = subprocess.check_output(inp)
result = result.decode('ascii')
result = result.replace('\r','')
print(result)