from bs4 import BeautifulSoup
import urllib.request as ure
import urllib.error as err
import os
from logfile import logFileName

fName= 'C:\sonyoonjoo\error.log'

def savePicFile(line):

    #将得到的地址中回车符去掉
    f_url = line.strip('\n')

    #定义抓去地址
    url = f_url

    #取得目录名称
    #url_list = url.split('/')
    #urlFolder = url_list[-1]

    folder = url.split("/")[-1]
    urlFolder = folder.split("product_no=")[-1][:5]

    # 连接目标地址，超过30秒放弃
    response = ure.urlopen(url, timeout=30)
    try:
        circle = response.read().decode('utf-8')

        # 将获取的图片地址依次放入count中
        count = []
        # 将获取的网页内容放入BeautifulSoup
        soup = BeautifulSoup(circle, 'lxml')
        # 根据谷歌SelectGadGet这个插件，获取html标签，比如获取：#gallery-list
        for item in soup.select('.productdetail'):
            # 用bs4中的find_all获取 cc标签中是否存在 img这个标签,limit:限制爬取的数量。
            print('正在获取' + '\033[0;31;0m\t' + urlFolder + '\033[0m' + '商品的图片信息，请等待...')
            for img in item.find_all('img', limit=50):

                # src 是 img标签中存在的属性
                img_src =img.get('src')

                if img_src.split("/")[-1][-3::] == 'jpg' :

                    # img_path = 'http://babinpumkin.com' + img.get('src')
                    # count.append(img_path)

                    if img_src[0:2] == '//' :
                        img_path = 'http:'+img.get('src')
                        count.append(img_path)
                    else:
                        img_path = 'http://babinpumkin.com' + img.get('src')
                        count.append(img_path)

        # 用enumerate依次取出count中的图片地址 放入v中
        for i,v in enumerate(count):
            #创建目录
            position = 'c:\\sonyoonjoo\\BP\\'+urlFolder+'\\'
            if not os.path.isdir(position):
                os.makedirs(position)
            path = position+str(i)+'.jpg'

            # 存取图片过程中，出现不能存储 int 类型，故而，我们对他进行类型转换 str()。w:读写方式打开，b：二进制进行读写。图片一般用到的都是二进制。
            with open(path, 'w') as file:
                try:
                    ure.urlretrieve(v, path)
                except err.URLError :
                    print('出错了！已经将错误信息写入'+fName+'文件中，请查收。')
                    logFileName(fName,'商品编码：'+urlFolder+'，地址\"'+v+'\"无法正常连接！\n')
            print('正在抓取产品编号为' + '\033[0;31;0m\t'+urlFolder +'\033[0m' + '的第' + '\033[0;32;0m\t'+str(i + 1) +'\033[0m'+ '张图片')
    except (UnicodeDecodeError, UnboundLocalError):
        print('出错了！已经将错误信息写入' + fName + '文件中，请查收。')
        logFileName(fName, '商品编码：' + urlFolder + '，该页面编码不可识别，请手动下载该页面中的图片内容。\n')