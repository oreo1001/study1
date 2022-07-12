croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
count = len(word)
for i in range(0, len(word)-1):
	for j in croa:
		if i > 0:
			if word[i-1] + word[i] + word[i+1] == "dz=":
				count -= 2
				i += 1
				if i >= len(word)-1:
					break
				pass
			if word[i] + word[i+1] == j:
				count -= 1
		else:
			if word[i] + word[i+1] == j:
				count -= 1
print(count)	