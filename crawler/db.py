#encoding=utf-8
import urllib
import time
import json
import my_common
from pymongo import *

client = MongoClient('localhost', 27017)
db = client.statistics
#collection = db.videoInfo
#print collection
#
#mydict = {'title' : 'aa', 'link' : 'http://www.baidu.com', 'channel' : 'bb', 'playCount' : '10', 'uploadTime' : '2017-03-30'}
#collection.insert(mydict)

#collection = db.videoDailyCount
#print collection

#mydict = {'videoId' : '58e9a6533bbe5945505086e5', 'playCount' : '10', 'date' : '2017-03-30'}
#collection.insert(mydict)


#print collection.find_one({'channel' : 'bbb'})
#print len(collection.find({'channel' : 'bb'}))

def find_videoInfo(info_dict):
    collection = db.videoInfo
    result = collection.find_one({'link' : info_dict['link'], 'channel' : info_dict['channel']})

    return result


def find_videoDailyCount(videoId, date):
    collection = db.videoDailyCount
    result = collection.find_one({'videoId' : videoId, 'date' : date})
    
    return result


def insert_db(info_dict):
    collection = db.videoInfo
    result_dict = find_videoInfo(info_dict)
    if result_dict != None:
        result_dict['playCount'] = info_dict['playCount']
        result_dict['uploadTime'] = info_dict['uploadTime']
        collection.save(result_dict)
    else:
        collection.insert(info_dict)
        
    
    result_dict = find_videoInfo(info_dict)
    #print result_dict['_id'] 
    collection1 = db.videoDailyCount
    result1_dict = find_videoDailyCount(result_dict['_id'], my_common.get_current_time())
    if result1_dict != None:
        result1_dict['playCount'] = info_dict['playCount']
        collection.save(result1_dict)
    else:
        tmp_dict = {'videoId' : result_dict['_id'], 'date' : my_common.get_current_time(), 'playCount' : result_dict['playCount']}
        collection1.insert(tmp_dict)



if __name__ == '__main__':
    mydict = {'title' : 'aa', 'link' : 'http://www.baidu.com', 'channel' : 'bb', 'playCount' : '11', 'uploadTime' : '2017-03-30'}
    print find_videoInfo(mydict)
    #print find_videoDailyCount('58e9a6533bbe5945505086e5')
    print insert_db(mydict)
    pass

