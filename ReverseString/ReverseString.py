def reverseString(s, _from, _to):
	s = s.split()
	while _from < _to:
		t = s[_from]
		s[_from] = s[_to]
		_from += 1
		s[_to] = t
		_to -= 1
	return ''.join(s)

def leftRotateString(s, n, m):
	m %= n
	s = reverseString(s, 0, m - 1)
	s = reverseString(s, m, n - 1)
	s = reverseString(s, 0, n - 1)
	return s

if __name__ == '__main__':
	a = '123456789'
	a = leftRotateString(a, len(a), len(a))
	print(a)
