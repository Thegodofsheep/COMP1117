import sys
def run_one_step(step, cur, stop):
 # step: current step number
 # cur: the position of current point
# stop: the position of stop point
 # Begin of your implementation ------             
    if (cur == stop):
        return step
    
    pos = run_one_step(step + 1, cur + step + 1,stop)
 
    neg = run_one_step(step + 1, cur - step - 1,stop)
 
    return min(pos, neg)

 # End of your implementation ------

stop = int(input())
step = run_one_step(0, 0, stop)
print(step)
