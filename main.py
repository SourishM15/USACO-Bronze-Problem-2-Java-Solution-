def rotate_clockwise(matrix):
  return list(zip(*reversed(matrix)))

def can_create_stamp_painting(N, desired_painting, K, stamp):
  for _ in range(4):
      for i in range(N - K + 1):
          for j in range(N - K + 1):
              match = True
              for x in range(K):
                  for y in range(K):
                      if stamp[x][y] == '*' and desired_painting[i + x][j + y] != '*':
                          match = False
                          break
              if match:
                  return "YES"
      stamp = rotate_clockwise(stamp)
  return "NO"

def main():
  T = int(input())
  for _ in range(T):
      N = int(input())
      desired_painting = [input().strip() for _ in range(N)]
      K = int(input())
      stamp = [input().strip() for _ in range(K)]

      result = can_create_stamp_painting(N, desired_painting, K, stamp)
      print(result)

      # Skip the newline after each test case except the last one
      if _ < T - 1:
          input()

if __name__ == "__main__":
  main()