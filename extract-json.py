#!/usr/bin/python3

import json

import argparse
parser = argparse.ArgumentParser(description='This program takes information from GREW output files and organizes it for lexbuilder.')
parser.add_argument('-i','--input', help='Input file', required=False)
parser.add_argument('-d', '--deptype', help='Dependence type: std, pass or cop')
parser.add_argument('-o','--output', help='Output file', required=False)
args = parser.parse_args()


with open(args.input, 'r') as json_file:
	json_load = json.load(json_file)
	entries = []
	for n in range(0, len(json_load)):
		wlist = []
		sentid = json_load[n]['sent_id']
		wlist.append(sentid)

		# Standard argument structure (verb = head)
		if args.deptype == "std":
			head = json_load[n]['matching']['nodes']['GOV']
			wlist.append(head)
			del json_load[n]['matching']['nodes']['GOV']
			for key,value in json_load[n]['matching']['nodes'].items():
				if key == "NSUBJIMP" or "NSUBJ" or "CSUBJSINF" or "CSUBJSCOMPL" or "CLR" or "OBJSCOMPL" or "OBJSN" or "OBJSINF" or "IOBJDE" or "OBJAVINF" or "OBJASN" or "IOBJA" or "IOBJDE" or "OBLSURSN" or "OBLSINF" or "OBLDESINF" or "OBJDESN" or "OBJDEVINF" or "OBLPARSN" or "OBLENSN" or "OBLDESN" or "OBLAVECSN" or "OBLCONTRESN" or "OBLASN" or "OBLASINF" or "CLY" or "DLOC":
					dep = key
					wlist.append(dep)

		# Argument structure with a copula (verb != head)
		elif args.deptype == "cop":
			head = json_load[n]['matching']['nodes']['VETAT']
			wlist.append(head)
			for key,value in json_load[n]['matching']['nodes'].items():
				dep = key
				wlist.append(dep)

		# Passive voice		
		elif args.deptype == "pass":
			head = json_load[n]['matching']['nodes']['PART']
			wlist.append(head)
			dep = "@passive"

		entries.append(wlist)

	with open(args.output, "w") as outputfile:
		outputfile.write(str("\n"))
		for elem in entries:
			outputfile.write(str(elem[0]) + '\t' + elem[1] + '\t' + elem[2] + '\n')
