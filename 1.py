
rmb_str_value = input('输入人民币金额：')

usd_vs_rmb = 6.77

rmb_value = eval(rmb_str_value)

usd_value = rmb_value / usd_vs_rmb

print(usd_value)
