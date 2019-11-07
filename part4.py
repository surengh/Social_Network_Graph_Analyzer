# Author : Surender Kumar
# Contact : kumarsu44@gmail.com


import MySQLdb
import sys
import Queue
#import t1
import lib
conn=MySQLdb.connect(host="10.5.18.45", user="10CS60D03", passwd="mtech10", db="test")
#conn=MySQLdb.connect(host="localhost", user="root", passwd="suren", db="test")
cursor = conn.cursor ()

def intersect(A, B):
	return list(set(A) & set(B))


############## Calling method to check acquantance ################
#flag=0
Que=Queue.Queue(0)

def main_part4():
	InputTag=raw_input("Enter Tag: ")
	flag=0
	############### Fetching Photo Ids for given tag ##########################
	PhotoIdsList=lib.fetch_photoid_for_tag(InputTag)

	################ Fetching Owner Ids for fetched photo Ids #################
	PhotoOwnerIdList=lib.fetch_owners_for_photoid_list(PhotoIdsList)

	if len(PhotoOwnerIdList)<1:
		print "False: Entered tag [", str(InputTag), "] belongs to less than 1 users"
	else:
		count=len(PhotoOwnerIdList)
		i=0
		while i<=count-2:
			j=i+1
			while j<=count-1:
				print "checking acquaintance between: ", PhotoOwnerIdList[i], " and ", PhotoOwnerIdList[j]
				acq=lib.check_acquaintance(PhotoOwnerIdList[i], PhotoOwnerIdList[j])		
				print "acq: ",acq
				if not acq:		
					flag=1
					break
				else:	
					j=j+1
			if flag:
				break	
			else:
				i=i+1
	
		if not flag:
			print "True: given tag [",str(InputTag), "] is a Weak Signature"
		else:
			print "Fail: given tag [",str(InputTag), "] is not a Weak Signature"
