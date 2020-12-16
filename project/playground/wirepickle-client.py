from wirepickle.client import Client

foo = Client('tcp://127.0.0.1:57301')

foo.bar()

print(foo.baz(arg1 = 1, kwarg1='hello from client!'))