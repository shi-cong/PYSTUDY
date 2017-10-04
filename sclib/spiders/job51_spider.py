from sclib.html_parserlib import XpathParser, ReParser
from sclib.requestslib import HTTP
from sclib.randomlib import random_small_number


class Job51Spider:
    def __init__(self):
        self.http = HTTP(session=True)

    def index(self):
        """
        访问首页
        主要是为了得到响应cookie
        :return:
        """
        url = 'http://51job.com/'
        headers = {
            'Host': '51job.com',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-self.session': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'ggzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
        }
        t, h, c, hi = self.http.get(url, headers=headers, allow_redirects=False)
        print(self.http.get_session_cookie())
        return c

    def login(self, user, password, cookies):
        url = 'http://login.51job.com/ajax/login.php'

        headers = {
            'host': "login.51job.com",
            'connection': "keep-alive",
            'content-length': "95",
            'cache-control': "no-cache",
            'origin': "http://www.51job.com",
            'upgrade-insecure-requests': "1",
            'content-type': "application/x-www-form-urlencoded",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'referer': "http://www.51job.com/",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
            'Cookie': 'NSC_usbdf.51kjohzjoh.dpn - 5 - 228 = ffffffffc3a018a945525d5f4f58455e445a4a423660'
            }
        formData = {
            'action': 'save',
            'from_domain': 'i',
            'lang': 'c',
            'loginname': user,
            'password': password,
            'verifycode': '',
            'isread': 'on'
        }
        t, h, c, hi = self.http.post(url, form_data=formData, headers=headers, cookies=cookies)
        print(t)

    def search(self, keyword, requestCookie, page=1):
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
        t, h, c, hi = self.http.get(url, headers=headers,
                             cookies=requestCookie, allow_redirects=False, encoding='gbk')
        xp = XpathParser(text=t)
        if page == 1:
            rp = ReParser()
            numJobsHtml = xp.xpath('//*[@id="resultList"]/div[1]/div[3]/text()').extract_first()
            numJobs = int(rp.compute('[0-9]+', numJobsHtml))
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
            if jobId:
                self.submitJob(jobId, url, c)
            n += 1

    def submitJob(self, jobId, referer, requestCookie):
        url = 'http://i.51job.com/delivery/delivery.php?'

        p = 'rand=' + str(random_small_number()) + '&jsoncallback=jQuery18302138634134253048_1507066246973&jobid=('+str(jobId) +'%3A0)&prd=search.51job.com&prp=01&cd=search.51job.com&cp=01&resumeid=&cvlan=&coverid=&qpostset=&elementname=delivery_jobid&deliverytype=2&deliverydomain=http%3A%2F%2Fi.51job.com&language=c&imgpath=http%3A%2F%2Fimg03.51jobcdn.com&_=1507068354931'
        headers = {
            'Host': 'i.51job.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'cookies': 'guid=15070646256806980017; _ujz=MTA5MTM4MDQ1MA%3D%3D; ps=us%3DXmRQOlQ2Vn4FYwFkB3xdbwc2BjFUfFA0AjwAZF0rAzIPMloxAGVXYVA3XzYAbF1sDT0CNFRkWzhcJlJCDXIEaV4%252BUG4%253D%26%7C%26needv%3D0; slife=resumeguide%3D1%26%7C%26lowbrowser%3Dnot%26%7C%26lastlogindate%3D20171004%26%7C%26; 51job=cuid%3D109138045%26%7C%26cusername%3Dphone_15728567842%26%7C%26cpassword%3D%26%7C%26cname%3D%25CA%25A9%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%25B4%25CF%26%7C%26cemail%3Dshi_cong%2540icloud.com%26%7C%26cemailstatus%3D3%26%7C%26cnickname%3D%25D3%25C7%25D3%25F4%25B5%25C4%25C3%25AB%25C3%25AB%26%7C%26ccry%3D.0wUMWp2Zl.as%26%7C%26cconfirmkey%3DshDPI9YPQYVPQ%26%7C%26cresumeids%3D.0VPKsW.6cwzk%257C%26%7C%26cautologin%3D1%26%7C%26cenglish%3D0%26%7C%26sex%3D0%26%7C%26cnamekey%3Dsh0zZQQixMXvI%26%7C%26to%3DDjdUP1A7ATZSMF05BWAGMQM1BntWIAI%252FXTRTbwlmBlkBOFQ6D2pWYlM6CWAGZVxoBD8EMVNnBSxXYFE2DTQBOQ4wVD9QMwE%252BUjBdNQ%253D%253D%26%7C%26; search=jobarea%7E%60040000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA040000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1507065072%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21'
        }
        

        t, h, c, hi = self.http.get(url+p, headers=headers, allow_redirects=False, encoding='gbk')
        if 'deliverySuccessLayer' in t:
            print('投递成功')
        elif 'deliveryHasApplyLayer' in t:
            print('已投递')
        else:
            print('失败', t)


def main(user='admin', password='123456'):
    j5s = Job51Spider()
    c = j5s.index()
    reqs = j5s.login(user, password, c)
    j5s.search('python', reqs)

    p = 1
    tmp = j5s.numJobs // 50 + 1 if j5s.numJobs % 50 == 0 else j5s.numJobs // 50
    p = 2

    while p <= tmp:
        try:
            j5s.search('python', reqs, p)
        except:
            continue
        p += 1

main()
