# coding=utf-8

import requests
import time

#请填写此处字段
USERNAME = "??"
PASSWORD = "??"
FORMDATA1 = '??' #单引号
FORMDATA2 = '??' #单引号

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
        elif "操作成功" in retstr:
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
    