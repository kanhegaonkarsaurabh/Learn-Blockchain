""" This small piece of code is meant to clarify how the PoW algorithm works 
"""

from hashlib import sha256

x = 5
y = 0 

# Determine such a sha256 hash which ends in zero
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0": 
  y += 1

"""
  If you look at the solution, its evident that y = 21 took 
  time to solve. Hence, here the solution was difficult to 
  find. 
"""

print(f'The solution to it is y = {y}')

""" 
  But the value can easily be verified by printing the hash 
  onto the screen and checking the last digit
"""

