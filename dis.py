#!/usr/bin/python
import json
import subprocess
DIR = "*** FULL INSTALL DIR ***"
REFSCR = "lib/refresh.sh"
COMMD = DIR + REFSCR
BACKLOG = "Backlog"
BLOCKED = "Blocked"
ANALYSIS = "Analysis"
WIPRDY = "WIP Ready"
WIP = "WIP"
PEER = "Peer Review"
TESTRDY = "Test Ready"
TEST = "Test"
UAT = "UAT"
DONE = "Done"
statOrder = {0: BACKLOG,1: BLOCKED,2: ANALYSIS,3: WIPRDY,4: WIP,5: PEER,6: TESTRDY,7: TEST,8: UAT,9: DONE }
subprocess.call([COMMD], shell=True)
def printWf(tin, wkfl, sep):
	flag = 0
	for ti in tin:
		if ti["custom_fields"]["custom_286"] == wkfl:
			print("Ticket: " + ti["number"] + " - " + ti["custom_fields"]["custom_286"])
			print("\t" + ti["name"])
			flag = 1
	if flag == 1 and wkfl != DONE and sep == 1:
		print("\n--------------------------------\n")


print("\n")
f = open(DIR + 'lib/onTimeOutput.out', 'r')
jsonEncoded = f.read()
onTimeD = json.loads(jsonEncoded)
tickets = onTimeD['data']

for i in range(0,10):
	print('{} = {}'.format(i, statOrder[i]))

print('\n')

try:
	wkIn = input('Workflow Status: ')
except SyntaxError:
	wkIn = ""

print('\n\n')

if wkIn == "":
	for i in range(0,10):
		printWf(tickets, statOrder[i], 1)
else:
	printWf(tickets, statOrder[wkIn], 0)
	print('\n\n')
