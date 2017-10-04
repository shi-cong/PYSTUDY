# review
用行动去证明自己的能力

## 前程无忧爬虫
这个虫子，是我从去年，7月开始编写持续维护到今天的虫子。之前的需求很简单，
就是登陆，搜索，分页，投递简历。遇到的技术难点，一开始是登陆那个重定向
http到https，https又到http。之前投递是批量投递，这次是一个一个请求，
但是还是没有加入很多过滤，现在有考虑做职位统计，就是统计你投的这个职位
有多少胜算。

## 世纪佳缘爬虫
这个爬虫主要是我想收集交友网的妹子信息，然后再用程序模拟约会生成约会数据，
然后做k-NN近邻分类算法的测试数据的。不得不说他们后台还是很复杂的，首先，
账户可能有安全级别，解封条件大概是2天左右，验证码也防IP，解封条件1天左右。
目前我要的数据都已经拿到了，他们平台的验证码，还是比较容易破解的。

## 数据分析 
*统计爬虫并且工资在1万左右的人数最多的前100个*
```sql
SELECT * FROM job51.my_apply where  job_name like '%爬虫%'  and pay like '%1.%' order by submit_nums desc limit 100;
```
![](https://github.com/shi-cong/review/blob/master/data/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-10-05%20%E4%B8%8A%E5%8D%886.15.58.png)
从图中可以看出的是，爬虫在深圳招聘的并不多，由此可以认为，我上次辞职是一次非常大的失误。
这里就只有一家深圳你我金融看起来还不错的公司，其它都不符合。

*统计爬虫并且在深圳的公司
```sql
SELECT * FROM job51.my_apply where  job_name like '%爬虫%'  and company_name like '%深圳%'  order by submit_nums desc limit 100;
```
˙˙
## k-NN近邻分类算法
