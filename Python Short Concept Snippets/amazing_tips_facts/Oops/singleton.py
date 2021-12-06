class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Lazy singleton
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

x = Singleton()
y = Singleton()

print(f'{x is y=}')