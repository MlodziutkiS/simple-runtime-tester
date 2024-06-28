import sys
import subprocess
import time
print("running test on", sys.argv[1])
bef=time.time()
cmd="python3 "+sys.argv[1]
subprocess.Popen(cmd, shell=True).communicate(input=None)
now=time.time()
print("time elapsed running",str(now - bef))
