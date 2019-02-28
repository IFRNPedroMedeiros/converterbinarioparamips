def oper(x):
  l = []
  h = []
  a = 64
  for i in range(6):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[0+i])))
  return sum(h)

def funct(y):
  l = []
  h = []
  a = 64
  for i in range(6):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[26+i])))
  return sum(h)

def rs(z):
  l = []
  h = []
  a = 32
  for i in range(5):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[6+i])))
  return sum(h)

def sa(m):
  l = []
  h = []
  a = 32
  for i in range(5):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[21+i])))
  return sum(h)

def rt(q):
  l = []
  h = []
  a = 32
  for i in range(5):
    l.append(int(a / 2))
    a = int(l[i])
    h.append(int(l[i])*(int(bina[11+i])))
  return sum(h)

def rd(s):
  l = []
  h = []
  a = 32
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

b = input()
bina = list(b)

while len(bina) != 0:

    if oper(bina) == 0:
        if funct(bina) ==0:
            f = 'SLL'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 8:
            f = 'JR'
            print("{} ${}".format(f, rs(bina)))
        elif funct(bina) == 9:
            f = 'JALR'
            print("{} ${}".format(f, rs(bina)))
            print("{} ${}, ${}".format(f, rd(bina), rs(bina)))
        elif funct(bina) == 13:
            f = 'BREAK'
            print(f)
        elif funct(bina) == 20:
            f = 'DSLLV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 22:
            f = 'DSRLV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 23:
            f = 'DSRAV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 26:
            f = 'DIV'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 27:
            f = 'DIVU'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 28:
            f = 'DMULT'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 29:
            f = 'DMULTU'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 30:
            f = 'DDIV'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 31:
            f = 'DDIVU'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        
        if funct(bina) == 32: f = 'ADD'
        elif funct(bina) == 33: f = 'ADDU'
        elif funct(bina) == 34: f = 'SUB'
        elif funct(bina) == 35: f = 'SUBU'
        elif funct(bina) == 36: f = 'AND'
        elif funct(bina) == 37: f = 'OR'
        elif funct(bina) == 38: f = 'XOR'
        elif funct(bina) == 39: f = 'NOR'
        elif funct(bina) == 41: f = 'DADD'
        elif funct(bina) == 42: f = 'SLT'
        elif funct(bina) == 43: f = 'SLTU'
        elif funct(bina) == 45: f = 'DADDU'
        elif funct(bina) == 46: f = 'DSUB'
        elif funct(bina) == 47: f = 'DSUBU'
        elif funct(bina) == 56:
            f = 'DSLL'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 57:
            f = 'DSRL'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 59:
            f = 'DSRA'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 60:
            f = 'DSLL32'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 62:
            f = 'DSRL32'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 63:
            f = 'DSRA32'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))

    if oper(bina) == 1:
        if rt(bina) == 0: f = 'BLTZ'
        elif rt(bina) == 1: f = 'BGEZ'
        elif rt(bina) == 2: f = 'BLTZL'
        elif rt(bina) == 3: f = 'BGEZL'
        elif rt(bina) == 16: f = 'BLTZAL'
        elif rt(bina) == 17: f = 'BGEZAL'
        elif rt(bina) == 18: f = 'BLTZALL'
        elif rt(bina) == 19: f = 'BGEZALL'
        print("{} ${}, {}".format(f, rs(bina), imm(bina)))
    elif oper(bina) == 6:
        if rt(bina) == 0:
            f = 'BLEZ'
        print("{} ${}, {}".format(f, rs(bina), imm(bina)))
    elif oper(bina) == 7:
        if rt(bina) == 0:
            f = 'BGTZ'
        print("{} ${}, {}".format(f, rs(bina), imm(bina)))
    elif oper(bina) == 22:
        if rt(bina) == 0:
            f = 'BLEZL'
        print("{} ${}, {}".format(f, rs(bina), imm(bina)))
    elif oper(bina) == 23:
        if rt(bina) == 0:
            f = 'BGTZL'
        print("{} ${}, {}".format(f, rs(bina), imm(bina)))

    if oper(bina) == 4:
        f = 'BEQ'
        print("{} ${}, ${}, {}".format(f, rs(bina), rt(bina), imm(bina)))
    elif oper(bina) == 5:
        f = 'BNE'
        print("{} ${}, ${}, {}".format(f, rs(bina), rt(bina), imm(bina)))
    elif oper(bina) == 20:
        f = 'BEQL'
        print("{} ${}, ${}, {}".format(f, rs(bina), rt(bina), imm(bina)))
    elif oper(bina) == 21:
        f = 'BNEL'
        print("{} ${}, ${}, {}".format(f, rs(bina), rt(bina), imm(bina)))
    elif oper(bina) == 8:
        f = 'ADDI'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 9:
        f = 'ADDIU'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 12:
        f = 'ANDI'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 24:
        f = 'DADDI'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 25:
        f = 'DADDIU'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 32:
        f = 'LB'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 33:
        f = 'LH'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 34:
        f = 'LWL'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 35:
        f = 'LW'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 36:
        f = 'LBU'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 37:
        f = 'LHU'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 38:
        f = 'LHU'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 40:
        f = 'SB'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 41:
        f = 'SH'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 42:
        f = 'SWL'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 43:
        f = 'SW'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 43:
        f = 'SDL'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 45:
        f = 'SDR'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 46:
        f = 'SWR'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 51:
        f = 'SDC1'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 52:
        f = 'SDC2'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 54:
        f = 'SC'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 55:
        f = 'LD'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 60:
        f = 'SCD'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 63:
        f = 'SD'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))

    if oper(bina) == 2:
        f = 'j'
        print("{} {})".format(f, end(bina)))
    elif oper(bina) == 3:
        f = 'jal'
        print("{} {})".format(f, end(bina)))
    elif oper(bina) == 16:
        f = 'COP0'
        print("{} {})".format(f, end(bina)))
    elif oper(bina) == 17:
        f = 'COP1'
        print("{} {})".format(f, end(bina)))
    elif oper(bina) == 18:
        f = 'COP2'
        print("{} {})".format(f, end(bina)))
    elif oper(bina) == 19:
        f = 'COP3'
        print("{} {})".format(f, end(bina)))

    del bina[0:31]
