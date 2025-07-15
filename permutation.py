def permute(items, level):
    if level <= 1:
        yield items
    else:
        for perm in permute(items[1:], level):
            for i in range(level):
                level = level - 1
                yield perm[:i] + items[0:1] + perm[i:]
                
if __name__ == '__main__':
    items = [1,2,3,4]
    permute(items, len(items))

''' OUTPUT:
[1, 2, 3, 4]
[2, 3, 4, 1]
[3, 4, 1, 2]
[4, 1, 2, 3]
'''

