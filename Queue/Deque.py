from collections import deque

deq = deque(maxlen=3)

deq.append(10)
deq.append(20)
deq.append(30)
# After reaching size limit the newer element overrides opposite side's element
deq.appendleft(5)
print(deq)
deq.pop()  # Removes rightmost element
deq.popleft()

print(deq)
deq.clear()
print(deq)
