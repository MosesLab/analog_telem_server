import math

def steinhart(V, Rb):
    C1 = 1.285e-3
    C2 = 2.362e-4
    C3 = 9.285e-8
    Vin = 12.
    R = (-Rb * V + Rb * Vin) / V
    return 1 / (C1 + C2 * math.log(R) + C3 * math.pow(math.log(R), 3))

class T_CCD_COLD_BLOCK:
    units = "C"
    bias = 2.84e6
    def __init__(self,  chan):
        self.chan = chan
    def eq(self, V):
        return steinhart(V, bias)



class T_CF_plusY:
class T_CF_minusY:
class T_CF_zeroY:
class T_BP_zeroY:
class T_FC_COLD_BLOCK:
class T_FC_CPU:
class T_FC_5V_REG:
class T_FC_FPGA:
class T_ROE:
class T_ROE_PSU:
class T_PWR_BOX_INTERIOR:
class T_PWR_12V_REG:
class ROE_PSU_IMON:
class ROE_PSU_VMON:
class SHUT_VMON:
class SHUT_IMON:

