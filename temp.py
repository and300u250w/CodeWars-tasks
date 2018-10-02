def censor(text, word):
    stars = len(word) * "*"
    x = text.split(" ")
    x = [n.replace(word, stars) for n in x]
    print(x)





def censor(text, word):
    stars = len(word) * "*"
    x = text.split(" ")
    x = [n.replace(word, stars) for n in x]
  return x

censor("this hack is wack hack", "hack")
