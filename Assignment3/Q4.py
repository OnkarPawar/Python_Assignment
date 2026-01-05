# Explain why string are immutable in python
# => 1. Hashability for Dictionary Keys: To be used as keys in a dictionary 
# (which are implemented as hash tables), an object must be "hashable," 
# meaning its hash value must not change
# 2. Memory Efficiency and String Interning: Python optimizes memory usage by "interning" (reusing) 
# commonly used or short string literals. Multiple variables can point to the same memory location 
# for an identical string value. If a string were mutable, 
# changing it through one variable would unexpectedly affect all other variables 
# referencing the same object. Immutability prevents this issue, 
# allowing safe sharing of string objects.
