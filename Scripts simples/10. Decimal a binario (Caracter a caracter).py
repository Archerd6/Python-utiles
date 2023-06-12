# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
     
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
     
    print("---------------TEST---------------")
    s = "444544507000701223"
    s = s.replace("", " ")[1: -1]
    print(s)
    
    arr = s.split()
    print(arr)
    
    # decimal value
    dec_val = 7
    # Calling function
    DecimalToBinary(dec_val)
    print()
    
    print("----------------------------------")
    
    print()
    
    for i in range(len(arr)):
        DecimalToBinary(int(arr[i]))
        print()