import pandas as pd
import numpy as np
import jieba
import jieba.posseg as pseg
from jieba import analyse
import os
import gensim
gensim.models.doc2vec.bu

# table = pd.read_csv('爬取的新闻0609.csv')
# #print(table.head())
# news_title1 = table['news_title'][0:50]
# news_title2 = table['news_title'][50:100]
# print(type(news_title), len(news_title1))
# list_50 = str(list(news_title1))
# list_100 = str(list(news_title2))
# with open('list_50.txt', 'w') as a:
#     a.write(list_50)

# with open('list_100.txt', 'w') as b:
#     b.write(list_100)
# #print(dict_50)

class TextSimilarity(object):
    def __init__(self, file_a, file_b):
        '''
        初始化类行
        '''
        str_a = ''
        str_b = ''
        if not os.path.isfile(file_a):
            print(file_a, "is not file")
            return
        elif not os.path.isfile(file_b):
            print(file_b, "is not file")
            return
        else:
            with open(file_a, 'r') as f:
                for line in f.readlines():
                    str_a += line.strip()

                f.close()
            with open(file_b, 'r') as f:
                for line in f.readlines():
                    str_b += line.strip()

                f.close()

        self.str_a = str_a
        self.str_b = str_b
        # print(str_a)

    def lcs(self, str_a, str_b):
        lensum = float(len(str_a) + len(str_b))
        # 得到一个二维的数组，类似用dp[lena+1][lenb+1],并且初始化为0
        lengths = [[0 for j in range(len(str_b) + 1)] for i in range(len(str_a) + 1)]

        # enumerate(a)函数： 得到下标i和a[i]
        #x 的位置为什么没更新呢？
        for i, x in enumerate(str_a):
            for j, y in enumerate(str_b):
                if x == y:
                    lengths[i + 1][j + 1] = lengths[i][j] + 1
                else:
                    lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

        # 到这里已经得到最长的子序列的长度，下面从这个矩阵中就是得到最长子序列
        result = ""
        x, y = len(str_a), len(str_b)
        while x != 0 and y != 0:
            # 证明最后一个字符肯定没有用到
            if lengths[x][y] == lengths[x - 1][y]:
                x -= 1
            elif lengths[x][y] == lengths[x][y - 1]:
                y -= 1
            else:  # 用到的从后向前的当前一个字符
                assert str_a[x - 1] == str_b[y - 1]  # 后面语句为真，类似于if(a[x-1]==b[y-1]),执行后条件下的语句
                result = str_a[x - 1] + result  # 注意这一句，这是一个从后向前的过程
                x -= 1
                y -= 1

                # 和上面的代码类似
                # if str_a[x-1] == str_b[y-1]:
                #    result = str_a[x-1] + result #注意这一句，这是一个从后向前的过程
                #    x -= 1
                #    y -= 1
        longestdist = lengths[len(str_a)][len(str_b)]
        ratio = longestdist / min(len(str_a), len(str_b))
        # return {'longestdistance':longestdist, 'ratio':ratio, 'result':result}
        print("longestdist:", longestdist)
        print('result:', result)
        print(len(result))
        print(ratio)
        return ratio


a = TextSimilarity('list_50.txt', 'list_100.txt')
a.lcs(a.str_a, a.str_b)

