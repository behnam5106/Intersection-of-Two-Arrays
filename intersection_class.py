#Define a class
class Solution:
    #Define a method "intersection" within the "Solution" class
    def intersection(self, num1:list[int], num2:list[int]) ->list[int]:

        #Initialize an empty list "num3"
        num3=[]
        
        # Loop through each element in "num1"
        for i in num1:
            if i in num2 and i not in num3:
                num3.append(i)
        return num3

#main

#Initialize "num1" and "num2" as a sample
num1=[4,9,5]
num2=[9,4,9,8,4]       

# Create an instance of "Solution"
solution=Solution()

# Call intersection method and store the result in "res1"
res1=solution.intersection(num1,num2)
print(res1)
# Result is [4, 9]

