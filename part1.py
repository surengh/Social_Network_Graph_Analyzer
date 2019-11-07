# Author : Surender Kumar
# Contact : kumarsu44@gmail.com

import MySQLdb
import sys
import lib


conn=MySQLdb.connect(host="10.5.18.45", user="10CS60D03", passwd="mtech10", db="test")
#conn=MySQLdb.connect(host="localhost", user="root", passwd="suren", db="test")
cursor = conn.cursor ()

def intersect(A, B):
	return list(set(A) & set(B))

def main_part1():

	InputName=raw_input("Enter username: ")

	############### Fetching tags for given userid ##########################
	TagsList=lib.fetch_tags_for_username(InputName)
	TagsSet=set(TagsList)
	#print "User's tag list:", TagsList

	############### Fetching friends Ids from links for given username ##########################
	IdsList=[]
	IdsList=lib.fetch_friends_id(InputName)


	IntersectionList=[]
	if not IdsList:	
		print "Entered user have no friend"
	else:
		for fid in IdsList:
			FTagQuery="select distinct tags.tag from photo, tags where photo.owner="+ '"'+str(fid)+'"'+"and tags.photoid=photo.photoid"+';'
			cursor.execute(FTagQuery)
			RowsOfFTag=cursor.fetchall()
			FTagsList=[]
			#if not RowsOfFTag:
				#continue
			#else:
			if 1:
				for row in RowsOfFTag:
	        			ftag1="%s" %row
		        		if not ftag1 in FTagsList:
        			        	FTagsList.append(ftag1)
				#FTagsSet=set([])
				FTagsSet=set(FTagsList)
				IntersectionSet=TagsSet & FTagsSet
				if len(IntersectionSet)>0:
					print str(InputName), "and ", str(fid), " shares interest"
				else:
					print "Input User Id:", str(InputName), "doesn't shares interest with any one"


############## calling part1() method ###################
#part1()					
