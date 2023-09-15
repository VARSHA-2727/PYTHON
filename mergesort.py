#merge sort
def mergesort(list1,i=None,j=None,k=None):
  if len(list1)>1:
      mid=len(list1)//2
      left_list=list1[ :mid]
      right_list=list1[mid: ]
      mergesort(left_list)
      mergesort(right_list)
      i==0,j==0,k==0
      while i<len(left_list) and j<len (right_list):
              if left_list[i]<right_list[j]:
                 list1[k]=left_list[i]
                 k=k+1
                 i=i+1
      else:
                 list1[k]=right_list[j]
                 k=k+1
                 j=j+1
      while i<left_list:
             list1[k]=left_list[i]
             k=k+1
             i=i+1
      while j < right_list:
            list1[k] = right_list[j]
            k=k+1
            j=j+1
num=int(input("enter the number of elements in list"))
list1=(int(input())for x in range(num))
mergesort(list1)
print("sorted list",list1)






