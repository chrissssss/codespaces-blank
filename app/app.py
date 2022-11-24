import subprocess
import sys

user = "test"
host = "mysshserver"
cmd = "date"

param = ["ssh", "-v", "-oStrictHostKeyChecking=no", f"{user}@{host}", cmd]

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
