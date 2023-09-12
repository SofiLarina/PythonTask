"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите cколько семей живёт в доме N.
"""
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)

join = max(set(newspaper).union(set(magazine))) - min(set(newspaper).union(set(magazine)))+1
print(join - (max(both) - min(both) + 1))

