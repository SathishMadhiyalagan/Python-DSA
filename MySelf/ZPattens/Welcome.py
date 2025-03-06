# Enter your code here. Read input from STDIN. Print output to STDOUT
# r,c = 11,33
r,c = 7,21
print(r,c)
def dot(num):
    return "".join("-" for i in range(num))
# print(dot(3))
def pipe(num):
    return "".join(".|." for i in range(num))
# print(pipe(3))
dotCount = r//2 *3
pipeCount = 1

for i in range(r):
    if r//2 !=i:
        if r//2 >=i:
            print(dot(dotCount)+pipe(pipeCount)+dot(dotCount))
            dotCount-=3
            pipeCount+=2
        else:
            dotCount+=3
            pipeCount-=2
            print(dot(dotCount)+pipe(pipeCount)+dot(dotCount))
            
    else:
        print(dot((c-7)//2)+"WELCOME"+dot((c-7)//2))
    
    
    
    