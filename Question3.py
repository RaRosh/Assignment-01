sample_data = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
count = 0

for eachsample in sample_data:
    if (eachsample < 5):
        print(eachsample)
        count = count + 1

print("The total number of elements is " , count)

