#讀取檔案
product=[]
with open('product.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #跳到下一回
		name, price = line.strip().split(',') #先去空白與換行再切割
		product.append([name, price])
print(product)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name =='q':
		break
	price = int(input('請輸入商品價格:'))
	product.append([name, price])
print(product) 

# 印出所有購買記錄
for p in product:
	print(p[0] , '的價格', p[1])

#寫入檔案
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n') #加入表頭
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')
