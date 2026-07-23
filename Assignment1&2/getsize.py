
from sys import getsizeof

x=10
'''+----------------+
| Object Header  |
+----------------+
| Ref Count      |
+----------------+
| Type Pointer   |
+----------------+
| Integer Value  |
+----------------+'''
y=3.14
lst=[34,56,89,34,56,78,90]
'''
List Object

+--------------------+
| Header             |
+--------------------+
| Size               |
+--------------------+
| Pointer --> int 10 |
| Pointer --> int 20 |
| Pointer --> int 30 |
+--------------------+'''


s = "Python"
'''
+-------------------+
| Header            |
+-------------------+
| Length            |
+-------------------+
| Encoding Info     |
+-------------------+
| Characters        |
+-------------------+'''

print(getsizeof(x))
print(getsizeof(y))
print(getsizeof(lst))
print(getsizeof(s))

help(int)