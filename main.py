import  readFile
import  tn
import  ro
import bp

info = '''
------------- 操作列表 -------------
| BP：     http://babinpumkin.com/
| RO：    http://roer.co.kr/
| TN：    http://www.t-nani.co.kr/
| Q ：     退出
--------------------------------------
'''
print(info)

exit_flag =True

while exit_flag :

    selectItem = input('请根据上表键入需要抓取的网站的名称，按Q键退出程序：')

    if selectItem=="bp" or selectItem=="BP" :
        inputFileLocal = input('输入BP文件位置：')
        for i in readFile.getFileName(inputFileLocal):
            bp.savePicFile(i)
        print(info)

    elif selectItem=="ro" or selectItem=="RO" :
        inputFileLocal = input('输入RO文件位置：')
        for i in readFile.getFileName(inputFileLocal):
            ro.savePicFile(i)
        print(info)

    elif selectItem=="tn" or selectItem=="TN" :
        inputFileLocal = input('输入TN文件位置：')
        for i in readFile.getFileName(inputFileLocal):
            tn.savePicFile(i)
        print(info)

    elif  selectItem=="q" or selectItem=="Q" :
        print("感谢使用，祝愉快！")
        break

    else:
        input("请输入正确的功能选择，按回车重新输入！")
        print(info)