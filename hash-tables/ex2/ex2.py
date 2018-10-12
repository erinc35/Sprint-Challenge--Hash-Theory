def reconstruct_trip(tickets):
  dict = {}
  length = len(tickets)
  route = [None] * (length-1)
  ends = []

  for ticket in tickets:
    ends.append(ticket[1])
    if ticket[0] == None:
      route[0] = ticket[1]
    dict[ticket[0]] = ticket[1]

  i = 1

  for start in dict:
    if start not in ends:
      return []

  while i < length-1:
    route[i] = dict[route[i-1]]
    i += 1
  

  return route  

if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  print(reconstructTrip([
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [None, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', None],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
]))
