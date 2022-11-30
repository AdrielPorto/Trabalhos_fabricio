class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


singleton = SingletonClass()
nova_singleton = SingletonClass()

print(singleton is nova_singleton)

singleton.variavel_singleton = "Hello"
print(nova_singleton.variavel_singleton)
