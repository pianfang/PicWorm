import  chardet

# 定义文件读取函数
def logFileName (fileName, logCon):
    f = open(fileName, 'rb')
    f_encoding = chardet.detect(f.read())['encoding']
    f.close()

    # 打开目标文件，将文件内容读取到内存中
    f_open = open(file=fileName, mode='a+', encoding=f_encoding)
    f_open.write(logCon)