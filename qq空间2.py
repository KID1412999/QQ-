#留言和说说QQ号必须一致#
import requests
import re
import json
import time
import jsonpath
import matplotlib.pyplot as plt  
friend=[]
dict={}
x=[]
y=[]
url='https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6'
url2='https://user.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/get_msgb'
header={'user-agent':''}#构造请求头
header.update({'cookie':''})#cookie设置
data={
"uin":"",#目标qq
"pos":"20",#移动
"num":"20",#显示的页数
"g_tk":"686307889",
"qzonetoken":" "}
data2={
'hostUin': '',目标qq
'start': '0',#移动
's': '0.5485568764022071',
'num': '10',
'g_tk': '686307889',
'qzonetoken': ' '
}
def deal(html_text):#将数据存入friend列表
	def loads_jsonp(_jsonp):#将jsonp转为python对象
		try:
			return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
		except:
			raise ValueError('Invalid Input')
	t=loads_jsonp(html_text)
	l=jsonpath.jsonpath(t,'$..uin')#使用jsonpath方法匹配qq账号
	for i in l:
		friend.append(i)
	print(friend,len(friend))
def serch(k_,k):
	
	#说说#
	for m in range(0,k_*20,20):
		time.sleep(2)
		data.update(pos=m)
		html=requests.get(url,headers=header,params=data)
		deal(html.text)
	#留言#
	for n in range(0,k*10,10):
		data.update(start=n)
		html=requests.get(url2,headers=header,params=data2)
		deal(html.text)
	myset= set(friend) #删除列表中的重复元素 
	for item in myset: 
		# print(friend.count(item), " of ", item, "friend")
		dict.update({item:friend.count(item)})#将字典转为列表
	dict1=sorted(dict.items(), key=lambda dict:dict[1],reverse=True)#排序
	for c in dict1 :
		x.append(c[0])
		y.append(c[1])
	print(x)
	print(y)
	plt.barh(range(len(y)),y,color='rgb',tick_label=x) #绘图 
	plt.show()  
  
serch(10,1)
