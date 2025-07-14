import time
for i in range(101):
    print(f"\rLoading: [{i * '█'}{(100 - i) * '-'}] {i}%", end="")
    time.sleep(0.05)
print("\nDone!")