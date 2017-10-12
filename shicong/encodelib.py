from urllib.parse import unquote, urlencode, quote

decode_unicode_url = unquote
encode_unicode_url = urlencode
encode_uri = quote
"""
这两个函数是这么用的
print(encode_unicode_url({'a':'深圳'}))
上面这个代码就是封装成以 "&"拼接的ur编码字符串.

print(quote("深圳"))
上线这个就是转换成不以"&"拼接的url编码

print(decode_unicode_url('%E6%B7%B1%E5%9C%B3'))
上面这个就是将url编码的字符串转换成编码前的。
"""