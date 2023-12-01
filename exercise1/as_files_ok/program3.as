# Testing ldc, prm, prr, add, beq, hlt

ldc R1 2
ldc R0 1
ldc R2 1
prm R1
prr R1
add R1 R0
beq R1 2
beq R0 1
sub R0 R1
loop:
sub R0 R2
beq R0 @loop
hlt
