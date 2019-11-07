# Author : Surender Kumar
# Contact : kumarsu44@gmail.com



import MySQLdb
import sys
import lib

conn=MySQLdb.connect(host="10.5.18.45", user="10CS60D03", passwd="mtech10", db="test")
#conn=MySQLdb.connect(host="localhost", user="root", passwd="suren", db="test")
cursor = conn.cursor ()



############### Fetching Photo Ids for given tag ##########################
"""
PhotoIdQuery="select distinct tags.photoid from tags where tags.tag="+ '"'+str(InputTag)+'"'+';'
cursor.execute(PhotoIdQuery)
RowsOfPhotoId=cursor.fetchall()
PhotoIdsList=[]
for row in RowsOfPhotoId:
	pid="%s" %row
	if not pid in PhotoIdsList:
		PhotoIdsList.append(pid)
#print "PhotoIdsList: ", PhotoIdsList
"""

################ Fetching Owner Ids for fetched photo Ids #################
"""
PhotoOwnerIdList=[]
for pid1 in PhotoIdsList:
	OwnerIdsQuery="select distinct photo.owner from photo where photo.photoid="+'"'+str(pid1)+'"'+';'
	cursor.execute(OwnerIdsQuery)
	oiq=cursor.fetchone()
	#print oiq
	oid="%s" %oiq
	if not oid in PhotoOwnerIdList:
		#RowsPhotoOwnersId.append(oiq)
		oid="%s" %oid
		#print "oid: ", oid
		PhotoOwnerIdList.append(oid)
"""

############## Checking friendship for every pair (A, B) ################
#flag=0
def main_part3():
	global PhotoOwnerIdList
	flag=0
	InputTag=raw_input("Enter Tag: ")
	
	############### Fetching Photo Ids for given tag ##########################
	PhotoIdsList=lib.fetch_photoid_for_tag(InputTag)

	################ Fetching Owner Ids for fetched photo Ids #################
	PhotoOwnerIdList=lib.fetch_owners_for_photoid_list(PhotoIdsList)	

	if len(PhotoOwnerIdList)<2:
		print "False: Entered tag [", str(InputTag), "] belongs to less than 2 users"
	else:
		count=len(PhotoOwnerIdList)
		i=0
		while i<=count-2:
			j=i+1
			while j<=count-1:
				pid_t1="%s" %PhotoOwnerIdList[i]
				pid_t2="%s" %PhotoOwnerIdList[j]
				LinkQuery1="select * from links where (links.userid1="+'"'+str(pid_t1)+'"'\
				+" and links.userid2="+'"'+str(pid_t2)+'" );'
				cursor.execute(LinkQuery1)
				noofrows1=cursor.fetchall()
				if len(noofrows1)<=0:
					LinkQuery2="select * from links where (links.userid2="+'"'+str(pid_t1)+'"'\
					+" and links.userid1="+'"'+str(pid_t2)+'" );'
					cursor.execute(LinkQuery2)
					noofrows2=cursor.fetchall()
					if not len(noofrows2)>0:
						flag=1
						break
				else:	
					j=j+1
			if flag:
				print "Fail: given tag [",str(InputTag), "] is not a Signature"
				break	
			else:
				i=i+1

		if not flag:
			print "True: given tag [",str(InputTag), "] is a Signature"
