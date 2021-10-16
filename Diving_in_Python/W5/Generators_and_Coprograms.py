
# Co-program (корутин)
#
# def grep(pattern):
#     print('start grep')
#     while True:
#         line = yield
#         if pattern in line:
#             print(line)
#
#
# g = grep('python')
# next(g)  # g.send(None)
# g.send("golang is better?")
# g.send('python is simple!')

# Stopping Co-program with .close()
#
# def grep(pattern):
#     print('start grep')
#     try:
#         while True:
#             line = yield
#             if pattern in line:
#                 print(line)
#
#     except GeneratorExit:
#         print('stop generation')
#
#
# g = grep('python')
# next(g)
# g.send('python is the best!')
# g.throw(RuntimeError, 'something wrong!')   # Throw exception into the co-program
# g.close()


# Calling co-programs PEP 380\
#
# def grep(pattern):
#     print('start grep')
#     while True:
#         line = yield
#         if pattern in line:
#             print(line)
#
#
# def grep_python_coroutine():
#     g = grep('python')
#     yield from g
#
#
# g = grep_python_coroutine()
# print(g)
# g.send(None)
# g.send('python!')
# g.close()

# PEP 380 Generators
#
def chain(x_iter, y_iter):
    yield from x_iter
    yield from y_iter


def same_chain(x_iter, y_iter):
    for x in x_iter:
        yield x
    for y in y_iter:
        yield y


a = [1, 2, 3]
b = (4, 5)
for x in chain(a, b):
    print(x)

