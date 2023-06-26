class Solution:

   def searchInsert(self, A, B):
       start = 0
       end = len(A) - 1
       low = end + 1
       while start <= end:
           mid = (end + start) // 2
           if A[mid] == B:
               return mid
           else:
               if A[mid] > B:
                   end = mid - 1
               else:
                   start = mid + 1
       return start

x = Solution()
x.A = [11, 13, 15, 16]
x.B = 12
print(x.searchInsert(x.A,x.B))
