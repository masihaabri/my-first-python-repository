def get():  # this function getting the scores
    x = ""
    for i in range(20):
        x += input("Enter score:")
        x += ","

    return x


y = get()
z = y.split(',')
a = [None] * 20  # Specify the length of the array
for j in range(20):
    r = z[j]
    a[j] = int(r)
a.sort()
print("All of the scores small to large:")
print(a)
print("biggest score:")
print(a[19])
print("second score:")
print(a[18])
