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
        if funct(bina) == 0:
            f = 'SLL'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 2:
            f = 'SRL'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 3:
            f = 'SRA'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), sa(bina)))
        elif funct(bina) == 4:
            f = 'SLLV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 6:
            f = 'SRLV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 7:
            f = 'SRAV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 8:
            f = 'JR'
            print("{} ${}".format(f, rs(bina)))
        elif funct(bina) == 9:
            f = 'JALR'
            print("{} ${}".format(f, rs(bina)))
            print("{} ${}, ${}".format(f, rd(bina), rs(bina)))
        elif funct(bina) == 10:
            f = 'MOVZ'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 11:
            f = 'MOVN'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 12:
            f = 'SYSCALL'
            print(f)
        elif funct(bina) == 13:
            f = 'BREAK'
            print(f)
        elif funct(bina) == 15:
            f = 'SYNC'
            if sa(bina) == 0:
                print("{} implied".format(f))
            else:
                print("{} ${}".format(f, sa(bina)))
        elif funct(bina) == 16:
            f = 'MFHI'
            print("{} ${}".format(f, rd(bina)))
        elif funct(bina) == 17:
            f = 'MTHI'
            print("{} ${}".format(f, rs(bina)))
        elif funct(bina) == 18:
            f = 'MFLO'
            print("{} ${}".format(f, rd(bina)))
        elif funct(bina) == 19:
            f = 'MTLO'
            print("{} ${}".format(f, rs(bina)))
        elif funct(bina) == 20:
            f = 'DSLLV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 22:
            f = 'DSRLV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 23:
            f = 'DSRAV'
            print("{} ${}, ${}, ${}".format(f, rd(bina), rt(bina), rs(bina)))
        elif funct(bina) == 24:
            f = 'MULT'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 25:
            f = 'MULTU'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
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
        elif funct(bina) == 48:
            f = 'TGE'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 49:
            f = 'TGEU'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 50:
            f = 'TLT'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 51:
            f = 'TLTU'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
        elif funct(bina) == 54:
            f = 'TNE'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))

        if funct(bina) == 32:
          f = 'ADD'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 33:
          f = 'ADDU'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 34:
          f = 'SUB'

        elif funct(bina) == 35:
          f = 'SUBU'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 36:
          f = 'AND'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 37:
          f = 'OR'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 38:
          f = 'XOR'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 39:
          f = 'NOR'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 41:
          f = 'DADD'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 42:
          f = 'SLT'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 43:
          f = 'SLTU'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 45:
          f = 'DADDU'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 46:
          f = 'DSUB'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 47:
          f = 'DSUBU'
          print("{} ${}, ${}, ${}".format(f, rd(bina), rs(bina), rt(bina)))
        elif funct(bina) == 52:
            f = 'TEQ'
            print("{} ${}, ${}".format(f, rs(bina), rt(bina)))
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

    if oper(bina) == 1:
        if rt(bina) == 0:
          f = 'BLTZ'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 1:
          f = 'BGEZ'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 2:
          f = 'BLTZL'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 3:
          f = 'BGEZL'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 8:
          f = 'TGEI'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 9:
          f = 'TGEIU'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 10:
          f = 'TLTI'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 11:
          f = 'TLTIU'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 12:
          f = 'TEQI'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 14:
          f = 'TNEI'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 16:
          f = 'BLTZAL'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 17:
          f = 'BGEZAL'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 18:
          f = 'BLTZALL'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
        elif rt(bina) == 19:
          f = 'BGEZALL'
          print("{} ${}, {}".format(f, rs(bina), imm(bina)))
    elif oper(bina) == 6:
        f = 'BLEZ'
        print("{} ${}, {}".format(f, rs(bina), imm(bina)))
    elif oper(bina) == 7:
        f = 'BGTZ'
        print("{} ${}, {}".format(f, rs(bina), imm(bina)))
    elif oper(bina) == 22:
        f = 'BLEZL'
        print("{} ${}, {}".format(f, rs(bina), imm(bina)))
    elif oper(bina) == 23:
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
    elif oper(bina) == 10:
        f = 'SLTI'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 11:
        f = 'SLTIU'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 12:
        f = 'ANDI'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 13:
        f = 'ORI'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 14:
        f = 'XORI'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 15:
        f = 'LUI'
        print("{} ${}, {}".format(f, rt(bina), imm(bina)))
    elif oper(bina) == 24:
        f = 'DADDI'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 25:
        f = 'DADDIU'
        print("{} ${}, ${}, {}".format(f, rt(bina), rs(bina), imm(bina)))
    elif oper(bina) == 26:
        f = 'LDL'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 27:
        f = 'LDR'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
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
        f = 'LWR'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 39:
        f = 'LWU'
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
    elif oper(bina) == 44:
        f = 'SDL'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 45:
        f = 'SDR'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 46:
        f = 'SWR'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 48:
        f = 'LL'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 49:
        f = 'LWC1'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 50:
        f = 'LWC2'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 51:
        f = 'PREF'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 53:
        f = 'LDC1'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 54:
        f = 'LDC2'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 55:
        f = 'LD'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 56:
        f = 'SC'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 57:
        f = 'SWC1'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 58:
        f = 'SWC2'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 59:
        f = 'SWC3'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 60:
        f = 'SCD'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 61:
        f = 'SDC1'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 62:
        f = 'SDC2'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))
    elif oper(bina) == 63:
        f = 'SD'
        print("{} ${}, {}(${})".format(f, rt(bina), imm(bina), rs(bina)))

    if oper(bina) == 2:
        f = 'j'
        print("{} {}".format(f, end(bina)))
    elif oper(bina) == 3:
        f = 'jal'
        print("{} {}".format(f, end(bina)))
    elif oper(bina) == 16:
        f = 'COP0'
        print("{} {}".format(f, end(bina)))
    elif oper(bina) == 17:
        f = 'COP1'
        print("{} {}".format(f, end(bina)))
    elif oper(bina) == 18:
        f = 'COP2'
        print("{} {}".format(f, end(bina)))
    elif oper(bina) == 19:
        f = 'COP3'
        print("{} {}".format(f, end(bina)))

    del bina[0:32]
