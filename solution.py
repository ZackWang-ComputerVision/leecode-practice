"""
This file is my solutions in Python to some of the Medium and Hard level questions from LEECODE

"""

import my_data_structure as ds
import my_algorithm as al

# for type declaration practice
from typing import TypeVar, Generic, Callable, NewType, List, Dict
T = TypeVar('T')
U = TypeVar('U')
V = TypeVar('V')

"""
Although Python is a dynamic typing language, the type declaration is an important feature
when developing a large Python project, because errors will be caught in compile time.
Next four functions are for practicing Python in a functional programming style with static typing.
"""

def f1():
  func: Callable[[T, T], T] = lambda x, y: x + y
  return func

def f2(x: T, y: Callable[[T], U] = lambda f: f(x)):
  return y(x)

#a = f2(5, lambda y: y + 1)
#print(a)

def f3(x: T):
  func: Callable[[T], U] = lambda y: y(x)
  return func

#a = f3(10)
#b = a(lambda z: z + 1)
#print(b)

def f4(arg1: T, arg2: U, arg3: Callable[[T, U], V] = lambda z: z(x, y)):
  return arg3(arg1, arg2)


""" ---------------------------------------------------------
LEECODE Practice Start
--------------------------------------------------------- """


""" 
#2 -- Add Two Numbers


"""
link1 = ds.LinkedList(2)
link1.add(3)
link1.add(4)

link2 = ds.LinkedList(5)
link2.add(6)
link2.add(7)

def q2(link_a, link_b):
  a = 0
  b = 0
  curr1 = link_a.head
  curr2 = link_b.head

  multi1 = 1
  while curr1 != None:
    a += curr1.value * multi1
    curr1 = curr1.next
    multi1 = multi1 * 10

  multi2 = 1
  while curr2 != None:
    a += curr2.value * multi2
    curr2 = curr2.next
    multi2 = multi2 * 10

  return a + b

#print(q2(link1, link2))


""" 
#3 -- Longest Substring Without Repeating Characters


"""
def q3(string: str) -> int:
  dic = {}
  dic_len = 0
  count = 0
  for i in range(len(string)):
    dic_len += 1
    if s in arr:
      count = max(count, len(arr))
      if pre_index == len(arr): arr = []
      else: arr = arr[index + 1 : -1]
    arr.append(s)
  return max(count, len(arr))
    
#print(q3("wfgtrthd"))


""" 
#5 -- Longest Substring Without Repeating Characters


"""
def q5(string: str) -> str:
  return



""" 
#6 -- ZigZag Conversion


"""
def q6(string: str, n_row: int) -> str:
  arr = ["" for n in range(n_row)]
  order = True
  index = 0
  for i in string:
    arr[index] = arr[index] + i
    if order:
      index += 1
    else:
      index -= 1    
    if index > n_row - 1:
      order = False
      index -= 2
    elif index < 0: 
      order = True
      index += 2
  new_str = ""
  for word in arr:
    new_str = new_str + word
  return new_str

#print(q6("PAYPALISHIRING", 3))


""" #11 -- Container With Most Water """
def q11 (arr: List[int]) -> int:
  if len(arr) < 2: return 0
  s = 0
  e = len(arr) - 1
  area = 0
  while s < e:
    area = max(area, (e - s) * min(arr[s], arr[e]))
    if arr[s] <= arr[e]: s += 1
    else: e -= 1
  return area

#print(q11([5,3,7,2]))


""" #13 -- 3Sum """
def q13 (nums: List[int]) -> List[List[int]]:
  if len(arr) < 3: return None
  arr = set()
  length = len(arr)
  #result = []
  for i in arr[0 : length - 2]:
    for j in arr[i + 1 : length - 1]:
      if j != i:
        target = 0 - (i + j)
        for k in arr[j + 1 : length]:
          if k != j and target == k:
            unique.add(output)
  return unique
# not unique
#print(q13([-1,0,1,2,-1,-4]))


""" 
#22 -- Generate Parentheses

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
def q22 (n: int) -> List[str]:
  stack = []

  def recursion (left=0, right=0, buff=[]):
    if len(buff) == 2 * n:
      stack.append("".join(buff))
      return
    if left < n:
      buff.append("(")
      recursion (left + 1, right, buff)
      buff.pop()
    if right < left:
      buff.append(")")
      recursion(left, right + 1, buff)
      buff.pop()
  
  recursion()
  return stack

#print(q22(3))


""" 
#39 -- Combination Sum

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
"""
def q39(nums: List[int], target: int) -> List[List[int]]:
  arr = []
  if target < 0 or len(nums) == 0: return arr
  sort_nums = sorted(nums)

  def recursion(summ, path, list_nums):
    for i in range(len(list_nums)):
      new_sum = list_nums[i] + summ
      new_path = path + [list_nums[i]]
      if new_sum == target:
        arr.append(new_path)
        return
      if new_sum > target:
        return
      recursion(new_sum, new_path, list_nums[i:])
  
  recursion(0, [], sort_nums)
  return arr

#print(q39([2,3,5], 8))


""" 
#46 -- Permutation

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
def q46 (nums: List[int]) -> List[List[int]]:
  arr = []

  def recursion (collection, new_nums):
    inner_arr = []

    for i in range(len(new_nums)):
      inner_arr.append([nums[i]])

    for j in inner_arr:
      pass


  return arr


""" 
#54 -- Spiral Matrix

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""
def q54 (nums: List[List[int]]) -> List[int] :
  arr = []

  def recursion (new_nums, left_to_right):
    if left_to_right:
      arr + new_nums[0]
      for i in range(1, len(new_nums)):
        arr.append(new_nums[i][-1])
      matrix = new_nums[1 : ][ : -1]
      return matrix
    else:
      arr + list(reversed(new_nums[-1]))
      for i in range(len(new_nums) - 2, -1):
        arr.append(new_nums[i][0])
      matrix = new_nums[ : -1][ 1 : ]
      return matrix

  new_matrix = nums
  left_to_right = True
  for i in range(len(nums)):
    print(new_matrix)
    new_matrix = recursion(new_matrix, left_to_right)
    print(left_to_right)
    left_to_right = not left_to_right

  return arr

print(q54([[1,2,3],[4,5,6],[7,8,9]]))

""" 
#56 -- Merge Intervals

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""
def q56 (intervals: List[List[int]]) -> List[List[int]]:
  arr = []
  index = 0
  for interval in intervals:
    if len(arr) == 0:
      arr.append(interval[0])
      arr.append(interval[1])
    else:
      start = interval[0]
      while start <= arr[index]:
        if index > 0:
          index -= 1
        else:
          break
      arr = arr[ : index + 1]

      end = interval[1]
      if (index + 1) % 2 != 0:
        arr.append(end)
        index += 1
      else:
        arr.append(start)
        arr.append(end)
        index += 2
  result = []
  for i in range(0, len(arr), 2):
    result.append([arr[i], arr[i + 1]])
  return result

#print(q56([[1,3],[2,6],[8,10],[15,18]]))