import urllib3
import re
import os

info ='''
------------- 操作列表 -------------
该程序是为抓取TN网站中商品类别下\n
的所有商品链接，以供main.py使用。\n
注意，抓取内容会替换原文件的记录！
--------------------------------------
'''
print(info)

inputUrl =input('请输入要商品类别的地址：')
fileAddress = input('请输入存储地址的文件名称，不需写文件后缀：')

#定义要抓取的地址
webUrl = inputUrl
#定义网站主地址
mainUrl='http://www.t-nani.co.kr'

#获取抓去地址中的内容
http = urllib3.PoolManager()
r = http.request('GET', webUrl);

#开始查找所有/shop/shopdetail.html开头的链接
link_list =re.findall(r"(?<=href=\")/shop/shopdetail.html.+?(?=\")" ,str(r.data))

#创建目录
position = 'c:\\sonyoonjoo\\TN\\'
if not os.path.isdir(position):
    os.makedirs(position)

# 开始写文件
f = position+fileAddress+'.txt'
if os.path.exists(f) :
    f_open = open(file=f, mode='a', encoding='utf-8')
    count=0
    for url in link_list:
        f_open.write(mainUrl + url + '\n')
        count+= 1
    f_open.close()
    print('完成操作，已经将'+str(count)+'条记录存储到“'+f+'”文件中，请查收。')
else:
    f_open = open(file=f, mode='w+', encoding='utf-8')
    count = 0
    for url in link_list:
        f_open.write(mainUrl + url + '\n')
        count += 1
    f_open.close()
    print('完成操作，已经将' + str(count) + '条记录存储到“' + f + '”文件中，请查收。')