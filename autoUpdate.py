# coding=utf-8

import requests
import time

USERNAME = "2018213639"
PASSWORD = "1085455474"
FORMDATA1 = 'ismoved=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&sfxk=0&xkqq=&uid=40448&date='
FORMDATA2 = '&tw=3&sfcxtz=0&sfyyjc=0&jcjgqr=0&jcjg=&sfjcbh=0&sfcxzysx=0&qksm=&remark=&address=%E5%90%89%E6%9E%97%E7%9C%81%E9%95%BF%E6%98%A5%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E6%A1%82%E6%9E%97%E8%A1%97%E9%81%93%E5%90%8C%E5%85%89%E8%B7%AF5-9-3%E9%97%A8&area=%E5%90%89%E6%9E%97%E7%9C%81+%E9%95%BF%E6%98%A5%E5%B8%82+%E6%9C%9D%E9%98%B3%E5%8C%BA&province=%E5%90%89%E6%9E%97%E7%9C%81&city=%E9%95%BF%E6%98%A5%E5%B8%82&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22P%22%3A43.870060492622%2C%22O%22%3A125.32097195095503%2C%22lng%22%3A125.320972%2C%22lat%22%3A43.87006%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get+ipLocation+failed.Get+geolocation+success.Convert+Success.Get+address+success.%22%2C%22accuracy%22%3A65%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%220431%22%2C%22adcode%22%3A%22220104%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E6%A1%82%E6%9E%97%E8%B7%AF%22%2C%22id%22%3A%22220104%22%2C%22location%22%3A%7B%22P%22%3A43.867444%2C%22O%22%3A125.31685500000003%2C%22lng%22%3A125.316855%2C%22lat%22%3A43.867444%7D%7D%2C%7B%22name%22%3A%22%E6%B0%B8%E6%98%8C%22%2C%22id%22%3A%22220104%22%2C%22location%22%3A%7B%22P%22%3A43.877416%2C%22O%22%3A125.316822%2C%22lng%22%3A125.316822%2C%22lat%22%3A43.877416%7D%7D%2C%7B%22name%22%3A%22%E5%8D%97%E5%B2%AD%22%2C%22id%22%3A%22220102%22%2C%22location%22%3A%7B%22P%22%3A43.859268%2C%22O%22%3A125.33823899999999%2C%22lng%22%3A125.338239%2C%22lat%22%3A43.859268%7D%7D%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E5%90%8C%E5%85%89%E8%B7%AF%22%2C%22streetNumber%22%3A%225-9-3%E9%97%A8%22%2C%22province%22%3A%22%E5%90%89%E6%9E%97%E7%9C%81%22%2C%22city%22%3A%22%E9%95%BF%E6%98%A5%E5%B8%82%22%2C%22district%22%3A%22%E6%9C%9D%E9%98%B3%E5%8C%BA%22%2C%22township%22%3A%22%E6%A1%82%E6%9E%97%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E5%90%89%E6%9E%97%E7%9C%81%E9%95%BF%E6%98%A5%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E6%A1%82%E6%9E%97%E8%A1%97%E9%81%93%E5%90%8C%E5%85%89%E8%B7%AF5-9-3%E9%97%A8%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&created=1585020295&sfzx=0&sfjcwhry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&sftjwh=0&sftjhb=0&fxyy=&bztcyy=&fjsj=0&sfjchbry=0&sfjcqz=&jcqzrq=&jcwhryfs=&jchbryfs=&xjzd=&szgj=&sfsfbh=0&jhfjsftjwh=0&jhfjsftjhb=0&szsqsfybl=0&sfygtjzzfj=0&gtjzzfjsj=&sfsqhzjkk=0&sqhzjkkys=&created_uid=22739&id=1475714&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy='

def print_msg(msg,level=1):
    if level is 1:
        head = "[INFO]    "
    elif level is 2:
        head = "[DEBUG]   "
    elif level is 3:
        head = "[WARNING] "
    elif level is 4:
        head = "[ERROR]   "
    else:
        pass
    print(head+msg)

