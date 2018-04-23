
def convert_to_bits(n, pad):
  result = []
  while n > 0: 
    if (n % 2) == 0:
      result = [0] + result
    else:
      result = [1] + result
    n = n // 2
  while len(result) < pad:
    result = [0] + result
  return result


def array_to_string(arr):
  return ''.join(str(e) for e in arr)


def string_to_bits(s):
  result = []
  for c in s:
    result = convert_to_bits(ord(c), 7) + result
  return result

def xor(message, key):
  cipher = []
  print(key)
  print(message)
  val = 0
  for m in message:
    if (m == key[val]) == True:
      cipher = [0] + cipher
    else:
      print(str(m) + ' ' + str(key[val]))
      cipher = [m or key[val]] + cipher
    val = val + 1
  return cipher

def main():
  message = string_to_bits('CS')
  key = string_to_bits('KA')
  # Padding important as in one-time-pad the length of key = len of message
  
  cipher = xor(message, key)
  print(cipher) 
if __name__ == "__main__":
  main()
 
