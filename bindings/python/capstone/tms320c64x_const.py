from . import CS_OP_INVALID, CS_OP_REG, CS_OP_IMM, CS_OP_FP, CS_OP_PRED, CS_OP_SPECIAL, CS_OP_MEM, CS_OP_MEM_REG, CS_OP_MEM_IMM, UINT16_MAX, UINT8_MAX
# For Capstone Engine. AUTO-GENERATED FILE, DO NOT EDIT [tms320c64x_const.py]
TMS320C64X_OP_INVALID = CS_OP_INVALID
TMS320C64X_OP_REG = CS_OP_REG
TMS320C64X_OP_IMM = CS_OP_IMM
TMS320C64X_OP_REGPAIR = CS_OP_SPECIAL+0
TMS320C64X_OP_MEM = CS_OP_MEM

TMS320C64X_MEM_DISP_INVALID = 0
TMS320C64X_MEM_DISP_CONSTANT = 1
TMS320C64X_MEM_DISP_REGISTER = 2

TMS320C64X_MEM_DIR_INVALID = 0
TMS320C64X_MEM_DIR_FW = 1
TMS320C64X_MEM_DIR_BW = 2

TMS320C64X_MEM_MOD_INVALID = 0
TMS320C64X_MEM_MOD_NO = 1
TMS320C64X_MEM_MOD_PRE = 2
TMS320C64X_MEM_MOD_POST = 3

TMS320C64X_REG_INVALID = 0
TMS320C64X_REG_AMR = 1
TMS320C64X_REG_CSR = 2
TMS320C64X_REG_DIER = 3
TMS320C64X_REG_DNUM = 4
TMS320C64X_REG_ECR = 5
TMS320C64X_REG_GFPGFR = 6
TMS320C64X_REG_GPLYA = 7
TMS320C64X_REG_GPLYB = 8
TMS320C64X_REG_ICR = 9
TMS320C64X_REG_IER = 10
TMS320C64X_REG_IERR = 11
TMS320C64X_REG_ILC = 12
TMS320C64X_REG_IRP = 13
TMS320C64X_REG_ISR = 14
TMS320C64X_REG_ISTP = 15
TMS320C64X_REG_ITSR = 16
TMS320C64X_REG_NRP = 17
TMS320C64X_REG_NTSR = 18
TMS320C64X_REG_REP = 19
TMS320C64X_REG_RILC = 20
TMS320C64X_REG_SSR = 21
TMS320C64X_REG_TSCH = 22
TMS320C64X_REG_TSCL = 23
TMS320C64X_REG_TSR = 24
TMS320C64X_REG_A0 = 25
TMS320C64X_REG_A1 = 26
TMS320C64X_REG_A2 = 27
TMS320C64X_REG_A3 = 28
TMS320C64X_REG_A4 = 29
TMS320C64X_REG_A5 = 30
TMS320C64X_REG_A6 = 31
TMS320C64X_REG_A7 = 32
TMS320C64X_REG_A8 = 33
TMS320C64X_REG_A9 = 34
TMS320C64X_REG_A10 = 35
TMS320C64X_REG_A11 = 36
TMS320C64X_REG_A12 = 37
TMS320C64X_REG_A13 = 38
TMS320C64X_REG_A14 = 39
TMS320C64X_REG_A15 = 40
TMS320C64X_REG_A16 = 41
TMS320C64X_REG_A17 = 42
TMS320C64X_REG_A18 = 43
TMS320C64X_REG_A19 = 44
TMS320C64X_REG_A20 = 45
TMS320C64X_REG_A21 = 46
TMS320C64X_REG_A22 = 47
TMS320C64X_REG_A23 = 48
TMS320C64X_REG_A24 = 49
TMS320C64X_REG_A25 = 50
TMS320C64X_REG_A26 = 51
TMS320C64X_REG_A27 = 52
TMS320C64X_REG_A28 = 53
TMS320C64X_REG_A29 = 54
TMS320C64X_REG_A30 = 55
TMS320C64X_REG_A31 = 56
TMS320C64X_REG_B0 = 57
TMS320C64X_REG_B1 = 58
TMS320C64X_REG_B2 = 59
TMS320C64X_REG_B3 = 60
TMS320C64X_REG_B4 = 61
TMS320C64X_REG_B5 = 62
TMS320C64X_REG_B6 = 63
TMS320C64X_REG_B7 = 64
TMS320C64X_REG_B8 = 65
TMS320C64X_REG_B9 = 66
TMS320C64X_REG_B10 = 67
TMS320C64X_REG_B11 = 68
TMS320C64X_REG_B12 = 69
TMS320C64X_REG_B13 = 70
TMS320C64X_REG_B14 = 71
TMS320C64X_REG_B15 = 72
TMS320C64X_REG_B16 = 73
TMS320C64X_REG_B17 = 74
TMS320C64X_REG_B18 = 75
TMS320C64X_REG_B19 = 76
TMS320C64X_REG_B20 = 77
TMS320C64X_REG_B21 = 78
TMS320C64X_REG_B22 = 79
TMS320C64X_REG_B23 = 80
TMS320C64X_REG_B24 = 81
TMS320C64X_REG_B25 = 82
TMS320C64X_REG_B26 = 83
TMS320C64X_REG_B27 = 84
TMS320C64X_REG_B28 = 85
TMS320C64X_REG_B29 = 86
TMS320C64X_REG_B30 = 87
TMS320C64X_REG_B31 = 88
TMS320C64X_REG_PCE1 = 89
TMS320C64X_REG_ENDING = 90
TMS320C64X_REG_EFR = TMS320C64X_REG_ECR
TMS320C64X_REG_IFR = TMS320C64X_REG_ISR

