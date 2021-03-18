from threading import Lock

def synchronized(func):
    """
    线程安全的单例模式，线程访问创建类的实例时会拿到锁，就相当于独占该单例类
    其他线程无法创建该单例类的实例，使用完释放锁，其他线程才可以创建单例类的实例
    :param func:
    :return:
    """
    func.__lock__ = Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func

def singleton(func):
    instance = {}
    @synchronized
    def warpper(*arge, **kwargs):
        if func not in instance:
            instance[func] = func(*arge, **kwargs)
        return instance[func]
    return warpper

