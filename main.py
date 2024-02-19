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

def update_robot_position(matrix, old_x, old_y, robot=None):
  if robot:
    matrix[old_y][old_x] = 0
    matrix[robot.y][robot.x] = robot.orientation
  else:
    matrix[old_y][old_x] = "L"

def move_robot(robot, matrix, m, n, commands):
  
  def lost_robot(robot, matrix, old_x, old_y):
    print('Robot is lost!')
    robot.set_lost()
    update_robot_position(matrix, old_x, old_y)
    
  for command in commands:
    if command == 'F':
      old_x = robot.x
      old_y = robot.y
      if robot.orientation == 'N':
        new_y = robot.y + 1
        if 0 <= new_y < m:
          robot.move_forward()
          update_robot_position(matrix, old_x, old_y, robot)
          
        else:
          lost_robot(robot, matrix, old_x, old_y)
          break
      elif robot.orientation == 'E':
        new_x = robot.x + 1
        if 0 <= new_x < n:
          robot.move_forward()
          update_robot_position(matrix, old_x, old_y, robot)
        else:
          lost_robot(robot, matrix, old_x, old_y)
          break
      elif robot.orientation == 'S':
        new_y = robot.y - 1
        if 0 <= new_y < n:
          robot.move_forward()
          update_robot_position(matrix, old_x, old_y, robot)
        else:
          lost_robot(robot, matrix, old_x, old_y)
          break
      elif robot.orientation == 'W':
        new_x = robot.x - 1
        if 0 <= new_x < n:
          robot.move_forward()
          update_robot_position(matrix, old_x, old_y, robot)
        else:
          lost_robot(robot, matrix, old_x, old_y)
          break
    print("Robot performed: {}".format(command))
    print_matrix(matrix, m, n)


def main():
  # m = int(input("Rows:"))
  # n = int(input("Columns:"))

  m = 4
  n = 8
  
  # +1 matrix size to allow the robots to reach the top of the matrix
  m +=1
  n +=1 
  
  robot1_initial_state = (2, 2, 'W')
  robot_moves = 'FF'

  mars = build_matrix(m, n)
  
  print("Initial matrix:")

  robot1 = Robot(*robot1_initial_state)
  deploy_robot(mars, robot1)

  print_matrix(mars, m, n)
  move_robot(robot1, mars, m, n, robot_moves)
  
  print("Final matrix:")
  print_matrix(mars, m, n)

if __name__ == "__main__":
  main()