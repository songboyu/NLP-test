from IM import InputMethod

if __name__ == '__main__':
  im = InputMethod()
  print im.translate(['a','li','ba','ba','ji','tuan'])
  print im.translate(['ce','shi','zhong','wen','shu','ru','fa'])
  print im.translate(['zhong','hua','ren','min','gong','he','guo'])
  print im.translate(['yi','zhi','mei','li','de','xiao','hua'])
  print im.translate(['wo','ai','bei','jing','tian','an','men'])

  while True:
    pinyins = raw_input("pinyin: ")
    print im.translate(pinyins.split())