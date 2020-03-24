# BUPT 疫情防控通 Robot

自动化运行的脚本，帮助你从疫情防控通的填报中解放出来。

## 使用方法

首先需要打开`autoUpdate.py`文件，修改几处参数

首先将用户名和密码修改一下

```
USERNAME = "xxxxxxxxx"
PASSWORD = "xxxxxx"
```

然后下面有两个奇怪的参数`FORMDATA1`和`FORMDATA2`，这两个参数非常关键，请按照下面步骤进行修改。

### 第一步 获取信息

登录我们的[填报网站](https://app.bupt.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex)，把信息都填好，地理位置也点击获取一下，注意！不要点击提交

接下来复制这段代码

```javascript
$.ajax({
                            url: '/ncov/wap/default/save',
                            type: 'POST',
                            dataType: 'JSON',
                            data: vm.info,
                            success: function (resp) {
                                _this.ajaxLock = false;
                                waploading('hide');
                                if(resp.e == 0) {
                                    wapalert('提交信息成功');
                                    _this.hasFlag = 1;
                                }else {
                                    wapalert(resp.m);
                                }
                            },
                            error: function () {
                                _this.ajaxLock = false;
                                waploading('hide');
                                wapalert('系统繁忙，请稍后再试！');
                            }
                        });
```

打开你的浏览器开发者模式（一般是F12），找到其中的`控制台`功能，将刚才的代码复制进去

![](https://ww1.yunjiexi.club/2020/03/24/bi8U0.png)

注意哦，这个时候点击`网络`选项，再回到控制台，点击回车执行。然后回到网络选项，往下翻到一个POST方法，资源是save的请求。

![](https://ww1.yunjiexi.club/2020/03/24/bi4St.png)

点开它，把POST的信息复制下来，就是我们需要的了。（学过计网的同学都知道POST是什么的吧！）

![](https://ww1.yunjiexi.club/2020/03/24/biI8a.png)

### 第二步 分隔一下

我们刚刚获取的那个字符串大概长这样

```
ismoved=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&sfxk=0&xkqq=&uid=40448&date=20200324&tw=3...好长好长
```

今天是几号？比如今天是`2020年3月24日`，你只需要搜索一下`20200324`的位置，把它删掉，它前面的复制到`FORMDATA1`，后面的复制到`FORMDATA2`就可以了。注意双引号哦

```
FORMDATA1 = "ismoved=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&sfxk=0&xkqq=&uid=40448&date="
FORMDATA2 = "&tw=3...好长好长"
```

### 第三步 启动

首先需要python3环境。

然后要安装一些依赖

```bash
pip install -r requirements.txt
```

（如果不行的话就把pip换成pip3）

最后直接运行就可以了。

```
python autoUpload.py
```

（不行的话就把python换成python3）

这个命令行框框不退出，程序就可以一直运行了，自动检测时间进行打卡。

后面是我对网页的分析，不重要~

## 网页分析

```
登录网址: https://app.bupt.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex
这里会setcookie一次，登录后，这个session才可以使用
填报网址: https://app.bupt.edu.cn/ncov/wap/default/index
需要登录的session
```

首先setcookie，然后看核心js（Vue编写）

```javascript
$.ajax({
                        type: "POST",
                        cache: false,
                        url: '/uc/wap/login/check',
                        data: {
                            username: vm.username,
                            password: vm.password,
                        },
                        dataType: 'json',
                        success: function (resp) {
                            if (resp.e == '0') {
                                window.location.href = vm.redirect_url;
                            } else if (resp.e == '10016') {
                                wapalert(resp.m);
                            } else {
                                wapalert(vm.setting.login_error || resp.m);
                            }
                            vm.locked = false;
                        },
                        error: function () {
                            vm.locked = false;
                        }
                    });
```

改一下

```javascript
$.ajax({
                        type: "POST",
                        cache: false,
                        url: '/uc/wap/login/check',
                        data: {
                            username: "...",
                            password: "...",
                        },
                        dataType: 'json',
                        success: function (resp) {
                            if (resp.e == '0') {
                                window.location.href = vm.redirect_url;
                            } else if (resp.e == '10016') {
                                wapalert(resp.m);
                            } else {
                                wapalert(vm.setting.login_error || resp.m);
                            }
                            vm.locked = false;
                        },
                        error: function () {
                            vm.locked = false;
                        }
                    });
```

发现check的api在这里

```
https://app.bupt.edu.cn/uc/wap/login/check
```

填报的网址找关键ajax

```javascript
$.ajax({
                            url: '/ncov/wap/default/save',
                            type: 'POST',
                            dataType: 'JSON',
                            data: vm.info,
                            success: function (resp) {
                                _this.ajaxLock = false;
                                waploading('hide');
                                if(resp.e == 0) {
                                    wapalert('提交信息成功');
                                    _this.hasFlag = 1;
                                }else {
                                    wapalert(resp.m);
                                }
                            },
                            error: function () {
                                _this.ajaxLock = false;
                                waploading('hide');
                                wapalert('系统繁忙，请稍后再试！');
                            }
                        });
                       
```

