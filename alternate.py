name='jismy'
letters=0
alt=''
for letters in range(len(name)):
	if(letters%2==0):
		alt+=name[letters]
print alt