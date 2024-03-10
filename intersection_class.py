class Solution:
    def intersection(self, num1:list[int], num2:list[int]) ->list[int]:
        num3=[]
        for i in num1:
            if i in num2 and i not in num3:
                num3.append(i)
        return num3

#main
    
num1=[4,9,5]
num2=[9,4,9,8,4]       
        
solution=Solution()
result=solution.intersection(num1,num2)
print(result)

