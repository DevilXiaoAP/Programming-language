from pythonds.basic.deque import Deque

def palchechker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addFront(ch)

    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


print(palchechker("lsdkjfskf"))
print(palchechker("radar"))