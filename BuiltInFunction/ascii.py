"""
ascii
印字可能な表現を含む文字列を返す。（python2のrepr()と同様）
"""

# 文字列をASCIIコードに変換
txt = 'Hello World, こんにちは世界'
ascii_txt = ascii(txt)
print(ascii_txt)    # 'Hello World, \u3053\u3093\u306b\u3061\u306f\u4e16\u754c'