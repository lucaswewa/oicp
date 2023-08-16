from ctypes import *

print(windll.kernel32)
print(cdll.msvcrt)
print(windll.kernel32.GetModuleHandleW)
print(hex(windll.kernel32.GetModuleHandleA(32)))