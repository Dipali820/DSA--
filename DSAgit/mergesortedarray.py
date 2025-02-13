
def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
     
      i=0
      j=0
      while i<len(nums1) and  nums2[j]>=nums1[i]:
            if nums1[i]==nums2[j]:
                nums1[i+1]=nums2[j]
            else:
                i+=1
      return nums1
nums1=list(input("enter the number:"))
nums2=list(input("enter the number:"))  
print(merge())
