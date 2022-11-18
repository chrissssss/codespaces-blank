import subprocess

print("Python running!")

user="test"
host="mysshserver"
cmd="date"

cmdline=f"ssh {user}@{host} {cmd}"
subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

print("Python finished!") 