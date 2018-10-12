def get_indices_of_item_weights(weights, limit):
  dict = {}

  for ind, num in enumerate(weights):
    if num in dict:
      return (ind, dict[weights[ind]])
    else:
      dict[limit - weights[ind]] = ind

  return ()

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(get_indices_of_item_weights([4, 6, 10, 15, 16], 21))
 