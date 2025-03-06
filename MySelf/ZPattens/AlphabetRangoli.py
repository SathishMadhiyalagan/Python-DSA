def print_center_elements(position,listE):
    center_index = len(listE) // 2  # Find the center index of the list
    half_range = position // 2      # Half range to get elements around the center
    start = max(center_index - half_range, 0)
    end = min(center_index + half_range + 1, len(listE))
    return(listE[start:end])

# def dictC(mid,colRange):
#     return {i: (i+1 if  else i - 1) for i in range(colRange)}

# print(dictC(4,9))
def pr(size):
    row = size+(size-1)
    col = row + (row-1)
    # print(row,col)
    
    position = 1
    
    for i in range(row):
        # print(position)
        listE =[i for i in range(col) if i%2==0]
        elementList = print_center_elements(position,listE)
        inc = size
        for j in range(col):
            if j%2==0 and (j in elementList):
                if col//2 >j:
                    print(chr(inc+96),end="")
                    inc-=1
                else:
                    print(chr(inc+96),end="")
                    inc+=1
            else:
                print("-",end="")
        
        position += 2 if i < row // 2 else -2
          
        print()
  
pr(3)