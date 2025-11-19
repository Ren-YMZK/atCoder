S, A, B, X = map(int, input().split())

# 1周期の長さ
one_cycle_time = A + B

# 1周期の回数
how_many_cycle = X // one_cycle_time

# 余った時間
amari_time = X % one_cycle_time

# 1周期で走った時間
cycle_run_time = how_many_cycle * A

#あまり時間で走った時間
if amari_time < A:
  amari_run_time = amari_time
else:
  amari_run_time = A

run_time_sum = how_many_cycle * A + amari_run_time

run_meters = run_time_sum * S

print(run_meters)
