#####################################################################################################################################################
#							Library for following enlisted mothods
#							Author: Surender Kumar
#							M-Tech (CS)
#							IIT Kharagpur
#							email: oksuren@gmail.com
#####################################################################################################################################################
#
# List of supported methods with their Signature:
#
# fetch_tags_for_userid(InputId)
# fetch_tags_for_username(InputName)
# fetch_tags_for_photoid(PhotoId)
# fetch_photoids(InputId)
# fetch_friends_id(InputId)
# fetch_friends_id(InputName)
# fetch_photoid_for_tag(InputTag)
# fetch_owners_for_photoid_list(InputPhotoIdsList)
# check_interest_share(Id1, Id2)
# check_friendship_for_every_pair(InputOwnerIdList)
# check_acquaintance(Id1, Id2)
# intersection_of_lists(List1, List2)
# match_lists(List1,List2)
# removeall(List)


import MySQLdb
import sys
import Queue

conn=MySQLdb.connect(host="10.5.18.45", user="10CS60D03", passwd="mtech10", db="test")
#conn=MySQLdb.connect(host="localhost", user="root", passwd="suren", db="test")
cursor = conn.cursor ()


############### Method returns list of tags for given InputId (userid) ##########################
def fetch_tags_for_userid(InputId):
	TagQuery="select distinct tags.tag from photo, tags where photo.owner="+ '"'+str(InputId)+'"'+"and tags.photoid=photo.photoid"+';'
	cursor.execute(TagQuery)
	RowsOfTag=cursor.fetchall()
	TagsList=[]
	for row in RowsOfTag:
        	tag1="%s" %row
        	if not tag1 in TagsList:
                	TagsList.append(tag1)
	#print TagsList
	#TagsSet=set(TagsList)
	return TagsList


############### Method returns list of tags for given InputName (username) ##########################
def fetch_tags_for_username(InputName):
        TagQuery="select distinct tags.tag from photo, tags, user where user.username="+ '"'+str(InputName)+'"'+"and user.userid=photo.owner and\
	tags.photoid=photo.photoid"+';'
        cursor.execute(TagQuery)
        RowsOfTag=cursor.fetchall()
        TagsList=[]
	if not RowsOfTag:
		return []
	else:
        	for row in RowsOfTag:
                	tag1="%s" %row
	                if not tag1 in TagsList:
        	                TagsList.append(tag1)
        	#print TagsList
        	#TagsSet=set(TagsList)
        	return TagsList


############### Method returns list of tags for given PhotoId ##########################
def fetch_tags_for_photoid(InputPhotoId):
        TagQuery="select distinct tags.tag from photo, tags where photo.photoid="+ '"'+str(InputPhotoId)+'"'+"and tags.photoid=photo.photoid"+';'
        cursor.execute(TagQuery)
        RowsOfTag=cursor.fetchall()
        TagsList=[]
        for row in RowsOfTag:
                tag1="%s" %row
                if not tag1 in TagsList:
                        TagsList.append(tag1)
        return TagsList



############### Method returns list of tags for given InputName (username) ##########################
def fetch_photoids(InputName):
        TagQuery="select distinct photo.photoid from photo, user where user.username="+ '"'+str(InputName)+'"'+"and user.userid=photo.owner"+';'
        cursor.execute(TagQuery)
        RowsOfPhotoIds=cursor.fetchall()
        PhotoIdsList=[]
        for row in RowsOfPhotoIds:
                pid1="%s" %row
                if not pid1 in PhotoIdsList:
                        PhotoIdsList.append(pid1)
        return PhotoIdsList




############### Method returns list of friends Ids from links for given InputId (userid) ##########################
def fetch_friends_id(InputId):
	IdQuery="select distinct links.userid2 from links where links.userid1="+ '"'+str(InputId)+'"'+';'
	cursor.execute(IdQuery)
	RowsOfId=cursor.fetchall()
	IdsList=[]
	for row in RowsOfId:
        	id1="%s" %row
	        if not id1 in IdsList:
        	        IdsList.append(id1)
	return IdsList



############### Method returns list of friends Ids from links for given username ##########################
def fetch_friends_id(InputName):
        IdQuery="select distinct links.userid2 from links, user where user.username="+ '"'+str(InputName)+'" and user.userid=links.userid1'+';'
        cursor.execute(IdQuery)
        RowsOfId=cursor.fetchall()
        IdsList=[]
        for row in RowsOfId:
                id1="%s" %row
                if not id1 in IdsList:
                        IdsList.append(id1)
        return IdsList



################ Method returns 1 pair (Id1, Id2) shares interest i.e. has one or more common tag(s) #################
def check_interest_share(Id1, Id2):
	TagsList=[]
	FTagsList=[]	
	IntersectionList=[]
	TagsList=fetch_tags(Id1)
	TagsSet=set(TagsList)
        FTagQuery="select distinct tags.tag from photo, tags where photo.owner="+ '"'+str(Id2)+'"'+"and tags.photoid=photo.photoid"+';'
        cursor.execute(FTagQuery)
        RowsOfFTag=cursor.fetchall()
        for row in RowsOfFTag:
        	ftag="%s" %row
        	if not ftag in FTagsList:
        		FTagsList.append(ftag)
        FTagsSet=set(FTagsList)
        #IntersectionList=TagsSet.intersect(FTagsSet)
        IntersectionList=TagsSet & FTagsSet
	print "Intersection: ",IntersectionList
	if len(IntersectionList)>0:
        	#print str(InputId), "and ", str(fid), " shares interest"
		return 1
	else:	
        	#print "Input User Id:", str(InputId), "doesn't shares interest with any one"
		return 0



