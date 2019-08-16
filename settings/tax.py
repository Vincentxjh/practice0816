#此模块用于计算个人所得税（练习八008.py使用）
def tax_calculate(salary, preminm = 0, cost = 0,):
    '''
    功能：计算应缴纳的个人所得税
    :param salary: 工资
    :param preminm: 五险一金
    :param cost: 其他费用
    :return: 个人所得税额
    '''
    #应缴纳所得额 = 税前工资 - 起征点金额（5000）- 五险一金 - 附加费用
    payable = (salary - 5000 - preminm - cost)
    if payable < 0:
        tax = 0
    elif 0 < payable <= 3000:
        tax = (payable * 0.03) - 0
    elif 3000 < payable <= 12000:
        tax = (payable * 0.1) - 210
    elif 12000 < payable <= 25000:
        tax = (payable * 0.2) - 1410
    elif 25000 < payable <= 35000:
        tax = (payable * 0.25) - 2660
    elif 35000 < payable <= 55000:
        tax = (payable * 0.3) - 4410
    elif 55000 < payable <= 80000:
        tax = (payable * 0.35) - 7160
    else:
        tax = (payable * 0.45) - 15160
    return tax
