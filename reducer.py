#!/usr/bin/python

import sys

def reducer():
	lastJobId = ""
	lastJobAttrs = ""
	for line in sys.stdin:
		(jobId, jobAttrs, isFinished) = line[:-1].split("\t")
		if jobId == lastJobId:
			if isFinished == "0":
				print " ".join((jobId, jobAttrs, lastJobAttrs))
			elif isFinished == "1":
				print " ".join((jobId, lastJobAttrs, jobAttrs))
		lastJobId = jobId
		lastJobAttrs = jobAttrs

if __name__ == "__main__":
	reducer()
