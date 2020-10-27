import time


def js_time(func):
    def time1(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f'时间差是{end_time}')
        return f

    return time1

@js_time
def add(a, b, c):
    return a + b + c


if __name__ == "__main__":
    add(4, 5, 6)

