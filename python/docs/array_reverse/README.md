# Array Reverse
A function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available in Python, return an array with elements in reversed order.

## Whiteboard Process
[Whiteboard](reverse-array.png)

## Approach & Efficiency

I tried to work out how it could be done and began writing the white board. The Big O would be linear.

## Solution
I took my idea for how it would work to ChatGPT and it gave me this. I tested it in replit.

def reverse_array(arr, start, end):
  
    if start >= end:
        return
    
    arr[start], arr[end] = arr[end], arr[start]
    
    reverse_array(arr, start + 1, end - 1)

### Example usage:
my_array = [1, 2, 3, 4, 5]
reverse_array(my_array, 0, len(my_array) - 1)
print(my_array)