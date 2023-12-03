ldc R2 @arr_length
ldc R0 0

#set length of array here
ldc R1 28
str R1 R2

ldc R2 @array
# initialise array
loop1:
str R1 R2
prm R2
inc R2
dec R1
bne R1 @loop1

# initialisation done

# headpointer
ldc R0 @array
# tailpointer
ldc R1 @array
ldc R3 @arr_length
ldr R2 R3
#now pointing to tail
add R1 R2

ldc R2 0
ldc R3 0

loop2:
# load head
ldr R2 R0

# load tail
ldr R3 R1

# swap
swp R2 R3

# load back into array
str R2 R0
str R3 R1


# increment head by one
inc R0
#store head and tail indexes
cpy R2 R0
cpy R3 R1
#compute difference of head and tail
sub R3 R2
# if even amount of elements in array, will break here
beq R3 @end

# we have to first check condition above, otherwise even amount of elements would not break
# decrement tail
dec R1

# store again indexes
cpy R2 R0
cpy R3 R1

#compute difference of actual head and tail
sub R3 R2

end:
# if odd elements in array, will break here
bne R3 @loop2

#print array
ldc R3 @arr_length
ldr R1 R3
ldc R0 0
ldc R2 @array

loop3:
prm R2
inc R2
dec R1
bne R1 @loop3
prm R2

hlt

.data
array:30
arr_length: 1
