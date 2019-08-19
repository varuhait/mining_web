import scripts.setting as setting
from collections import OrderedDict

class Datamanage:
    def __init__(self,contract):
        self.ore_list = contract
        self.ore_prices = setting.InitOrePrice()
        self.ices = self.ore_prices.ices

    #contract 整理
    def ContractTrim(self):
        #リストへの整理
        Contract_info = []
        raw_contract = self.ore_list
        raw_contract = raw_contract.split("\r\n")
        for i in range(len(raw_contract)):
            Contract_info.append(raw_contract[i].split("*"))
            del Contract_info[i][-1]
            del Contract_info[i][-1]
            buffer = Contract_info[i][-1].split('\t')
            del Contract_info[i][-1]
            Contract_info[i].append(buffer[1])

            buffer2 = Contract_info[i][0].split(" ")
            while len(buffer2) != 2:
                buffer2[1] = buffer2[1] + " " + buffer2[2]
                del buffer2[2]
            if buffer2[0] == "Compressed":
                Contract_info[i][0] = buffer2[1]
                if buffer2[1] in self.ices:
                    pass
                else:
                    Contract_info[i][1] = int(Contract_info[i][1]) * 100
            else:
                pass

        return Contract_info
