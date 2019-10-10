# >>> '中文'.encode('gb2312')
# b'\xd6\xd0\xce\xc4'

print(ord("A"))
# 65
print(ord("中"))
# 20013
print(chr(66))
# 'B'
print(chr(25991))
# '文'
print("\u4e2d\u6587")
# 中文

print("ABC".encode("ascii"))
# b'ABC'
print("中文".encode("utf-8"))
# b'\xe4\xb8\xad\xe6\x96\x87'
print("中文".encode("ascii"))
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

