#!/usr/bin/python

import os
import sys

filepath = os.environ["map_input_file"]
filename = os.path.split(filepath)[-1]

def mapper():
	for line in sys.stdin:
		isFinished = "-1"
		if not line.strip():
			continue
		jobInfoList = line.split()
		jobId = jobInfoList[0]
		jobAttrs = " ".join(jobInfoList[1:])
		if filename.startswith("jobsubmit"):
			isFinished = "0"
		elif filename.startswith("jobfinish"):
			isFinished = "1"
		print "%s\t%s\t%s" % (jobId, jobAttrs, isFinished)

if __name__ == "__main__":
    mapper()
