# Author : Surender Kumar
# Contact : kumarsu44@gmail.com

import MySQLdb
import sys
import lib



TagsList=[]
PhotoIdsList=[]

ListOfTagsSets=[]
TagCoverSet=set([])
CoverSet=set([])
ListOfSets=[]

def merge(S1, S2):
	return S1|S2

def check_cover(IList, ListOfSets):
	#global ListOfSets
	global CoverSet
	global PhotoIdsList
	#global ListOfSets
	ResultList=[]
	TempSet1=set([])
	TempSet1=CoverSet
	flag=0
	for setElement in IList:
		TempList=[]
		TempSet=set([])
		#ResultSet=CoverSet
		coverlen=len(CoverSet)
		#print "Processing element: ", setElement
		for setElementIndex in setElement:
			for element in ListOfSets[setElementIndex]:
				TempSet.add(element)
		m=lib.match_lists(list(TempSet), list(CoverSet))
		#print "m: ", m
		if m==1:
			if len(setElement)<len(TempSet1):
				ResultList=[]
				ResultList.append(setElement)
				TempSet1=set([])
				#TempSet1=set(ResultList)
				flag=1
				break
	#if len(TempSet1)==len(CoverSet):
		if flag:
			break
	if flag==0:
		return []
	else:
		#print ResultList
		return ResultList


count=1

def min_set_cover(IndexList):
	global count
	global ListOfSets
	global PhotoIdsList
	#checkinh if any single element is covering
	#global ListOfSets1
	combIndex=check_cover(IndexList, ListOfSets)
	#print "combIndex: ", combIndex
	#print "IndexList: ", IndexList
	if not combIndex:
		#generate combinations
		CombList=[]
		size=len(IndexList)
		#print "size: ", size
		i=0
		count=count+1
		while i<=size-2:
			j=i+1
			while j<=size-1:
				#print "i: ", i, " j: ", j
				mergedElements=merge(IndexList[i], IndexList[j])
				if not mergedElements in CombList:
					if len(mergedElements)<=count:
						CombList.append(merge(IndexList[i], IndexList[j]))
				j=j+1
			i=i+1
		#lib.removeall(ListOfSets1)
		#ListOfSets1=CombList
		#print "CombList: ", CombList
		min_set_cover(CombList)
	else:
		print "Minimum Set Cover: "
		combIndex=list(combIndex)
		for ind in combIndex:
			ind=list(ind)
			#print "ind: ", list(ind)
			for i in ind:
				#print ListOfSets[i]
				print PhotoIdsList[i]
	

########################### Test Cases Samples #####################################################
#Cover=[1,2,3,4,5,7,12,9]
#Cover=['a','b','c','d','e','f','g','h']
#CoverSet=set(Cover)
#ListOfSets=[set([1,2,4]), set([3,5,4]), set([1,2,5]), set([3,5,9]), set([7,12])]
#ListOfSets=[set(['a', 'b', 'd']), set(['c', 'd', 'e']), set(['c', 'e', 'h']), set(['f', 'g']), set(['a', 'f', 'g', 'h'])]

def main_part2():
	global CoverSet
	global ListOfSets
	global PhotoIdsList
	InputName=raw_input('Enter username: ')
########################## Fetching all photoids for given user #####################################
	PhotoIdsList=lib.fetch_photoids(InputName)

	TagCoverSet=set([])
	if PhotoIdsList: # process if PhotoIdsList is not empty
        	for pid in PhotoIdsList:
                	TempTagsList=lib.fetch_tags_for_photoid(pid)
	                TempTagsSet=set(TempTagsList)
        	        ListOfTagsSets.append(TempTagsSet)

        	#print "ListOfTagsSets: ", ListOfTagsSets
        	for sete in ListOfTagsSets:
                	TagCoverSet=TagCoverSet|sete

        	#print "TagCoverSet: ", TagCoverSet
	else:
        	print "Entered user has no photos"
        	sys.exit(0)

	ListOfSets=ListOfTagsSets
	CoverSet=TagCoverSet
	IndexList=[]

	#size=len(ListOfSets)
	size=len(ListOfSets)
	i=0
	for i in range(size):
        	IndexList.append(set([i]))

	#print "IndexList: ", IndexList
	if not IndexList:
        	print "Entered user has not set any tag"
	else:
		min_set_cover(IndexList)	

"""
########################## Fetching all photoids for given user #####################################
PhotoIdsList=lib.fetch_photoids(InputName)


if PhotoIdsList: # process if PhotoIdsList is not empty
	for pid in PhotoIdsList:
		TempTagsList=lib.fetch_tags_for_photoid(pid)
		TempTagsSet=set(TempTagsList)
		ListOfTagsSets.append(TempTagsSet)

	print "ListOfTagsSets: ", ListOfTagsSets

	for sete in ListOfTagsSets:
		TagCoverSet=TagCoverSet|sete

	print "TagCoverSet: ", TagCoverSet
else:
	print "Entered user has no photos"
	sys.exit(0)

ListOfSets=ListOfTagsSets
CoverSet=TagCoverSet
IndexList=[]

#size=len(ListOfSets)
size=len(ListOfSets)
i=0
for i in range(size):
	IndexList.append(set([i]))

#print "IndexList: ", IndexList
if not IndexList:
	print "Entered user has not set any tag"
else:
	main_part2()
	#min_set_cover(IndexList)	
"""
