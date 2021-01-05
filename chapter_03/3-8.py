# 5 个你渴望去旅游的地方
local = [ 'USA', 'UK', 'Japan', 'Korea', 'Singapore' ]
# 按原始排列顺序打印该列表
print(local)
# 使用 sorted() 按字母顺序打印这个列表,同时不要修改它
print(sorted(local))
# 再次打印该列表,核实排列顺序未变
print(local)
# 使用 reverse() 修改列表元素的排列顺序。打印该列表,核实排列顺序确实变了
local.reverse()
print(local)
# 使用 reverse() 再次修改列表元素的排列顺序
local.reverse()
print(local)
# 使用 sort() 修改该列表,使其元素按字母顺序排列
local.sort()
print(local)
# 使用 sort() 修改该列表,使其元素按与字母顺序相反的顺序排列
local.sort(reverse=True)
print(local)
