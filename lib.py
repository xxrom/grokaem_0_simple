def isVecSizeEqual(vec_a, vec_b):
  check = len(vec_a) == len(vec_b)

  if not check:
    print('warn ! sizes are not equal!', vec_a, vec_b)

  return check


def elementwise_multiplication(vec_a, vec_b):
  if not isVecSizeEqual(vec_a, vec_b):
    return None

  sum = 0
  for i in range(0, len(vec_a)):
    sum += vec_a[i] * vec_b[i]

  return sum


def elementwise_addition(vec_a, vec_b):
  if not isVecSizeEqual(vec_a, vec_b):
    return None

  sum = 0
  for i in range(0, len(vec_a)):
    sum += vec_a[i] + vec_b[i]

  return sum


def vector_sum(vec_a):
  sum = 0
  for i in range(0, len(vec_a)):
    sum += vec_a[i]

  return sum


def vector_average(vec_a):
  sum = vector_sum(vec_a)
  return sum / len(vec_a)


a0 = [1, 2, 3, 4]
b0 = [1, 2, 3, 4]
print(elementwise_multiplication(a0, b0) == 30)

a1 = [1, 2, 3, 4]
b1 = [1, 2, 3, 4]
print(elementwise_addition(a1, b1) == 20)

a2 = [1, 2, 3, 4]
print(vector_sum(a2) == 10)

a3 = [1, 2, 3, 4]
print(vector_average(a3) == 2.5)