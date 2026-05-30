numbers = [10,25,8,99,14]
largest = numbers[0]
smallest = numbers[0]
even_count = 0
for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
    if i % 2 == 0:
        even_count = even_count + 1
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Count:", even_count)
        
               
        
