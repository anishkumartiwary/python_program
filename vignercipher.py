def vigner_cipher(filename, keys):
	s=''
	with open(filename, "r+") as fp:
		for line in iter(fp.readline,''): #' ' is called sentinal values
			s += encrypt(line,keys)  # when ' ' is seen stop

		fp.truncate(0)
		fp.writelines(s)

	


def rotate(string,keys):
	'''

	:param string: takes character as input
	:param keys: take key value
	:return: char after rotating it with key value
	'''
	s = ''
	for i in string:
		if 97<=ord(i)<=122:
			if ord(i)+keys > 122:
				s += chr((ord(i)+keys)-25)

			else:
				s += chr(ord(i)+keys)
		else:
			s+= i




	return s


def encrypt(string,keys):
	'''

	:param string: take a string to encrypt
	:param keys: take keys
	:return: encode version of string acoording to vigner cipher
	'''
	list1 = list(string)
	s = ''
	j = 0
	for i in range(len(list1)):
		if j == len(list1):
			break
		for k in range(len(keys)):
			if j+k > len(list1)-1:
				break
			else:
				s += rotate(list1[j+k],ord(keys[k])-96)

		j += len(keys)


	return s






vigner_cipher('anish2.doc','abcd')






