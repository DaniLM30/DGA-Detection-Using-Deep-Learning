#!/usr/bin/env python
#Copyright (c) 2020 Daniel Lopez
#All rights reserved.

from dgaintel import get_prob


def dga_analyzer():
	#Open file
	with open("dga_testing.txt") as f:
		domains = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
	domains = [x.strip() for x in domains] 
	
	total= 0
	detected = 0
	
	#For loop to analyze domains
	for domain in domains:
		probability = get_prob(domain)
		total += 1
		#print("This domain: " + str(domain) + " has " + str(probability) + " probability")
		if probability > 0.5:
			detected +=1
	
	print("--------------------------------------------------------------------------")
	print("Domains detected: " + str(detected) + "/ Total domains: " + str(total))
	print("Percentage: " + str(detected/total*100) + "%")
	print("--------------------------------------------------------------------------")
		
dga_analyzer()