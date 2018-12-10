# -*-coding: utf-8-*-
import requests

# 该全局变量代表请求成功后服务端返回的数据
response = ''


def login(stuNum, password, checkcode, cookie):
    # 发起登陆请求的url
    url = 'http://222.24.62.120/default2.aspx'
    # 登陆时http报文需要传输的数据
    body = {'__VIEWSTATE': 'dDwxNTMxMDk5Mzc0Ozs+lYSKnsl/mKGQ7CKkWFJpv0btUa8=',
            'txtUserName': stuNum,
            'Textbox1': '',
            'TextBox2': password,
            'txtSecretCode': checkcode,
            'RadioButtonList1': 'ѧ��',
            'Button1': '',
            'lbLanguage': '',
            'hidPdrs': '',
            'hidsc': ''}
    # 该请求的请求头
    headers = {'Host': '222.24.62.120',
               'Content-Length': str(body.__len__()),
               'Cache-Control': 'max-age=0',
               'Upgrade-Insecure-Requests': '1',
               'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Referer': 'http://222.24.62.120/default2.aspx',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Proxy-Connection': 'keep-alive'}

    cookie = {'ASP.NET_SessionId': cookie}

    # 返回该次请求的结果
    s = requests.session()
    response = s.post(url=url, data=body, headers=headers, cookies=cookie)
    return judge_request_result(result=response)


# 判断该次请求的结果
def judge_request_result(result):
    response_text = result.text
    # 通过请求返回的数据包的请求头来判断该次请求是否成功
    if ('P3P' in result.headers):
        # 如果请求失败根据返回数据包的body判断请求失败的类型
        if (response_text.__contains__('密码错误')):
            # 如果请求失败就将结果数据赋空值
            global response
            response = ''
            return 'password error'
        if (response_text.__contains__('验证码不正确')):
            # 如果请求失败就将结果放数据赋空值
            response = ''
            return 'checkcode error'
        return 'unknown error'
    else:
        # 更新全局变量的值
        response = response_text
        return 'pass'
