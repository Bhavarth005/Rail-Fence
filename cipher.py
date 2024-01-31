from sys import argv


def cipher(str, key):
   matrix = [[] for _ in range(key)] 
   direction = 1
   index = 0
   for i in str:
      matrix[index].append(i)
      if index==0:
         direction = 1
      elif index == key-1: 
        direction = -1
      index += direction
#    print(matrix)
   return "".join(["".join(row_str) for row_str in matrix])

if __name__ == "__main__":
   print(cipher(argv[1], int(argv[2])))