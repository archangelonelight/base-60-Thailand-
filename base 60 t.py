

a='กข๑ฃคฅฆ๐งจฉชะ๒เซฌญฎฏฐฑ๓แฒ๔ณด๙ตถทธน๕บปผฝ๘ใพฟภม๖โยรลวศไษสห๗ฬอฮ'

def ac(n):
	p=''
	v=int(n)
	while True:
		p+=a[v%60]
		print(str(v)+'  '+a[v%60])
		v//=60
		if(v<1):
			break
	
	return p[::-1]

def ad(n):
	h=0
	ct=0
	for i in range(len(n)):
		while (a[ct]!=n[i]):
		 	ct+=1
		h+=ct*(60**(len(n)-1-i))
		print(n[i]+' = '+str(ct)+' × '+str(60**(len(n)-1-i)))
		ct=0
		
	return str(h)

dp=input('-----> ')
print('\n'+ac(dp)+'\n')
dp1=input('-----> ')
print('\n'+ad(dp1))