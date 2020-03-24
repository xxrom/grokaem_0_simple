# Calc prediction output from input and weights
def w_sum(input, weights):
  if len(input) != len(weights):
    assert (len(input) == len(weights))
    return None

  sum = 0
  for i in range(0, len(input)):
    sum += input[i] * weights[i]

  return sum


# Neurons
def neural_network(input, weights):
  pred = w_sum(input, weights)
  return pred


# Team info data
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

input = [toes[0], wlrec[0], nfans[0]]
weights = [0.1, 0.2, 0]

# Get predictions
pred = neural_network(input, weights)
print('chance to win ~'t, pred)
