from scrapy.selector import Selector
import requests
from requests.utils import dict_from_cookiejar, cookiejar_from_dict
import pprint
import time


class LiePagnationSpider:
    def __init__(self, cat_id, total_pages, customer):
        self.index = 'https://powell.com'
        self.session = requests.session()
        self.cat_id = cat_id
        self.total_pages = total_pages
        self.customer = customer

    def pagnation(self, url):
        i = 1
        EVENTVALIDATION, txtQtys, VIEWSTATE, aspnetForm = None, [], None, None
        while i <= self.total_pages:
            print('------------------------------------------------------------------- 页数：', i)

            try:
                html = self.page(url, i, EVENTVALIDATION, txtQtys, VIEWSTATE, aspnetForm)
                if 'erp' in html or 'ERP' in html or 'Erp' in html:
                    print('Erp服务器挂了')
                    time.sleep(300 * 2)
                    i -= 1
                else:
                    EVENTVALIDATION, txtQtys, VIEWSTATE, aspnetForm = self.parse_page(html, i)
            except Exception as e:
                print(e)

                if i == 1:
                    return

                self.session = requests.session()
                tmp = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                    'Referer': url,
                    'Host': 'powell.com',
                    'origin': 'https://powell.com',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Upgrade-Insecure-Requests': '1'
                }
                r = self.session.get(url, headers=tmp)
                EVENTVALIDATION, txtQtys, VIEWSTATE, aspnetForm = self.parse_page(r.text, 1)
                i -= 1

            # time.sleep(10)
            i += 1

    def page(self, url, page=0, EVENTVALIDATION=None, txtQtys=None, VIEWSTATE=None, aspnetForm=None):
        tmp = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'Referer': url,
            'Host': 'powell.com',
            'origin': 'https://powell.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests': '1'
        }

        if page != 1:
            if page <= 11:
                page = '0' + str(page - 1)
                if page == '010':
                    page = '10'
            elif page % 10 != 0:
                page = '0' + str(page % 10)
            else:
                page = '11'
            if page == '10':
                v1 = v2 = ''
            else:
                v1 = v2 = '0,0'
            WebForms = {
                '__EVENTTARGET': 'ctl00$CustomerMainContent$e2wItemLayout1$DataGrid2$ctl14$ctl' + page,
                '__EVENTARGUMENT': '',
                '__ctl00$e2wLeftMenu1$e2wt_SS': '',
                '__ctl00$e2wLeftMenu1$e2wt_ECS': '0;',
                '__ctl00$e2wLeftMenu1$e2wt_CHS': '',
                '__ctl00$e2wLeftMenu1$e2wt_SCS': v1,
                '__ctl00$e2wLeftMenu1$treeSelfService_SS': '',
                '__ctl00$e2wLeftMenu1$treeSelfService_ECS': '',
                '__ctl00$e2wLeftMenu1$treeSelfService_CHS': '',
                '__ctl00$e2wLeftMenu1$treeSelfService_SCS': v2,
                '__LASTFOCUS': '',
                '__VIEWSTATE': VIEWSTATE,
                'ctl00$hdnBaseUrl': 'https://www.powell.com',
                'ctl00$E2wHeader1$E2wSearchCatalog1$hdnDefaultSearchText': 'Search...',
                'ctl00$E2wHeader1$E2wSearchCatalog1$ddlSearchType': 'K',
                'ctl00$E2wHeader1$E2wSearchCatalog1$searchText': '',
                'ctl00$E2wHeader1$E2wSearchCatalog1$tbw1_Search_ClientState': '',
                'ctl00$E2wHeader1$LoginView1$txtUserId': '',
                'ctl00$E2wHeader1$LoginView1$tbw1_Userid_ClientState': '',
                'ctl00$E2wHeader1$LoginView1$txtPassword': '',
                'ctl00$E2wHeader1$LoginView1$tbw1_Password_ClientState': '',
                'ctl00$CustomerMainContent$e2wItemLayout1$ddlListPerPage': '10',
                'ctl00$CustomerMainContent$e2wItemLayout1$ddlSorting': 'ThirdItemNumber ASC',
                'ctl00$txtIEFixForEnterKey': '',
                '__VIEWSTATEGENERATOR': 'F0AD6DEA',
                '__EVENTVALIDATION': EVENTVALIDATION,
                '__SCROLLPOSITIONX': '0',
                '__SCROLLPOSITIONY': '1040'
            }
            print('===============', WebForms['__EVENTTARGET'])
            i = 3
            for element in txtQtys:
                tmp_s = '0' + str(i)
                if i >= 10:
                    tmp_s = str(i)
                WebForms['ctl00$CustomerMainContent$e2wItemLayout1$DataGrid2$ctl' + tmp_s + '$txtQty:' + element] = ''
                i += 1
            r = self.session.post(aspnetForm, data=WebForms, headers=tmp)
            return r.text
        else:
            r = self.session.get(url, headers=tmp)
            html = r.text
            return html

    def parse_page(self, html, page):
        res = Selector(text=html)
        # post url
        aspnetForm = self.index + res.xpath('//form[@name="aspnetForm"]/@action').extract_first()
        # 　表单参数
        __EVENTVALIDATION = res.xpath('//input[@name="__EVENTVALIDATION"]/@value').extract_first()
        __VIEWSTATE = res.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first()
        # if page > 10:
        #     __VIEWSTATE = __VIEWSTATE.split('+')[0]
        # print('__VIEWSTATE: ', __VIEWSTATE)
        txtQtys = []

        # 获取goods列表
        GridRows = res.xpath('//tr[@class="GridRow"]')
        GridAlternateRow = res.xpath('//tr[@class="GridAlternateRow"]')
        trs = GridRows + GridAlternateRow
        for tr in trs:
            tds = tr.xpath('./td')
            goods_thumb = tds[0].xpath('.//img/@src').extract_first()
            site_url = self.index + tds[1].xpath('.//a/@href').extract_first()
            goods_name = tds[1].xpath('./span/text()').extract_first()
            goods_desc = tds[2].xpath('./text()').extract_first('')
            provider_name = tds[-1].xpath('./text()').extract_first('')

            if site_url:
                txtQty = site_url.split('-')[-1]
                txtQtys.append(txtQty)
                goods = {
                    'cat_id': self.cat_id,
                    'goods_thumb': goods_thumb,
                    'site_url': site_url,
                    'goods_name': goods_name,
                    'goods_desc': goods_desc,
                    'provider_name': provider_name
                }
                print('Sent :', goods)
                if self.customer:
                    self.customer.storeData(str(goods))

        return __EVENTVALIDATION, txtQtys, __VIEWSTATE, aspnetForm


if __name__ == '__main__':
    d = {'cat_id': 533, 'page_count': 367,
         'url': 'https://powell.com/catalog/Products-2100000223/Connectors-3100017745/Military-3100017752/Space-Grade-3100017807/Mighty-Mouse-3100017808'}
    lps = LiePagnationSpider(cat_id=d['cat_id'], total_pages=d['page_count'], customer=None)
    lps.pagnation(url=d['url'])
