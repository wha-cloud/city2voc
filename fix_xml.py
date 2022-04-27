try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET


source_path = 'C:\\Users\\wha\\Desktop\\新建文件夹 (2)\\'

rootdir = source_path + 'trainval.txt'
gt = open(rootdir).read().splitlines()
need = ['bicycle', 'bird', 'car', 'cat', 'dog', 'person']
zero = []
for i in range(len(gt)):

  path = source_path + 'Annotations\\' + gt[i] + '.xml'
  # path = source_path + 'ann\\' + gt[i] + '.xml'

  tree = ET.parse(path)  # 将xml解析为树
  root = tree.getroot()       # 获取根节点



  # for obj in range(len(root)):
  #   # print(obj.text)
  #   object1 = root[obj].tag
  #   if object1 == 'object':
  #     if root[obj].text not in need:
  #       print(root[obj].text)
  #       root.remove(root[obj])
  j = 0
  remove1 = []
  for obj in root:
    # print(obj.text)
    if obj.tag == 'object':
      if obj[0].text not in need:
        print(obj[0].text)
        remove1.append(j)
    j+=1

  if len(remove1)>0:
    for l in range(len(remove1)):
      root.remove(root[remove1[l]-l])

  tree.write(path, 'UTF-8')

  fix = True
  for obj in root:
    if obj.tag == 'object':
      fix = False
      break
  if fix:
    zero.append(gt[i])

with open("C:/Users/wha/Desktop/新建文件夹 (2)/zero.txt", "a") as f:
  for i in range(len(zero)):
    f.write(zero[i] + "\n")

    # print(student[0].text) # 打印名字