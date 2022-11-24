import subprocess
import sys

print("Python running!")

user = "test"
host = "mysshserver"
cmd = "date"

cmdline = f"ssh -oStrictHostKeyChecking=no {user}@{host} {cmd}"


print("Python finished!")

command = "uname -a"

# ["ssh", "some-host@some-user", "some-command"]
param = ["ssh", "-oStrictHostKeyChecking=no", host, cmd]

ssh = subprocess.Popen(param,
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print(f"ERROR: {error}", file=sys.stderr)
else:
    print(result)
