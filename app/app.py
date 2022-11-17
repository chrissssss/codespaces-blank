import subprocess

user="test"
host="ssh"
cmd='date'

cmdline=f"ssh {user}@{host} {cmd}"
subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

