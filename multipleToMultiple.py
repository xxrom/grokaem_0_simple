# Weights to outputs = 0 строка - injuries(травмы), 1- win, 2 - sadness
weights = [[0.1, 0.1, -0.3], [0.1, 0.2, 0.0], [0.0, 1.3, 0.1]]


def w_sum(vec_a, vec_b):
  assert (len(vec_a) == len(vec_b))
  sum = 0
  for i in range(len(vec_a)):
    sum += vec_a[i] * vec_b[i]
  return sum


def vect_mat_mul(vect, matrix):
  assert (len(vect) == len(matrix))
  output = [0, 0, 0]

  for i in range(len(vect)):
    output[i] = w_sum(vect, matrix[i])

  return output


def neural_network(input, weights):
  pred = vect_mat_mul(input, weights)
  return pred


toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]

pred = neural_network(input, weights)
print(pred)