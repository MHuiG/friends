# -*- coding: utf-8 -*-

import requests
import yaml
import random
requests.packages.urllib3.disable_warnings()

def load_config():
    f = open('_config.yml', 'r',encoding='gbk')
    ystr = f.read()
    ymllist = yaml.load(ystr, Loader=yaml.FullLoader)
    return ymllist

# 反反爬虫
def getRandUa():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                    '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua

def get_data(link):
    config = load_config()
    result = ''
    header = {
      'User-Agent': getRandUa(),
      "Connection": "close",
      }
    try:
        requests.adapters.DEFAULT_RETRIES = 55
        s = requests.session()
        s.keep_alive = False # 关闭多余连接
        r = s.get(link, headers=header, timeout=config['request']['timeout'],verify=False)
        s.close()
        r.encoding = 'utf-8'
        result = r.text.encode("gbk", 'ignore').decode('gbk', 'ignore')
        if str(r) == '<Response [404]>':
            result = 'error'
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])
        print(e.__traceback__.tb_lineno)
        result = 'error'
    return result

