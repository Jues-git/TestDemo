import allure

def single(func):
    """
    单例模式（暂时不用）
    :param func: base_fuc 的__init__ 构造函数，只初始化一次
    :return:
    """
    _instance = {}
    def wrapper(*args, **kwargs):
        if func in _instance:
            return _instance[func]
        else:
            _instance[func] = func(*args, **kwargs)
            return _instance[func]
    return wrapper

def find_main_black(func):
    """"
    查找黑名单装饰器
    """
    def wrapper(*args, **kwargs):
        from App.page.basepage import Base_func
        # instance是 base_fuc的实例，args[0]获取self
        # 局部调用
        instance: Base_func = args[0]
        try:
            result = func(*args, **kwargs)
            return result
            instance.error_num = 0

        except Exception as e:
            # 若发现异常，保存截图
            instance.driver.save_screenshot('tmp.png')
            with open('tmp.png', 'rb') as f:
                photo = f.read()
            allure.attach(photo, name="异常信息截图",
                          attachment_type=allure.attachment_type.PNG)
            # 如果查询黑名单次数大于最大查询次数，抛出异常
            if instance.error_num > instance.max_num:
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
