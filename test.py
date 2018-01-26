import math 
import random

def normal_approximation_to_binomial(n, p):
	"""Find mu and sigma corresponding to a Binomial(n, p)"""
	mu = p * n 
	sigma = math.sqrt(p * (1-p) *  n)
	return mu, sigma

def normal_upper_bound(probability, mu=0, sigma=1):

	pass

def two_sided_p_value(x, mu=0, sigma=1):
	if x >= mu:
		return 2 * normal_approximation_to_binomial
	pass


def run_experimnet():
	"""Filp a fair coin 1000 times, True=heads, False=Tails"""
	return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(exper):
	"""Using 5% signafice levels"""
	num_heads = len([flip for flip in exper if flip])
	return num_heads < 469 or num_heads > 531







def main():
	# normal_approximation_to_binomial(10, 2)

	random.seed(0)
	expers = [run_experimnet() for _ in range(1000)] 
	num_rejects = len([exper for exper in expers if reject_fairness(exper)])
	print(num_rejects)
if __name__ == '__main__':
	main()