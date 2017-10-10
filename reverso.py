def reverso(n):
   s = str(n)
   l = 0
   for x in range(len(s)):
       l += int(s[x]) * (10**x)
   return l

n = int(raw_input('N: '))
print reverso(n)