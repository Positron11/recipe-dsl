def linear(start:float, end:float, frac:float) -> float:
	"""Linear interpolation from start to end"""
	
	return start + (end - start) * frac


def exp_increase(start:float, end:float, frac:float) -> float:
	"""Exponentially accelerating increase (ease-in)"""
	
	f = 0.0 if frac < 0.0 else 1.0 if frac > 1.0 else frac # clamp to [0, 1]
	k = 3.0 # Steepness parameter; higher => stronger acceleration
	
	# normalize exp so that f=0 -> 0, f=1 -> 1
	num = (pow(2.718281828459045, k * f) - 1.0)
	den = (pow(2.718281828459045, k) - 1.0)
	norm = num / den if den != 0.0 else f
	
	return start + (end - start) * norm
