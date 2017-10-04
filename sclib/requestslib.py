"""
requestsÄ£¿é
"""
import requests
from collections import OrderedDict
from requests.utils import dict_from_cookiejar


class HTTP(object):
    def __init__(self, session=False):
        if session:
            self.session = requests.Session()

            adapter = requests.adapters.HTTPAdapter(
                pool_connections=100, pool_maxsize=100)
            self.session.mount('http://', adapter)
            self.session.mount('https://', adapter)

    def close(self):
        if self.session:
            self.session.close()

    def get_session_cookie(self):
        if self.session:
            return dict_from_cookiejar(self.session.cookies)

    def get(self,
            url,
            headers=None,
            cookies=None,
            timeout=30,
            verify=False,
            proxies=None,
            allow_redirects=True,
            encoding='utf-8'):
        if self.session:
            r = self.session.get(url,
                                 headers=OrderedDict(headers),
                                 cookies=cookies,
                                 timeout=timeout,
                                 verify=verify,
                                 proxies=proxies,
                                 allow_redirects=allow_redirects)
            r.raise_for_status()
            r.encoding = encoding
            return r.text, r.headers, dict_from_cookiejar(r.cookies), r.history
        else:
            r = requests.get(url,
                             headers=OrderedDict(headers),
                             cookies=cookies,
                             timeout=timeout,
                             verify=verify,
                             proxies=proxies,
                             allow_redirects=allow_redirects)
            r.raise_for_status()
            r.encoding = encoding
            return r.text, r.headers, dict_from_cookiejar(r.cookies), r.history

    def get_img(self,
            url,
            headers=None,
            cookies=None,
            timeout=30,
            verify=False,
            proxies=None,
            allow_redirects=True):
        if self.session:
            r = self.session.get(url,
                                 headers=OrderedDict(headers),
                                 cookies=cookies,
                                 timeout=timeout,
                                 verify=verify,
                                 proxies=proxies,
                                 allow_redirects=allow_redirects)
            r.raise_for_status()
            return r.content
        else:
            r = requests.get(url,
                             headers=OrderedDict(headers),
                             cookies=cookies,
                             timeout=timeout,
                             verify=verify,
                             proxies=proxies,
                             allow_redirects=allow_redirects)
            r.raise_for_status()
            return r.content

    def post(self,
             url,
             headers=None,
             cookies=None,
             timeout=30,
             form_data={},
             verify=False,
             proxies=None,
             allow_redirects=True,
             encoding='utf-8'):
        if self.session:
            r = self.session.post(
                url,
                headers=OrderedDict(headers),
                cookies=cookies,
                timeout=timeout,
                data=form_data,
                verify=verify,
                proxies=proxies,
                allow_redirects=allow_redirects)
            r.raise_for_status()
            r.encoding = encoding
            return r.text, r.headers, dict_from_cookiejar(r.cookies), r.history
        else:
            r = requests.post(
                url,
                headers=OrderedDict(headers),
                cookies=cookies,
                timeout=timeout,
                data=form_data,
                verify=verify,
                proxies=proxies,
                allow_redirects=allow_redirects)
            r.raise_for_status()
            r.encoding = encoding
            return r.text, r.headers, dict_from_cookiejar(r.cookies), r.history