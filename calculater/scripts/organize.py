import scripts.setting as setting
from collections import OrderedDict

class Datamanage:
    def __init__(self,loot,ignore):
        self.loot = loot
        self.ignore = ignore

    #Loot品整理
    #戦利品ウィンドウからコピペしたデータから余分な部分を削除する
    def LootTrim(self):
        #リストへの整理
        Loot_info = []
        raw_loot = self.loot
        raw_loot = raw_loot.split("\r\n")
        for i in range(len(raw_loot)):
            Loot_info.append(raw_loot[i].split(" "))
        while len(Loot_info[-1]) <= 1:
            del Loot_info[-1]

        #余分な要素を削除(及び取得アイテム数のint化)
        for i in range(len(Loot_info)):
            del Loot_info[i][0]
            del Loot_info[i][-1]
            while Loot_info[i][1] != "が":
                Loot_info[i][0] = Loot_info[i][0] + ' '+ Loot_info[i][1]
                del Loot_info[i][1]
            Loot_info[i].remove("が")
            Loot_info[i].remove("x")
            Loot_info[i][1] = int(Loot_info[i][1].replace(",",""))

        return Loot_info

    def IgnoreTrim(self):
        ignore_info = []
        raw_ignore = self.ignore
        raw_ignore = raw_ignore.split("\r\n")
        for i in range(len(raw_ignore)):
            ignore_info.append(raw_ignore[i].split(" "))

        return ignore_info

    #無視プレイヤーの反映、鉱石以外のアイテムの除去、鉱石、プレイヤー名の結合
    def ReflectIgnore(self,loot_list,ignore_list):
        number = []
        count = 0

        #無視プレイヤーの反映
        for i in range(len(ignore_list)):
            while len(ignore_list[i]) != 1:
                ignore_list[i][0] = ignore_list[i][0] + " " + ignore_list[i][1]
                del ignore_list[i][1]

        for i in range(len(loot_list)):
            for j in range(len(ignore_list)):
                if loot_list[i][0] == ignore_list[j][0]:
                    number.append(i)

        for i in number:
            del loot_list[i-count]
            count += 1

        #鉱石及びプレイヤー名の結合
        for i in range(len(loot_list)):
            loot_list[i][-1] = loot_list[i][-1].replace("*","")

            while len(loot_list[i]) != 3:
                loot_list[i][-1] = loot_list[i][-2] + " " + loot_list[i][-1]
                del loot_list[i][-2]

        #鉱石以外のアイテムを無視
        ore_prices = setting.InitOrePrice()
        count = 0
        for i in range(len(loot_list)):
            if not loot_list[i-count][-1] in ore_prices.all_ore_price:
                del loot_list[i-count]
                count += 1

        return loot_list
