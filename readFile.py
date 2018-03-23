#定义爬虫打开文件获取每一行地址
#被打开的文件必须是文件文件
#每行一个地址，每一行后需要有回画符

import  chardet

# 定义文件读取函数
def getFileName(fileName):
    f = open(fileName, 'rb')
    f_encoding = chardet.detect(f.read())['encoding']
    f.close()

    # 打开目标文件，将文件内容读取到内存中
    f_open = open(file=fileName, mode='r+', encoding=f_encoding)
    sline = f_open.readlines()
    return sline


# 定义日志文件读写
def logFileName(fileName,logCon):
    f = open(fileName, 'rb')
    f_encoding = chardet.detect(f.read())['encoding']
    f.close()

    # 打开目标文件，将文件内容读取到内存中
    f_open = open(file=fileName, mode='a+', encoding=f_encoding)
    f_open.write(logCon)