def front_back(word):

  if len(word) <= 1:
    return word
 
  return word[-1] + word[1:-1] + word[0]
