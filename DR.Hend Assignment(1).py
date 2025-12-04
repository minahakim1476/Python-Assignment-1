#Problem 1
products = ["  LAPTOP ", "phone  ", "  Tablet", "CAMERA  "] 
fixedProducts = list(map(lambda x : x.strip().title() , products))
print(fixedProducts)

#Problem 2
celsius = [0, 10, 20, 30, 40] 
Fahrenheit = list(map(lambda x : x * (9/5) + 32.0 , celsius))
print(Fahrenheit)

#Problem 3
nums = [1, 2, 3, 4, 5]
resultNums = list(map(lambda x : (x ** 2) + 10 , nums))
print(resultNums)


#Problem 4
words = ["python", "lambda", "programming", "map", "function"]
charsList = list(map(lambda word : (word[0] , word[-1]) , words))
print(charsList)

#Problem 5
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
resultList = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))
print(resultList)

#Problem 6
nums = [10, 20, 30, 40, 50]
minValue = min(nums)
maxValue = max(nums)
normalized = list(map(lambda num : (num - minValue) / (maxValue - minValue) , nums))
print(normalized)

#Problem 7
sentences = ["The quick brown fox" , "Jumps over the lazy dog" , "Python is fun"]
wordsLength = list(map(lambda sentence : list(map(lambda word : len(word) , sentence.split())), sentences))
print(wordsLength)