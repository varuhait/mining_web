import scripts.setting as setting
from collections import OrderedDict

#合計推定金額、個人推定金額、および比の算出
class BalanceCalculate:
    def __init__(self,loot_list,buy_coefficient,fuel_tax):
        self.settings = setting.InitOrePrice()
        self.personal_balances = OrderedDict()
        self.personal_balances_ratio = OrderedDict()
        self.personal_ores = OrderedDict()
        self.personal_ores_quant = OrderedDict()
        self.personal_data = OrderedDict()
        self.personal_totals = OrderedDict()
        self.ore_balances = OrderedDict()
        self.total_balance = 0
        self.loot_list = loot_list
        self.buy_coefficient = buy_coefficient
        self.fuel_tax = fuel_tax
        self.efficiency = 0.73

    def balances(self):
        #プレイヤー、鉱石の辞書作成
        for i in range(len(self.loot_list)):
            self.personal_balances[self.loot_list[i][0]] = 0

            self.ore_balances[self.loot_list[i][2]] = 0

            if self.loot_list[i][0] in self.personal_ores:
                pass
            else:
                self.personal_ores[self.loot_list[i][0]] = OrderedDict()

            self.personal_ores[self.loot_list[i][0]][self.loot_list[i][2]] = 0

            if self.loot_list[i][0] in self.personal_ores_quant:
                pass
            else:
                self.personal_ores_quant[self.loot_list[i][0]] = OrderedDict()

            self.personal_ores_quant[self.loot_list[i][0]][self.loot_list[i][2]] = 0

            if self.loot_list[i][0] in self.personal_data:
                pass
            else:
                self.personal_data[self.loot_list[i][0]] = OrderedDict()

            self.personal_data[self.loot_list[i][0]][self.loot_list[i][2]] = OrderedDict()

        #プレイヤー、鉱石毎の値段を足し合わせる
        for i in range(len(self.loot_list)):
            self.personal_balances[self.loot_list[i][0]] += round( self.settings.all_ore_price[self.loot_list[i][2]] * self.loot_list[i][1] * self.buy_coefficient * self.efficiency)

            self.ore_balances[self.loot_list[i][2]] += round( self.settings.all_ore_price[self.loot_list[i][2]] * self.loot_list[i][1] *  self.buy_coefficient * self.efficiency)

            self.personal_ores[self.loot_list[i][0]][self.loot_list[i][2]] += round(self.settings.all_ore_price[self.loot_list[i][2]] * self.loot_list[i][1] * self.buy_coefficient * self.efficiency)

            self.personal_ores_quant[self.loot_list[i][0]][self.loot_list[i][2]] +=  self.loot_list[i][1]

            self.total_balance += round( self.settings.all_ore_price[self.loot_list[i][2]] * self.loot_list[i][1] *  self.buy_coefficient * self.efficiency)

        for i in self.personal_balances:
            self.personal_balances_ratio[i] = self.personal_balances[i] / self.total_balance * self.buy_coefficient

        for i in self.personal_ores.keys():
            for j in self.personal_ores[i].keys():
                self.personal_data[i][j][self.personal_ores_quant[i][j]] = self.personal_ores[i][j]
            else:
                self.personal_data[i]['total'] = self.personal_balances[i]
                self.personal_data[i]['tax'] = round(self.personal_balances[i] * self.fuel_tax)
                self.personal_data[i]['pay'] = round(self.personal_data[i]['total'] - self.personal_data[i]['tax'])



        all_prices = [self.personal_balances,self.ore_balances,self.personal_balances_ratio,self.personal_ores,self.personal_ores_quant, self.personal_data, self.total_balance]
        return all_prices
