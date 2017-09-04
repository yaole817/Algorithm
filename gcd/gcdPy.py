
class Algorithms(object):
	def euclidGcd(self,a,b):
		'''
		:type a: int
		:type b: int
		:rtype: int
		'''
		print(a,b)
		if b == 0:
			return a
		else:
			return self.euclidGcd(b, a%b)


if __name__ == '__main__':
	a = Algorithms()
	print(a.euclidGcd(1020,100570))
