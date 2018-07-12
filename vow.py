vowels=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
alpha=input()
if(alpha in vowels):
	print("Vowel")
elif(alpha in consonants):
	print("Consonant")
else:
	print("invalid")
