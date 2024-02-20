"""
all
iterableのすべての要素がTrueであればTrueを返す。
ひとつでもFalseならFalseが返る。
"""

datas = [True, True, True, False, True]

if all(datas):
    print('すべてTrue')
else:
    print('どれかFalse')    # こっちが出力



# 内包表記にも使用可能
nums = [5,6,7,8,9]

if all(num > 4 for num in nums):
    print('すべて4より大きい')  # こっちが出力
else:
    print('どれか4以下')
