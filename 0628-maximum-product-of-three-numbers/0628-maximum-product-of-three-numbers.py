class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        temp=nums
        temp.sort()

        n1=temp[-1]
        n2=temp[-2]
        n3=temp[-3]
        product1=n1*n2*n3
        
        n1=temp[0]
        n2=temp[1]
        n3=temp[-1]
        product2=n1*n2*n3

        return max(product1,product2)
        