TMS320C64X_INS_INVALID = 0
TMS320C64X_INS_ABS = 1
TMS320C64X_INS_ABS2 = 2
TMS320C64X_INS_ADD = 3
TMS320C64X_INS_ADD2 = 4
TMS320C64X_INS_ADD4 = 5
TMS320C64X_INS_ADDAB = 6
TMS320C64X_INS_ADDAD = 7
TMS320C64X_INS_ADDAH = 8
TMS320C64X_INS_ADDAW = 9
TMS320C64X_INS_ADDK = 10
TMS320C64X_INS_ADDKPC = 11
TMS320C64X_INS_ADDU = 12
TMS320C64X_INS_AND = 13
TMS320C64X_INS_ANDN = 14
TMS320C64X_INS_AVG2 = 15
TMS320C64X_INS_AVGU4 = 16
TMS320C64X_INS_B = 17
TMS320C64X_INS_BDEC = 18
TMS320C64X_INS_BITC4 = 19
TMS320C64X_INS_BNOP = 20
TMS320C64X_INS_BPOS = 21
TMS320C64X_INS_CLR = 22
TMS320C64X_INS_CMPEQ = 23
TMS320C64X_INS_CMPEQ2 = 24
TMS320C64X_INS_CMPEQ4 = 25
TMS320C64X_INS_CMPGT = 26
TMS320C64X_INS_CMPGT2 = 27
TMS320C64X_INS_CMPGTU4 = 28
TMS320C64X_INS_CMPLT = 29
TMS320C64X_INS_CMPLTU = 30
TMS320C64X_INS_DEAL = 31
TMS320C64X_INS_DOTP2 = 32
TMS320C64X_INS_DOTPN2 = 33
TMS320C64X_INS_DOTPNRSU2 = 34
TMS320C64X_INS_DOTPRSU2 = 35
TMS320C64X_INS_DOTPSU4 = 36
TMS320C64X_INS_DOTPU4 = 37
TMS320C64X_INS_EXT = 38
TMS320C64X_INS_EXTU = 39
TMS320C64X_INS_GMPGTU = 40
TMS320C64X_INS_GMPY4 = 41
TMS320C64X_INS_LDB = 42
TMS320C64X_INS_LDBU = 43
TMS320C64X_INS_LDDW = 44
TMS320C64X_INS_LDH = 45
TMS320C64X_INS_LDHU = 46
TMS320C64X_INS_LDNDW = 47
TMS320C64X_INS_LDNW = 48
TMS320C64X_INS_LDW = 49
TMS320C64X_INS_LMBD = 50
TMS320C64X_INS_MAX2 = 51
TMS320C64X_INS_MAXU4 = 52
TMS320C64X_INS_MIN2 = 53
TMS320C64X_INS_MINU4 = 54
TMS320C64X_INS_MPY = 55
TMS320C64X_INS_MPY2 = 56
TMS320C64X_INS_MPYH = 57
TMS320C64X_INS_MPYHI = 58
TMS320C64X_INS_MPYHIR = 59
TMS320C64X_INS_MPYHL = 60
TMS320C64X_INS_MPYHLU = 61
TMS320C64X_INS_MPYHSLU = 62
TMS320C64X_INS_MPYHSU = 63
TMS320C64X_INS_MPYHU = 64
TMS320C64X_INS_MPYHULS = 65
TMS320C64X_INS_MPYHUS = 66
TMS320C64X_INS_MPYLH = 67
TMS320C64X_INS_MPYLHU = 68
TMS320C64X_INS_MPYLI = 69
TMS320C64X_INS_MPYLIR = 70
TMS320C64X_INS_MPYLSHU = 71
TMS320C64X_INS_MPYLUHS = 72
TMS320C64X_INS_MPYSU = 73
TMS320C64X_INS_MPYSU4 = 74
TMS320C64X_INS_MPYU = 75
TMS320C64X_INS_MPYU4 = 76
TMS320C64X_INS_MPYUS = 77
TMS320C64X_INS_MVC = 78
TMS320C64X_INS_MVD = 79
TMS320C64X_INS_MVK = 80
TMS320C64X_INS_MVKL = 81
TMS320C64X_INS_MVKLH = 82
TMS320C64X_INS_NOP = 83
TMS320C64X_INS_NORM = 84
TMS320C64X_INS_OR = 85
TMS320C64X_INS_PACK2 = 86
TMS320C64X_INS_PACKH2 = 87
TMS320C64X_INS_PACKH4 = 88
TMS320C64X_INS_PACKHL2 = 89
TMS320C64X_INS_PACKL4 = 90
TMS320C64X_INS_PACKLH2 = 91
TMS320C64X_INS_ROTL = 92
TMS320C64X_INS_SADD = 93
TMS320C64X_INS_SADD2 = 94
TMS320C64X_INS_SADDU4 = 95
TMS320C64X_INS_SADDUS2 = 96
TMS320C64X_INS_SAT = 97
TMS320C64X_INS_SET = 98
TMS320C64X_INS_SHFL = 99
TMS320C64X_INS_SHL = 100
TMS320C64X_INS_SHLMB = 101
TMS320C64X_INS_SHR = 102
TMS320C64X_INS_SHR2 = 103
TMS320C64X_INS_SHRMB = 104
TMS320C64X_INS_SHRU = 105
TMS320C64X_INS_SHRU2 = 106
TMS320C64X_INS_SMPY = 107
TMS320C64X_INS_SMPY2 = 108
TMS320C64X_INS_SMPYH = 109
TMS320C64X_INS_SMPYHL = 110
TMS320C64X_INS_SMPYLH = 111
TMS320C64X_INS_SPACK2 = 112
TMS320C64X_INS_SPACKU4 = 113
TMS320C64X_INS_SSHL = 114
TMS320C64X_INS_SSHVL = 115
TMS320C64X_INS_SSHVR = 116
TMS320C64X_INS_SSUB = 117
TMS320C64X_INS_STB = 118
TMS320C64X_INS_STDW = 119
TMS320C64X_INS_STH = 120
TMS320C64X_INS_STNDW = 121
TMS320C64X_INS_STNW = 122
TMS320C64X_INS_STW = 123
TMS320C64X_INS_SUB = 124
TMS320C64X_INS_SUB2 = 125
TMS320C64X_INS_SUB4 = 126
TMS320C64X_INS_SUBAB = 127
TMS320C64X_INS_SUBABS4 = 128
TMS320C64X_INS_SUBAH = 129
TMS320C64X_INS_SUBAW = 130
TMS320C64X_INS_SUBC = 131
TMS320C64X_INS_SUBU = 132
TMS320C64X_INS_SWAP4 = 133
TMS320C64X_INS_UNPKHU4 = 134
TMS320C64X_INS_UNPKLU4 = 135
TMS320C64X_INS_XOR = 136
TMS320C64X_INS_XPND2 = 137
TMS320C64X_INS_XPND4 = 138
TMS320C64X_INS_IDLE = 139
TMS320C64X_INS_MV = 140
TMS320C64X_INS_NEG = 141
TMS320C64X_INS_NOT = 142
TMS320C64X_INS_SWAP2 = 143
TMS320C64X_INS_ZERO = 144
TMS320C64X_INS_ENDING = 145

TMS320C64X_GRP_INVALID = 0
TMS320C64X_GRP_JUMP = 1
TMS320C64X_GRP_FUNIT_D = 128
TMS320C64X_GRP_FUNIT_L = 129
TMS320C64X_GRP_FUNIT_M = 130
TMS320C64X_GRP_FUNIT_S = 131
TMS320C64X_GRP_FUNIT_NO = 132
TMS320C64X_GRP_ENDING = 133

TMS320C64X_FUNIT_INVALID = 0
TMS320C64X_FUNIT_D = 1
TMS320C64X_FUNIT_L = 2
TMS320C64X_FUNIT_M = 3
TMS320C64X_FUNIT_S = 4
TMS320C64X_FUNIT_NO = 5
