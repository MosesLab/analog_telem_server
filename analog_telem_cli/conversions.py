import math

def steinhart(V, Rb):
    C1 = 1.285e-3
    C2 = 2.362e-4
    C3 = 9.285e-8
    Vin = 12.

    if V <= 0:
        V = 1e-6

    #R = (-Rb * V + Rb * Vin) / V
    R = -Rb * V / (V-Vin)
    return 1 / (C1 + C2 * math.log(R) + C3 * math.pow(math.log(R), 3)) - 273.15

class T_CCD_COLD_BLOCK:
    units = "C"
    bias = 2.84e6
    chan = 101
    str = "T_CCD_COLD_BLOCK"
    def eq(self, V):
        return steinhart(V, self.bias)

class T_CF_plusY:
    units = "C"
    bias = 433e3
    chan = 102
    str = "T_CF_+Y"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_CF_minusY:
    units = "C"
    bias = 433e3
    chan = 103
    str = "T_CF_-Y"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_CF_zeroY:
    units = "C"
    bias = 433e3
    chan = 104
    str = "T_CF_0Y"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_BP_zeroY:
    units = "C"
    bias = 433e3
    chan = 105
    str = "T_BP_0Y"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_FC_COLD_BLOCK:
    units = "C"
    bias = 88.7e3
    chan = 106
    str = "T_FC_COLD_BLOCK"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_FC_CPU:
    units = "C"
    bias = 11.4e3
    chan = 107
    str = "T_FC_CPU"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_FC_5V_REG:
    units = "C"
    bias = 11.4e3
    chan = 108
    str = "T_FC_5V_REG"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_FC_FPGA:
    units = "C"
    bias = 11.4e3
    chan = 109
    str = "T_FC_FPGA"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_ROE:
    units = "C"
    bias = 29.8e3
    chan = 110
    str = "T_ROE"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_ROE_PSU:
    units = "C"
    bias = 11.4e3
    chan = 111
    str = "T_ROE_PSU"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_PWR_BOX_INTERIOR:
    units = "C"
    bias = 11.4e3
    chan = 112
    str = "T_PWR_BOX_INTERIOR"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class T_PWR_12V_REG:
    units = "C"
    bias = 11.4e3
    chan = 113
    str = "T_PWR_12V_REG"
    def eq(self, V):
        return steinhart(V, self.bias)
    
class ROE_PSU_IMON:
    units = "A"
    chan = 114
    str = "ROE_PSU_IMON"
    def eq(self, V):
        return V/5
    
class ROE_PSU_VMON:
    units = "V"
    chan = 115
    str = "ROE_PSU_VMON"
    def eq(self, V):
        return 10.4*V
    
class SHUT_VMON:
    units = "V"
    chan = 116
    str = "SHUT_VMON"
    def eq(self, V):
        return 10.4*V
    
class SHUT_IMON:
    units = "A"
    chan = 117
    str = "SHUT_IMON"
    def eq(self, V):
        return V
    
class FC_IMON:
    units = "A"
    chan = 118
    str = "FC_IMON"
    def eq(self, V):
        return V/2
    
class FC_VMON:
    units = "V"
    chan = 119
    str = "FC_VMON"
    def eq(self, V):
        return 5*V
    
class TMU_IMON:
    units = "A"
    chan = 120
    str = "TMU_IMON"
    def eq(self, V):
        return V/10
    
class TMU_VMON:
    units = "V"
    chan = 121
    str = "TMU_VMON"
    def eq(self, V):
        return 5*V
    
class BATTVCC_IMON:
    units = "A"
    chan = 122
    str = "BATTVCC_IMON"
    def eq(self, V):
        return V

class BATT_28V_VCC_VMON:
    units = "V"
    chan = 123
    str = "28V_BATT_VCC_VMON"
    def eq(self, V):
        return 10.4*V
    
class VOUT_28V_IN_VMON:
    units = "V"
    chan = 124
    str = "28V_VOUT_IN_VMON"
    def eq(self, V):
        return 10.4*V
    
class VOUT_28V_IN_IMON:
    units = "A"
    chan = 125
    str = "28V_VOUT_IN_IMON"
    def eq(self, V):
        return V
    
class T_LISS_MOUNT:
    units = "C"
    bias = 11.4e3
    chan = 126
    str = "T_LISS_MOUNT"
    def eq(self, V):
        return steinhart(V, self.bias)
