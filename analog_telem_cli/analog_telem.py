
import agilent

# initialize the serial port
adc = agilent.init_serial()


T_CCD_COLD_BLOCK = 0
T_CF_plusY = 1
T_CF_minusY = 2
T_CF_zeroY = 3
T_BP_zeroY = 4
T_FC_COLD_BLOCK = 5
T_FC_CPU = 6
T_FC_5V_REG = 7
T_FC_FPGA = 8
T_ROE = 9
T_ROE_PSU = 10
T_PWR_BOX_INTERIOR = 11
T_PWR_12V_REG = 12
ROE_PSU_IMON = 13
ROE_PSU_VMON = 14
SHUT_VMON = 15
SHUT_IMON = 16

name_strs = [0 for col in range(T_CCD_COLD_BLOCK, SHUT_IMON+1)]
name_strs[T_CCD_COLD_BLOCK] = "T_CCD_COLD_BLOCK"
name_strs[T_CF_plusY] = "T_CF_+Y"
name_strs[T_CF_minusY] = "T_CF_-Y"
name_strs[T_CF_zeroY] = "T_CF_0Y"
name_strs[T_BP_zeroY] = "T_BP_0Y"
name_strs[T_FC_COLD_BLOCK] = "T_FC_COLD_BLOCK"
name_strs[T_FC_CPU] = "T_FC_CPU"
name_strs[T_FC_5V_REG] = "T_FC_5V_REG"
name_strs[T_FC_FPGA] = "T_FC_FPGA"
name_strs[T_ROE] = "T_ROE"
name_strs[T_ROE_PSU] = "T_ROE_PSU"
name_strs[T_PWR_BOX_INTERIOR] = "T_PWR_BOX_INTERIOR"
name_strs[T_PWR_12V_REG] = "T_PWR_12V_REG"
name_strs[ROE_PSU_IMON] = "ROE_PSU_IMON"
name_strs[ROE_PSU_VMON] = "ROE_PSU_VMON"
name_strs[SHUT_VMON] = "SHUT_VMON"
name_strs[SHUT_IMON] = "SHUT_IMON"

while(True):

    print("______________________________________________")

    # Perform measurement
    m_str = agilent.measure(adc, 101+0, 101+16)
    m_lst = m_str.split(",")

    for i in range(0,16):

        print(name_strs[i],m_lst[i])



