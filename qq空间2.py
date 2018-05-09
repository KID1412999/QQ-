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
header={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
header.update({'cookie':'pgv_pvi=4859450368; pt2gguin=o1608448192; RK=Btbdy5ZFSZ; ptcz=144369a9c075d907a9a24cdae245c886e2f1116bb2d34d0a74ce65881802bdd4; pgv_pvid=1135926938; __Q_w_s_hat_seed=1; __Q_w_s__QZN_TodoMsgCnt=1; _qpsvr_localtk=0.6548637929487284; pgv_si=s278756352; pgv_info=ssid=s43600350; ptisp=cnc; ptui_loginuin=155656464986; uin=o1608448192; skey=@sKqcT0TtH; p_uin=o1608448192; pt4_token=ved4BSG0GOkgRBQy7PB63KIOK01fGgIog7cEkvX3n8Y_; p_skey=iQErIrNLWxNU-qjeiyw4w35wJ3pA4OmDiRm9djzVByI_; fnc=2; Loading=Yes; rv2=80FFD750D88CF4E71621FB1324292F87D401E2C264F0BF15AF; property20=639DB3321ADBF6659994FFD996C493D461237F89E0FCF0FE7D012474EEA47696033F08FDC3FB46B2'})
data={
"uin":"1537772142",
"pos":"20",#移动
"num":"20",#显示的页数
"g_tk":"686307889",
"qzonetoken":"713c866ae963c95792c1adb9ab7ffe9cb74b8f5e23d9fd0b0e48e1a3eba025ac1db6897280cd9be24d"}
data2={
'hostUin': '1537772142',
'start': '0',#移动
's': '0.5485568764022071',
'num': '10',
'g_tk': '686307889',
'qzonetoken': '713c866ae963c95792c1adb9ab7ffe9cb74b8f5e23d9fd0b0e48e1a3eba025ac1db6897280cd9be24d'
}
def deal(html_text):#将数据存入friend列表
	def loads_jsonp(_jsonp):#将jsonp转为python对象
		try:
			return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
		except:
			raise ValueError('Invalid Input')
	t=loads_jsonp(html_text)
	s=re.findall('"con":"(.+?)","type"',html_text)
	l=jsonpath.jsonpath(t,'$..uin')
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
		dict.update({item:friend.count(item)})
	dict1=sorted(dict.items(), key=lambda dict:dict[1],reverse=True)#排序
	for c in dict1 :
		x.append(c[0])
		y.append(c[1])
	print(x)
	print(y)
	plt.barh(range(len(y)),y,color='rgb',tick_label=x)  
	plt.show()  

serch(10,1)

