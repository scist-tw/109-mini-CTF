from Crypto.Util.number import *
from gmpy2 import is_prime, next_prime
from secret import flag

def get_triple_prime():
	p, q, r = getPrime(512), 0, 0
	while(True):
		if(is_prime(p+2) and is_prime(p+6)):
			q = p+2
			r = p+6
			break
		else:
			p = next_prime(p)
	return (p,q,r)

p1, p2, p3 = get_triple_prime()
q1, q2, q3 = get_triple_prime()

n1 = p1*q1
n2 = p2*q2
n3 = p3*q3
e = 65537

C = pow(pow(pow( bytes_to_long(flag), e, n1), e, n2), e, n3)

with open('output', 'w') as f:
	f.write('C= {}\n\ne= {}\n\nn1= {}\n\nn2= {}\n\nn3= {}'.format(C, e, n1, n2, n3))
