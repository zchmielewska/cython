from nbody import main
import time

n = 500_000
start = time.time()
main(n)
end = time.time()
print("Elapsed seconds:", end-start)  # 4.2 seconds
