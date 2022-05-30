while True:
        i = input('Upiši koju sliku želiš ubacit (samo png, upišeš naziv slike bez extenzije): ')
        try:
                with open(f'{i}.png', 'rb') as f: a=f.read()
        except FileNotFoundError:
                print('Nema tog filea!')
                continue
        i = input('Upiši tajnu poruku: ')
        j = input('Upiši tajni kod: ')
        break
from random import randrange as r, seed as s
a = a+i.encode()
s(j.strip().capitalize())
k = [r(10) for i in range(len(a))]
a = [a[i]-k[i] if a[i]-k[i] >= 0 else 256+a[i]-k[i] for i in range(len(a))]
a = bytes(a)
#print(a[:200])
#with open('hash png.png', 'wb') as f: f.write(a)
z = [f'{hex(i)[2:]}' for i in a]
for i in range(len(z)):
	if len(z[i]) == 1: z[i] = '0'+z[i][-1]
z = ''.join(z)
with open('hex hash upis.txt', 'w') as f: f.write('')
with open('hex hash upis.txt', 'a') as f:
	for i in range(len(z)):
		if i == 0: f.write(z[i])
		elif i % 180 == 0: f.write('\n'+z[i])
		else: f.write(z[i]) 
