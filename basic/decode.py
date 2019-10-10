print(len(b"ABC"))
# 3
print(len(b"\xe4\xb8\xad\xe6\x96\x87"))
# 6
print(len("中文".encode("utf-8")))
# 6


print(len("ABC"))
# 3
print(len("中文"))
# 2

print(b"\xe4\xb8\xad\xff".decode("utf-8", errors="ignore"))
# '中'

print(b"ABC".decode("ascii"))
# 'ABC'
print(b"\xe4\xb8\xad\xe6\x96\x87".decode("utf-8"))
# '中文'
print(b"\xe4\xb8\xad\xff".decode("utf-8"))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte

