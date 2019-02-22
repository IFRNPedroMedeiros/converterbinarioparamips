def oper(x):
  l = []
  h = []
  a = 32 * 2
  for i in range(6):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[0+i])))
  return sum(h)

def funct(y):
  l = []
  h = []
  a = 32 * 2
  for i in range(6):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[25+i])))
  return sum(h)

def rs(z):
  l = []
  h = []
  a = 16 * 2
  for i in range(5):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[6+i])))
  return sum(h)

def rt(q):
  l = []
  h = []
  a = 16 * 2
  for i in range(5):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[11+i])))
  return sum(h)

def rd(s):
  l = []
  h = []
  a = 16 * 2
  for i in range(5):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[16+i])))
  return sum(h)

def imm(r):
  l = []
  h = []
  a = 32768 * 2
  for i in range(15):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[16+i])))  
  return sum(h)

def end(u):
  l = []
  h = []
  a = 33554432 * 2
  for i in range(25):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[6+i])))  
  return sum(h)

b = input('')
bina = list(b)

if oper(bina) == 0:
  if funct(bina) == 32: f = 'add'
  else: f = 'sub'
  print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))

if oper(bina) == 32:
  f = 'lb'
  print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
elif oper(bina) == 33:
  f = 'lh'
  print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
elif oper(bina) == 35:
  f = 'lw'
  print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))

if oper(bina) == 2:
  f = 'j'
  print("{} {})".format(f, end(bina)))
elif oper(bina) == 3:
  f = 'jal'
  print("{} {})".format(f, end(bina)))