import sys
import subprocess
import time
print("running test on", sys.argv[1])
count=1
try:
    count=sys.argv[2]
except:
    print("run single execution")
bef=time.time()
for x in range(0,int(count)):
    cmd="python3 "+sys.argv[1]
    subprocess.Popen(cmd, shell=True).communicate(input=None)
now=time.time()
print("time elapsed running",str(now - bef))
