
def single(func):
    """
    单例模式（暂时不用）
    :param func: basepage 的__init__ 构造函数，只初始化一次
    :return:
    """
    _instance = {}
    def wrapper(*args, **kwargs):
        if func in _instance:
            return func(*args, **kwargs)
        else:
            _instance[func] = func(*args, **kwargs)
            return _instance[func]
    return wrapper

def find_mainblack(func):
    """"
    查找黑名单装饰器
    """
    def wrapper(*args, **kwargs):
        # instance是basefuc的实例，args[0]获取self
        # 局部调用
        from App.page.basepage import basefuc
        instance: basefuc = args[0]
        try:
            result = func(*args, **kwargs)
            return result
            instance.error_num = 0
        except Exception as e:
            # 如果查询黑名单次数大于最大查询次数，抛出异常
            if instance.error_num > instance.max_num
                raise e
            # 查找黑名单 +1
            instance.error_num += 1
            # 正常用例查找元素没有找到，则查找黑名单
            for black_ele in instance.main_black:
                # 这里用find_elements
                ele = instance.driver.find_elements(*black_ele)
                # 如果找到黑名单元素，则点击
                if len(ele) > 0:
                    ele[0].click()
                    # 点击关闭以后，继续查找用例元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
