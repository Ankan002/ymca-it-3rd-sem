def getOddMagicSquare(size: int) -> list[list[int]]:
    magic_square = [[0 for x in range(size)] for y in range(size)]
    
    i = size // 2
    j = size - 1
    
    num = 1
    
    while num <= (size * size):
        if i == -1 and j == size:
            j = size - 2
            i = 0
        
        else:
            if j == size:
                j = 0
            
            if i < 0:
                i = size - 1
                
        if magic_square[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
            
        else:
            magic_square[int(i)][int(j)] = num
            num = num + 1
                
        j = j + 1
        i = i - 1
        
    return magic_square 
         
               
            
print(getOddMagicSquare(3))