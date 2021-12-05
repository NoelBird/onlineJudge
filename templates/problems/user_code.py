N = int(input())
for _ in range(N):
  a = input()
  is_pal = True
  for i in range(len(a) // 2):
    if a[i] != a[len(a)-i-1]:
      is_pal = False
      break
  print(is_pal)