"""
format
文字列に変数を組み込んで使うことができる
"""

person = 'Araragi'
txt = '{}さん、こんにちは！'.format(person)
print(txt)

person2 = 'Kamijo'
txt2 = f'{person2}さん、こんにちは！'
print(txt2)

person3 = 'Misaka'
txt3 = '%sさん、こんにちは！'%(person3)
print(txt3)