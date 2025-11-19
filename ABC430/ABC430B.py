N, M = map(int, input().split())
S =[list(map(str, input().strip())) for _ in range(N)]

good_grid =""
final_grid = set()

# 左上を順番にきめていく
for i in range(N-M+1):
  for j in range(N-M+1):
    grid = []
    
    # 決まった左上を基にM×Mの行列を決めていく
    for p in range(M):
      for q in range(M):
        
        # 決まったM×M行列をgridリストに入れていく
        grid.append(S[i+p][j+q])
    good_grid = ''.join(grid)
    final_grid.add(good_grid)
    

print(len(final_grid))