s = "abcabcabcabc"
max = 0
for i in range(1, len(s)//2 + 1):
    a = s[0:i]
    k = 1
    while a == s[k*i:(k+1)*i]:
        k += 1
    else:
        if k*i == len(s) and max < k:
            max = k
print(max)
