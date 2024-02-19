from robot import Robot

def build_matrix(m, n):
  matrix = []
  for row in range(m):
    x = []
    for column in range(n):
      x.append(0)
    matrix.append(x)
    
  return matrix

def print_matrix(matrix, m, n):
  for row in range(m - 1, -1, -1):
    for column in range(n):
      print(matrix[row][column], end=" ")
    print()

def deploy_robot(matrix, robot):
  matrix[robot.y][robot.x] = robot.orientation

def main():
  m = 4
  n = 8
  
  # +1 matrix size to allow the robots to reach the top of the matrix
  m +=1
  n +=1 
  
  robot1_initial_state = (0, 2, 'E')
  robot_moves = 'FLFRFF'

  mars = build_matrix(m, n)
  
  print("Initial matrix:")
  print_matrix(mars, m, n)

  robot1 = Robot(*robot1_initial_state)
  matrix = deploy_robot(mars, robot1)
  print("Final matrix:")
  print_matrix(mars, m, n)

if __name__ == "__main__":
  main()