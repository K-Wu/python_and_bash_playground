count = 0


def increment_count():
    global count
    count += 1
    return count


def foo(a=increment_count()):
    print(a)


print(increment_count())  # 2
print(increment_count())  # 3
foo()  # 1
foo()  # 1
foo()  # 1
