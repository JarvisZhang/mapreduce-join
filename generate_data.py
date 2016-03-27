#!/usr/bin/python

import sys

submitEgg = {
    'job_id="job_200906250002_6326"': 'submit_time="1246503054810" user="rank-ubs"',
    'job_id="job_200906250002_6327"': 'submit_time="1246503199098" user="rank-ubs"',
    'job_id="job_200906250002_6328"': 'submit_time="1246503312670" user="rank-ubs"',
    'job_id="job_200906250002_6329"': 'submit_time="1246503330231" user="zhangyan"'
}

finishEgg = {
    'job_id="job_200906250002_6326"': 'finish_time="1245390445599" job_status="SUCCESS" input_size="13509354230" midoutput_size="2000" output_size="42"',
    'job_id="job_200906180111_0583"': 'finish_time="1245390448751" job_status="SUCCESS" input_size="14363492302" midoutput_size="800" output_size="17"',
    'job_id="job_200906250002_6329"': 'finish_time="1245390503532" job_status="SUCCESS" input_size="15503679752" midoutput_size="2000" output_size="42"',
    'job_id="job_200906180111_0585"': 'finish_time="1245390512106" job_status="SUCCESS" input_size="14641261568" midoutput_size="2000" output_size="42"'
}

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print "the number for submit logs, finish logs and their paths"
        exit(1)
    submitLogPrefix = sys.argv[3] + "jobfinish.20090515"
    finishLogPrefix = sys.argv[3] + "jobsubmit.20090515"
    submitNum = int(sys.argv[1])
    finishNum = int(sys.argv[2])
    for i in range(0, submitNum):
        submitLogName = submitLogPrefix + str(i)
        finishLogName = finishLogPrefix + str(i)
        with open(submitLogName, "w") as submitFile:
            for j in range(0, 10):
                for (key, value) in submitEgg.iteritems():
                    submitFile.write("%s %s\n" % (key + str(i) + str(j), value));
        with open(finishLogName, "w") as finishFile:
            for j in range(0, 10):
                for (key, value) in finishEgg.iteritems():
                    finishFile.write("%s %s\n" % (key + str(i) + str(j), value));
