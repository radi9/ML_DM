#Data feed ::  Data format: UserID::MovieID::Rating::Timestamp

from numpy import matrix
from sys import getsizeof

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

def accessFile(path,property):
    file = open(path,property)
    return file

def output_record(fileSource,fileObject):
    count = 0
    for lines in fileSource :
        count += 1
        fileObject.write(str(count)+'\t'+lines+'\n')
    return fileObject


#Get the data property and test here

#write the user and movie list into file for validation or something..
#if this program logical is correct then the file r1.userID and r1.moveID have the correct data

#next time we could verify the data or use the data by read the file ,it is more shorter than original r1.train data set

_source = '/home/red/ML_DM data/ml-10M/'

train_data = getData(accessFile(_source+'r1.train','r+'))

user_list = getList(train_data,'user')

movie_list = getList(train_data,'movie')

write_userList = accessFile(_source+'r1.userID','w')

write_movieList = accessFile(_source+'r1.movieID','w')

write_out_userList = output_record(user_list,write_userList)

write_out_userList.close()

write_out_movieList = output_record(movie_list,write_movieList)

write_out_movieList.close()

    
print len(user_list) #55682
print len(movie_list) #10665

print 'this train data size is '+str(getsizeof(train_data)) #32208576 bytes
print 'this user list size is '+str(getsizeof(user_list))   #228676
print 'this movie list size is '+str(getsizeof(movie_list)) #43812

user_records = getUser_dict(train_data)

write_user_records = accessFile(_source+'r1user.record','w')

write_out_user_records = output_record(user_records,write_user_records)

write_out_user_records.close()


"print user_records['15555']"
#print NO.15555 user records

#all fucntion is test is ok...but for r1.train ....it's performance bottleneck




