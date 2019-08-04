products = []
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break #跳出程序
	price = input('请输入商品价格：')
	price = int(price)#把字符型元素转换成整数型
	products.append([name,price])#把商品名称和价格装入products清单
print(products)

for p in products:   #利用for loop 把清单products中的元素读出来
	print(p[0],'的价格是',p[1])

with open('products.csv','w') as f:# 把清单products中的元素写到products.csv文件中
	f.write('商品' + ',' + '价格' + '\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		
