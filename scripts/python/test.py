# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "%d %d" % (self.x, self.y )
#
#
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))


# point1 = Point(1,2)
# # print(point1)
# # print(vars(point1))
# print_attributes(point1)

class Kangaroo:
    """A Kangaroo is a marsupial."""

    # def __init__(self, name, contents=[]):
    # 列表是可变的，只初始化了一次，所以每一个袋鼠都可以看到其他袋鼠列表的变化
    def __init__(self, name, contents=None):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        self.name = name

        if contents is None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)

# print_attributes(roo)