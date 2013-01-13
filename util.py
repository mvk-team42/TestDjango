def isPrime(n):
	if n == 1:
		return False
	elif n > 1:
		return isFactorOfSomeElement(n, range(2,n))
	else:
		return False

def isFactorOfSomeElement(n, array):
	for element in array:
		if n % element == 0:
			return False
	return True

def getPrimesInRange(first, last):
	primesInRange = []
	for n in range(first, last+1):
		if isPrime(n):
			primesInRange.append(n)
	return primesInRange
