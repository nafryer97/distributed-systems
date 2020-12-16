from wirepickle.server import expose, Server

class Foo:
    @expose('bar')
    def bar(self):
        print('bar')
        return 0

    @expose('baz')
    def baz(self, arg1, kwarg1='baz'):
        print(kwarg1)
        return self.bar() + arg1

if __name__ == '__main__':
    instance = Foo()
    Server(instance).listen('tcp://*:57301')