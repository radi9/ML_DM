#Data feed ::  Data format: UserID::MovieID::Rating::Timestamp

#all fucntion is test is ok...but for r1.train ....it's performance bottleneck

from sys import getsizeof
from numpy import matrix


def getUser_dict(array):
	#get user's movie rating and movie ever see
	my_dict = dict()
	for lines in array:
		if lines[0] in my_dict :
			temp = my_dict[lines[0]]
			#the "::" means next reference "," means movie and score pair
			my_dict.update({lines[0] : temp+'::'+lines[1]+','+lines[2]})
		else :
			my_dict.update({lines[0] : lines[1]+','+lines[2]})
	return my_dict

def getData(source):
	temp = []
	for lines in source :
		temp.append(lines.split('::'))
	return temp

def getList(array,type):
	temp = []
	if type == 'user':
		typeID = 0
	elif type == 'movie':
		typeID = 1
	else :
		print 'error type id'
	
	temp.append(array.pop()[typeID])
	for elements in array :
		if elements[typeID] not in temp :
			temp.append(elements[typeID])
	temp.sort()
	return temp

def get_UserRate(userID,source):
	user_rate = []
	pair = dict()
	
	for line in source :
		if line[userID] == userID :
			 pair.update({line[movieID] : line[rating]})
	return pair

def createMatrix():
	

_source = '/home/red/ML_DM data/ml-10M/'

train_data = getData(open(_source+'r1.train','r+'))

user_list = getList(train_data,'user')

movie_list = getList(train_data,'movie')

a_write = open(_source+'r1.userID','w')




"user_dict = dict({x: '' for x in user_list})#my dictionary"

"""print mydict
user_list = getList(train_data)
train_list = getList(test_data)

print len(user_list)
print user_list"""



