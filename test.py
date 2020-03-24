# coding=utf-8

import requests

def login:
    pass

def get_session():
    pass

def final_update():
    load_data = 'ismoved=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&sfxk=0&xkqq=&uid=40448&date=20200324&tw=3&sfcxtz=0&sfyyjc=0&jcjgqr=0&jcjg=&sfjcbh=0&sfcxzysx=0&qksm=&remark=&address=%E5%90%89%E6%9E%97%E7%9C%81%E9%95%BF%E6%98%A5%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E6%A1%82%E6%9E%97%E8%A1%97%E9%81%93%E7%AB%8B%E4%BF%A1%E8%A1%97662%E5%8F%B7&area=%E5%90%89%E6%9E%97%E7%9C%81+%E9%95%BF%E6%98%A5%E5%B8%82+%E6%9C%9D%E9%98%B3%E5%8C%BA&province=%E5%90%89%E6%9E%97%E7%9C%81&city=%E9%95%BF%E6%98%A5%E5%B8%82&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22P%22%3A43.870369194879%2C%22O%22%3A125.320998535157%2C%22lng%22%3A125.320999%2C%22lat%22%3A43.870369%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get+ipLocation+failed.Get+geolocation+success.Convert+Success.Get+address+success.%22%2C%22accuracy%22%3A65%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%220431%22%2C%22adcode%22%3A%22220104%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E6%A1%82%E6%9E%97%E8%B7%AF%22%2C%22id%22%3A%22220104%22%2C%22location%22%3A%7B%22P%22%3A43.867444%2C%22O%22%3A125.31685500000003%2C%22lng%22%3A125.316855%2C%22lat%22%3A43.867444%7D%7D%2C%7B%22name%22%3A%22%E6%B0%B8%E6%98%8C%22%2C%22id%22%3A%22220104%22%2C%22location%22%3A%7B%22P%22%3A43.877416%2C%22O%22%3A125.316822%2C%22lng%22%3A125.316822%2C%22lat%22%3A43.877416%7D%7D%2C%7B%22name%22%3A%22%E8%A7%A3%E6%94%BE%E5%A4%A7%E8%B7%AF%22%2C%22id%22%3A%22220102%22%2C%22location%22%3A%7B%22P%22%3A43.878821%2C%22O%22%3A125.330987%2C%22lng%22%3A125.330987%2C%22lat%22%3A43.878821%7D%7D%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E7%AB%8B%E4%BF%A1%E8%A1%97%22%2C%22streetNumber%22%3A%22662%E5%8F%B7%22%2C%22province%22%3A%22%E5%90%89%E6%9E%97%E7%9C%81%22%2C%22city%22%3A%22%E9%95%BF%E6%98%A5%E5%B8%82%22%2C%22district%22%3A%22%E6%9C%9D%E9%98%B3%E5%8C%BA%22%2C%22township%22%3A%22%E6%A1%82%E6%9E%97%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E5%90%89%E6%9E%97%E7%9C%81%E9%95%BF%E6%98%A5%E5%B8%82%E6%9C%9D%E9%98%B3%E5%8C%BA%E6%A1%82%E6%9E%97%E8%A1%97%E9%81%93%E7%AB%8B%E4%BF%A1%E8%A1%97662%E5%8F%B7%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&created=1585020295&sfzx=0&sfjcwhry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&sftjwh=0&sftjhb=0&fxyy=&bztcyy=&fjsj=0&sfjchbry=0&sfjcqz=&jcqzrq=&jcwhryfs=&jchbryfs=&xjzd=&szgj=&sfsfbh=0&jhfjsftjwh=0&jhfjsftjhb=0&szsqsfybl=0&sfygtjzzfj=0&gtjzzfjsj=&sfsqhzjkk=0&sqhzjkkys=&created_uid=22739&id=1475714&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy='
    resp = requests.post(
        "https://app.bupt.edu.cn/ncov/wap/default/save",
        headers={
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
            "Cookie": "eai-sess=6go73jlj9acu4q5ck80ghs5e81; UUkey=6d68fd1dc1939574c14068aa9f0c2247; Hm_lvt_48b682d4885d22a90111e46b972e3268=1585031383; Hm_lpvt_48b682d4885d22a90111e46b972e3268=1585038501"
        },
        data=load_data);

    print(resp.text.encode("utf-8"));

update()
    
