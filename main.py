
def build_matrix(m, n):
  matrix = []
  for row in range(m):
    x = []
    for column in range(n):
      x.append(0)
    matrix.append(x)
    
  return matrix

def print_matrix(matrix, m, n):
  for row in range(m):
    for column in range(n):
      print(matrix[row][column], end=" ")
    print()

def main():
  m = 4
  n = 8
  
  mars = build_matrix(m, n) 
  print_matrix(mars, m, n)

if __name__ == "__main__":
  main()