############### Method returns list of photoid for given tag ##########################
def fetch_photoid_for_tag(InputTag):
	PhotoIdQuery="select distinct tags.photoid from tags where tags.tag="+ '"'+str(InputTag)+'"'+';'
	cursor.execute(PhotoIdQuery)
	RowsOfPhotoId=cursor.fetchall()
	PhotoIdsList=[]
	for row in RowsOfPhotoId:
        	pid="%s" %row
	        if not pid in PhotoIdsList:
        	        PhotoIdsList.append(pid)
	return PhotoIdsList


################ Fetching Owner Ids for photo Ids List #################
def fetch_owners_for_photoid_list(InputPhotoIdsList):
	PhotoOwnerIdList=[]
	for pid in InputPhotoIdsList:
        	OwnerIdsQuery="select distinct photo.owner from photo where photo.photoid="+'"'+str(pid)+'"'+';'
	        cursor.execute(OwnerIdsQuery)
        	oiq=cursor.fetchone()
	        #print oiq
        	oid="%s" %oiq
	        if not oid in PhotoOwnerIdList:
        	        #RowsPhotoOwnersId.append(oiq)
	                oid="%s" %oid
        	        #print "oid: ", oid
                	PhotoOwnerIdList.append(oid)

	return PhotoOwnerIdList


################ Method returns 1 if every pair (A, B) in InputOwnerIdList are friends #################
def check_friendship_for_every_pair(InputOwnerIdList):
	flag=0
	if len(InputOwnerIdList)<2:
		#print "False: Entered tag [", str(InputTag), "] belongs to less than 2 users"
		return 0
	else:
		count=len(PhotoOwnerIdList)
		i=0
		while i<=count-2:
			j=i+1
			while j<=count-1:
				pid_t1="%s" %InputOwnerIdList[i]
				pid_t2="%s" %InputOwnerIdList[j]
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
				#print "Fail: given tag [",str(InputTag), "] is not a Signature"
				#break
				return 0
			else:
				i=i+1

		if not flag:
			#print "True: given tag [",str(InputTag), "] is a Signature"
			return 1
	
	
################ Method returns 1 if Id1 and Id2 are freinds #################
acq=0
Que=Queue.Queue(0)
VList=[]
#FList=[]
def check_friendship(Id1, Id2):
	#global FList
	FList=[]
	LinkQuery1="select distinct links.userid2 from links where links.userid1="+'"'+str(Id1)+'";'
        cursor.execute(LinkQuery1)
        frows1=cursor.fetchall()
        for fi in frows1:
        	fi="%s" %fi
                FList.append(str(fi))
	#print "FList: ", FList
	if FList:
		if str(Id2) in FList:
			return 1
		else:
			return FList
	else:
		return 0


################ Method returns 1 if Id1 and Id2 are acquainted #################
acq=0
QList=[]
VList=[]
def check_acquaintance(Id1, Id2):
	global QList
        global acq
        global VList
        #Flist=[]
	if str(Id1) is str(Id2):
		acq=1
		return 1
	
        #print Id1, "---", Id2,
	if not Id1 in VList:
                VList.append(Id1)
		result=check_friendship(Id1, Id2)
		if result==1:
			#while len(QList)>0:
			removeall(QList)
			#print "Id1 and Id2 are acquainted"
			acq=1
			removeall(VList)
			return 1
		elif result==0:
			if len(QList)>0:
				Next1=str(QList.pop())
				if not Next1 in VList:
					return check_acquaintance(Next1, str(Id2))
			else:
				#print Id1, Id2, "are not Acquainted"
				removeall(VList)
				removeall(QList)
				return 0
		elif type(result).__name__=='list':
			if len(result)>0:
				for f1 in result:
                        		#f1="%s" %f1
					if (f1 not in QList) and (f1 not in VList):
                                		QList.append(str(f1))
                                		#print "Inserted in Queue: ", f1, "Que Size: ",Que.qsize()
					else:
						continue
			if len(QList)>0:
				Next2=str(QList.pop())
				#if not Next2 in VList:
				return check_acquaintance(Next2, str(Id2))
				#else:
					#return 0
	elif len(QList)>0:
        	Next3=str(QList.pop())
        	if not Next3 in VList:
                	return check_acquaintance(Next3, str(Id2))
                else:
                	return 0
	else:
		return 0
	


def intersection_of_lists(List1, List2):
	set1=set(List1)
	set2=set(List2)
	iset=set1 & set2
	return list(iset)


def match_lists(List1, List2):
	set1=set(List1)
	set2=set(List2)
	ilist=intersection_of_lists(List1, List2)
	eset=set1.union(set2)-set(ilist)
	if not eset:
		return 1
	else:
		return 0


def removeall(List):
	if List:
		l=List.pop()
		removeall(List)


