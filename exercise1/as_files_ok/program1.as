# Testing ldc, ldr, cpy, str, hlt
# R0 Tests ldc
# R1 Tests ldr
# R2 Tests cpy
# R3 Tests str

ldc R0 2
ldr R1 R0
ldc R2 0
ldc R3 0
cpy R2 R0
str R3 R0
hlt