def get_login_cookies():

    try:
            # Find Page
        print_msg("开始获取登录Session")
        url = "https://app.bupt.edu.cn/uc/wap/login?"
        resp = requests.get(url)
        eai_sess = resp.headers['Set-Cookie'].split(";")[0]

        # Login 
        url2 = "https://app.bupt.edu.cn/uc/wap/login/check"
        data = "username="+USERNAME+"&password="+PASSWORD
        headers = {
            "Host":"app.bupt.edu.cn",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0 micromessager",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Origin":"https://app.bupt.edu.cn",
            "Connection":"keep-alive",
            "Referer":"https://app.bupt.edu.cn/uc/wap/login",
            "Cookie":eai_sess
        }
        resp2 = requests.post(url2,data=data,headers=headers)

        print_msg("Login Session Return: "+resp2.text)
        if "操作成功" in resp2.text:
            print_msg("登录session获取成功")
            return eai_sess
        else:
            print_msg("登录session获取失败！",3)
            return None
    except:
        print_msg("登录session获取失败！可能是网络问题",3)
        return None



def final_update():

    try:
            # Generate Payload
        date = time.strftime("%Y%m%d", time.localtime())
        load_data =FORMDATA1+date+FORMDATA2
        url = "https://app.bupt.edu.cn/ncov/wap/default/save"
        login_cookies = get_login_cookies()
        default_cookies = 'eai-sess=71f9l8oucr4ml62m696pgn0or6'
        headers = {
                "Host": "app.bupt.edu.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0 micromessenger",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Content-Length": "2633",
                "Origin": "https://app.bupt.edu.cn",
                "Connection": "keep-alive",
                "Referer": "https://app.bupt.edu.cn/ncov/wap/default/index?from=history",
                "Cookie":login_cookies
                }
        resp = requests.post(
            url=url,
            headers=headers,
            data=load_data
            );

        # Return
        retstr = resp.text
        print_msg("Update Session Return: "+retstr)
        if "今天已经填报了" in retstr:
            print_msg("确认填报完成。\n")
            return True
        elif "填报成功" in retstr:
            print_msg("填报成功，随后进行确认\n")
            return True
        else:
            print_msg("填报失败!\n")
            return False

    except:
        print_msg("填报失败了，可能是网络问题")
        return False

def update():
    print_msg("开始打卡进程\n")
    succ_time = 0

    for i in range(4):
        print_msg("第"+str(i+1)+"次测试：\n")
        if final_update() == True:
            succ_time += 1
        else:
            break
        time.sleep(5)

    if succ_time == 4:
        return True
    else:
        return False


def getTime():
    return (time.strftime("%Y%m%d",time.localtime()) , time.strftime("%H%M%S",time.localtime()))

def print_basic_info():
    print_msg("BUPT自动填表抗疫情脚本v1.0 by RaidriarB")
    print_msg("请在使用前先行确认，是否已经按照提示设置好Payload！",3)
    print_msg("如果没有正确设置Payload，打卡信息可能会出错，严重的话会被学校查水表哦！",3)
    time.sleep(1)
    print_msg("下面是您的参数:")
    print_msg("用户名："+USERNAME,2)
    print_msg("密码："+PASSWORD,2)
    #print_msg("POST发送的表单："+FORMDATA1+time.strftime("%Y%m%d",time.localtime())+FORMDATA2,2)
    time.sleep(2)
    print_msg("确认开启自动进程吗：(y/n)")
    key = input()
    if key == "y" or key == "Y":
        print_msg("准备开启自动打卡. . . . .")
        time.sleep(1)
    else:
        print_msg("正在关闭. . . . .")
        time.sleep(1)
        exit(1)

def main_loop():

    RELOAD = 5
    finish_date = ''
    total_succ = 0

    print_basic_info()

    while True:
        if getTime()[0] != finish_date:
            time.sleep(RELOAD)
            fin = update()
            if fin == True:
                finish_date = getTime()[0]
                total_succ += 1
                print_msg("今日打卡成功！累计打卡天数: "+str(total_succ))
                print_msg("程序还在运行，会自动检测打卡")
            else:
                print_msg("打卡出现问题，很快重新尝试",2)
                continue
        time.sleep(RELOAD)


main_loop()
    