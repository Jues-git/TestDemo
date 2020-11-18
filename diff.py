import difflib


class meth_diff:
    def setup_class(self):
        with open('./test.xlsx', 'rw') as f:
            self.file_a = f.readlines()
        with open('./test1.xlsx', 'rw') as g:
            self.file_b = g.readlines()
        a = ['a', 'b', 'c', 'd']
        b = ['d', 'b', 'c', 'e']

    def html_diff(self):
        # 以Html展示差别
        h = difflib.HtmlDiff()
        re = h.make_file(self.file_a, self.file_b)
        print(re)

    def diff_text(self):
        # 以文本形式展示
        c_re = difflib.context_diff(self.file_a, self.file_b)
        print([i for i in c_re])
        # 返回 ['*** \n', '--- \n', '***************\n', '*** 1,4 ****\n', '! a', '  b', '  c', '! d',
        # '--- 1,4 ----\n', '! d', '  b', '  c', '! e']
        u_re = difflib.unified_diff(self.file_a, self.file_b)  # 结果是个生成器
        print([i for i in u_re])
        # 返回['--- \n', '+++ \n', '@@ -1,4 +1,4 @@\n', '-a', '+d', ' b', ' c', '-d', '+e']
        n_re = difflib.ndiff(self.file_a, self.file_b)
        print([i for i in n_re])
        # 返回 ['- a', '+ d', '  b', '  c', '- d', '+ e']
        """
        ‘-’	序列1独有
        ‘+’	序列2独有
        ‘ ‘	两个序列都有
        ‘?’	行不在任一输入序列
        """
        di = difflib.Differ()
        di_re = di.compare(self.file_a, self.file_b)
        print([i for i in di_re])
        # - "a,b,c
        # +  b,c,d
