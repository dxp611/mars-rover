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

def initialise_robot(matrix, robot):
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
    elif command == 'L':
      robot.rotate_left()
      initialise_robot(matrix, robot)
    elif command == 'R':
      robot.rotate_right()
      initialise_robot(matrix, robot)

    print("Robot performed: {}".format(command))
    print_matrix(matrix, m, n)

def process_input(inputs):
  m, n = inputs[0], inputs[1]
  robots = inputs[2:]
  return m, n, robots

def main(m, n, robots):
  # +1 matrix size to allow the robots to reach the top of the matrix
  m +=1
  n +=1 

  mars = build_matrix(m, n)
  deployed_robots =[]
  for initial_state, commands in robots:
    robot = Robot(*initial_state)
    initialise_robot(mars, robot)

    print("Initial matrix:")
    print_matrix(mars, m, n)
    move_robot(robot, mars, m, n, commands)

    deployed_robots.append(robot)

  print("Final matrix:")
  print_matrix(mars, m, n)
  
  result = []
  for i, robot in enumerate(deployed_robots):
    print("Robot {} final state:".format(i+1), robot.get_state())
    result.append(robot.get_state())
  return result

def run(inputs):
  # inputs=[4, 8, ((2, 3, 'E'), 'LFRFF'), ((0, 2, 'N'), 'FFLFRFF'), ((2, 3, 'N'), 'FLLFR'), ((1, 0, 'S'), 'FFRLF')]
  m, n, robots = process_input(inputs)
  return main(m, n, robots)
