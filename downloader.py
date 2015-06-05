# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
from collections import OrderedDict
import time
import os
import json

# dict JSONObject
class JSONObject:
     def __init__(self, d):
         self.__dict__ = d

# spider class
class Spider:
    def __init__(self):
        self.searchEngine = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&userip=172.19.207.64&rsz=large&as_filetype=jpg&q="
        self.dirname = ""
        self.urlList = []

    #get countents by keyword
    def getContents(self,keyword):
        self.dirname = keyword
        try:
            data = json.loads(urllib.request.urlopen((self.searchEngine+urllib.parse.quote(keyword))).read().decode('utf-8'), object_hook=JSONObject)
            for item in data.responseData.results:
                self.urlList.append(item)
            return True
        except urllib.error.HTTPError as e:
            print(e.code)

    #save image to disc
    def saveImage(self):
        save_path = self.dirname
        isExists = os.path.exists(save_path)
        if not isExists:
            os.makedirs(save_path)

        for i in range(len(self.urlList)):
            try:
                urllib.request.urlretrieve(self.urlList[i].url, save_path+"/"+str(time.time())+".jpg")
            except:
                print(self.urlList[i].url+" を見つからない！！！！")



if __name__ == '__main__':
    spider = Spider()
    # input keyword
    print("キーワードを入力してください")
    keyword = input()
    if not len(keyword)<1:
        # seach by 堀北真希
        if spider.getContents(keyword):
            # dataを取れると保存する
            spider.saveImage()
        else:
            # 見つからない
            print("コンテンツを見つからへん！")
