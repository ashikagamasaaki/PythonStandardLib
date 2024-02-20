"""
any
iterableのどれかひとつでもTrueであればTrueを返す。
すべてFalseならFalseが返る。
"""

datas = [True, True, True, False, True]

if any(datas):
    print('どれかTrue')    # こっちが出力
else:
    print('すべてFalse')



# 内包表記にも使用可能
nums = [5,6,7,8,9]

if all(num < 4 for num in nums):
    print('どれか4より大きい')
else:
    print('すべて4以下')  # こっちが出力
