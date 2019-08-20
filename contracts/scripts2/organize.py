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
            buffer1 = raw_contract[i].split("\t")
            buffer2 = buffer1[0].split(" ")
            if buffer2[0] == "Compressed":
                while len(buffer2) != 2:
                    buffer2[1] = buffer2[1] + " " + buffer2[2]
                    del buffer2[2]
                    buffer2[1] = buffer2[1].replace('*','')
            else:
                while len(buffer2) != 1:
                    buffer2[0] = buffer2[0] + " " + buffer2[1]
                    del buffer2[1]
                    buffer2[0] = buffer2[0].replace('*','')
            if buffer2[0] == "Compressed":
                if buffer2[1] in self.ices:
                    pass
                else:
                    buffer1[1] = int(buffer1[1]) * 100
                del buffer2[0]
            else:
                pass

            buffer3 = [buffer2[0],buffer1[1]]
            Contract_info.append(buffer3)


        return Contract_info
