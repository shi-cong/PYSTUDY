import logging
import requests
import random
import threading
import time
from sclib.html_parserlib import XpathParser, ReParser


class Job51Spider:
    TruthVisitPath = ['index', 'login']

    def __init__(self):
        self.visitePath = []
        self.session = requests.session()
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=100, pool_maxsize=100)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)

    def index(self):
        self.visitePath.append('index')

        url = 'http://www.51job.com/'
        headers = {
            'Host': 'www.51job.com',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-self.session': '1',
            'User-Agent': 'Golang',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        r = self.session.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            logging.info('%r - 访问主页成功!' % r.status_code)
            return r.cookies
        else:
            raise Exception('%r - 访问主页失败.' % r.status_code)

    def login(self, user, password, requestCookie):
        self.visitePath.append('login')
        url = 'http://login.51job.com/ajax/login.php'
        formData = {
            'action': 'save',
            'from_domain': 'i',
            'lang': 'c',
            'loginname': user,
            'password': password,
            'verifycode': '',
            'isread': 'on'
        }
        headers = {
            'Host': 'login.51job.com',
            'Origin': 'http://www.51job.com',
            'Upgrade-Insecure-self.session': '1',
            'User-Agent': 'Golang',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.51job.com/',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
        }
        r = self.session.post(url, data=formData, headers=headers, cookies=requestCookie)
        if r.status_code == 200:
            logging.info('%r - 登录成功!' % r.status_code)
            logging.debug(r.text)
            return r.cookies
        else:
            raise Exception('%r - 登录失败.' % r.status_code)

    def search(self, keyword, requestCookie, page=1):
        self.visitePath.append('search page %r' % page)
        url = 'http://search.51job.com/list/040000%252C030200%252C020000%252C010000,000000,0000,00,9,99,' + keyword + ',2,' + str(
            page) + '.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        headers = {
            'Host': 'search.51job.com',
            'Upgrade-Insecure-self.session': '1',
            'User-Agent': 'Golang',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.51job.com/',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
        }
        r = self.session.get(url, headers=headers,
                             cookies=requestCookie, allow_redirects=False)
        if r.status_code == 200:
            logging.info('%r - Search successfully!' % r.status_code)
            r.encoding = 'gbk'
            xp = XpathParser(text=r.text)
            if page == 1:
                rp = ReParser('[0-9]+')
                numJobsHtml = xp.xpath('//*[@id="resultList"]/div[1]/div[3]/text()').extract_first()
                numJobs = int(rp.compute(numJobsHtml))
                self.numJobs = numJobs
            jobsIdHtml = xp.xpath('//div[@class="el"]/p[@class="t1 "]')[:-1]
            companyHtml = xp.xpath('//div[@class="el"]/span[@class="t2"]')[:-1]
            addrHtml = xp.xpath('//div[@class="el"]/span[@class="t3"]')[:-1]
            moneyHtml = xp.xpath('//div[@class="el"]/span[@class="t4"]')[:-1]
            dateHtml = xp.xpath('//div[@class="el"]/span[@class="t5"]')[:-1]
            n = 0
            while n < len(jobsIdHtml):
                jobId = jobsIdHtml[n].xpath('./input/@value').extract_first()
                job_name = jobsIdHtml[n].xpath('./span/a/@title').extract_first('')
                company = companyHtml[n].xpath('./a/@title').extract_first('')
                company_link = companyHtml[n].xpath('./a/@href').extract_first('')
                addr = addrHtml[n].xpath('./text()').extract_first('')
                money = moneyHtml[n].xpath('./text()').extract_first('')
                date = dateHtml[n].xpath('./text()').extract_first('')
                print('%-25s%-25s%-20s%-10s%-10s' % (job_name, company, addr, money, date), end=' ')
                # job = Job(site='前程无忧', name=job_name, company=company, url=company_link, addr=addr, how_much=money, publish_date=date)
                # if not Job.has('前程无忧', job_name, company):
                #     Job.add_job(job)
                if jobId:
                    self.submitJob(jobId, url, r.cookies)
                n += 1
        else:
            raise Exception('%r - 搜索失败' % r.status_code)

    def submitJob(self, jobId, referer, requestCookie):
        url = 'http://my.51job.com/my/delivery/delivery.php?rand=' + str(
            random.random()) + '&jsoncallback=jQuery18305740801100126356_1496936607495&jobid=(' + jobId + '%3A0)&prd=search.51job.com&prp=01&cd=search.51job.com&cp=01&resumeid=&cvlan=&coverid=&qpostset=&elementname=delivery_jobid&deliverytype=2&deliverydomain=http%3A%2F%2Fmy.51job.com&language=c&imgpath=http%3A%2F%2Fimg02.51jobcdn.com&_=1496938008708'
        headers = {
            'Host': 'my.51job.com',
            'User-Agent': 'Golang',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Referer': referer
        }
        r = self.session.get(url, headers=headers, cookies=requestCookie, allow_redirects=False)
        r.encoding = 'gbk'
        if r.status_code == 200:
            err = 0
            if 'deliverySuccessLayer' in r.text:
                err = 1
                logging.info('%r - 简历投递成功!' % r.status_code)
            elif 'deliveryHasApplyLayer' in r.text:
                err = 2
                logging.info('%r - 简历已经投递过了!' % r.status_code)
                # raise Exception(r.text)
            else:
                err = 3
                logging.info('%r - 简历投递失败!' % r.status_code)
                logging.debug(('%r' % r.text))
                # raise Exception(r.text)
            if err == 0:
                print('成功')
            elif err == 2:
                print('无法重复申请')
            elif err == 3:
                print('失败')


def main():
    logging.info('作为我堂堂中华IT技术宅男，找工作何须亲自动手，双击运行程序即可')
    logging.info('就是喜欢电话被打爆的感觉。')

    j5s = Job51Spider()
    reqc = j5s.index()
    reqs = j5s.login('15800223273', 'sc501314', reqc)
    j5s.search('python', reqs)

    p = 1
    tmp = j5s.numJobs // 50 + 1 if j5s.numJobs % 50 == 0 else j5s.numJobs // 50
    logging.info('职位共有页数: %r; 总职位数: %r' % (tmp, j5s.numJobs))
    time.sleep(10)
    p = 2

    while p <= tmp:
        try:
            j5s.search('python', reqs, p)
        except:
            continue
        p += 1

logging.basicConfig(level=logging.DEBUG)
main()
