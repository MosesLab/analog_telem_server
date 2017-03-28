
import agilent
from conversions import *
from tabulate import tabulate

# initialize the serial port
adc = agilent.init_serial()


t_ccd_cold_block = T_CCD_COLD_BLOCK()
t_cf_plusy = T_CF_plusY()
t_cf_minusy = T_CF_minusY()
t_cf_zeroy = T_CF_zeroY()
t_bp_zeroy = T_BP_zeroY()
t_fc_cold_block = T_FC_COLD_BLOCK()
t_fc_cpu = T_FC_CPU()
t_fc_5v_reg = T_FC_5V_REG()
t_fc_fpga = T_FC_FPGA()
t_roe = T_ROE()
t_roe_psu = T_ROE_PSU()
t_pwr_box_interior = T_PWR_BOX_INTERIOR()
t_pwr_12v_reg = T_PWR_12V_REG()
roe_psu_imon = ROE_PSU_IMON()
roe_psu_vmon = ROE_PSU_VMON()
shut_vmon = SHUT_VMON()
shut_imon = SHUT_IMON()
fc_imon = FC_IMON()
fc_vmon = FC_VMON()
tmu_imon = TMU_IMON()
tmu_vmon = TMU_VMON()
battvcc_imon = BATTVCC_IMON()
batt_28v_vcc_vmon = BATT_28V_VCC_VMON()
vout_28v_in_vmon = VOUT_28V_IN_VMON()
vout_28v_in_imon = VOUT_28V_IN_IMON()
t_liss_mount = T_LISS_MOUNT()

conversions = [t_ccd_cold_block, t_cf_plusy, t_cf_minusy, t_cf_zeroy, t_bp_zeroy, t_fc_cold_block, t_fc_cpu, t_fc_5v_reg, t_fc_fpga, t_roe, t_roe_psu, t_pwr_box_interior, t_pwr_12v_reg, roe_psu_imon, roe_psu_vmon, shut_vmon, shut_imon, fc_imon, fc_vmon, tmu_imon, tmu_vmon, battvcc_imon, batt_28v_vcc_vmon, vout_28v_in_vmon, vout_28v_in_imon, t_liss_mount]
conversions.sort(key=lambda x: x.chan)
#chan_max = max(x.chan for x in conversions)
#chan_min = min(x.chan for x in conversions)
chan_min = 101
chan_max = 102
print(chan_min)
chan_lst = [i for i in range(chan_min, chan_max+1)]

vheader = ["Channel Name", "Value"]

while(True):

    print("______________________________________________")


    # Perform measurement
    m_str = agilent.measure(adc, chan_min, chan_max+1)
    m_lst = m_str.split(",")


    vtable = []

    for i in chan_lst:

        conv_ind = [j for j, x in enumerate(conversions) if x.chan == i]

        if(len(conv_ind) == 1):
            this_conv = conversions[conv_ind[0]]
            #print(this_conv.str, this_conv.eq(float(m_lst[i - chan_min])))
            vtable.append([this_conv.str, str('%.3f' % this_conv.eq(float(m_lst[i - chan_min]))) + " " + this_conv.units])

        else :
            print("incorrect channel specification")

    print(tabulate(vtable, headers=vheader))

