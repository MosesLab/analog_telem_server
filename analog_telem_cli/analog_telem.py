
import agilent
from conversions import *

# initialize the serial port
adc = agilent.init_serial()


t_ccd_cold_block = T_CCD_COLD_BLOCK
t_cf_plusy = T_CF_plusY
t_cf_minusy = T_CF_minusY
t_cf_zeroy = T_CF_zeroY
t_bp_zeroy = T_BP_zeroY
t_fc_cold_block = T_FC_COLD_BLOCK
t_fc_cpu = T_FC_CPU
t_fc_5v_reg = T_FC_5V_REG
t_fc_fpga = T_FC_FPGA
t_roe = T_ROE
t_roe_psu = T_ROE_PSU
t_pwr_box_interior = T_PWR_BOX_INTERIOR
t_pwr_12v_reg = T_PWR_12V_REG
roe_psu_imon = ROE_PSU_IMON
roe_psu_vmon = ROE_PSU_VMON
shut_vmon = SHUT_VMON
shut_imon = SHUT_IMON
fc_imon = FC_IMON
fc_vmon = FC_VMON
tmu_imon = TMU_IMON
tmu_vmon = TMU_VMON
battvcc_imon = BATTVCC_IMON
batt_28v_vcc_vmon = BATT_28V_VCC_VMON
vout_28v_in_vmon = VOUT_28V_IN_VMON
vout_28v_in_imon = VOUT_28V_IN_IMON
t_liss_mount = T_LISS_MOUNT


while(True):

    print("______________________________________________")

    # Perform measurement
    m_str = agilent.measure(adc, 101+0, 101+16)
    m_lst = m_str.split(",")

    for i in range(0,16):

        print(name_strs[i],m_lst[i])



