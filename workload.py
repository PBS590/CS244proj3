#! /usr/bin/env python

import time
import os
import subprocess

start = time.time()

subprocess.call("./workload.sh", shell=True)

end = time.time()

print(end - start)
