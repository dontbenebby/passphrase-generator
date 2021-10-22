import random
#NOTE: we *must* use SystemRandom to ensure reasonably cryptographically secure.
#NOTE Future version should probably generate a random seed then use that.

#empty list for PW
pw = []

#simulate dice rolls
for n in range(0,5):
	pw.append(random.SystemRandom().randint(1,6))
	 
#squishes together
passwordKey = ''.join(str(i) for i in pw)

print(passwordKey)
