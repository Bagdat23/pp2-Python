import collections
text = 'lorem ipsuma dolor sit amet amet amet'
words = text.split()
c = collections.Counter(words)
most_common, oc=c.most_common()[0]
l = max(words, key=len)
print(most_common, l)