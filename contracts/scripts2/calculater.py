import calculater.scripts.setting as setting
from collections import OrderedDict

#合計推定金額、個人推定金額、および比の算出
class BalanceCalculate:
    def __init__(self,ore_list,buy_coefficient):
        self.settings = setting.InitOrePrice()
        self.indi_ores = OrderedDict()
        self.total_balance = 0
        self.ore_list = ore_list
        self.buy_coefficient = float(int(buy_coefficient)/100)

    def balances(self):
        for i in range(len(self.ore_list)):
            self.indi_ores[self.ore_list[i][0]] = round(int(self.ore_list[i][1]) * self.settings.all_ore_price[self.ore_list[i][0]] * self.buy_coefficient)

            self.total_balance +=  round(int(self.ore_list[i][1]) * self.settings.all_ore_price[self.ore_list[i][0]] * self.buy_coefficient)

            dict = [self.indi_ores,self.total_balance]

        return dict
