from django.shortcuts import render
import sys,os
sys.path.append(os.path.dirname(__file__))
# Create your views here.

from scripts2.organize import Datamanage
from calculater.scripts.setting import InitOrePrice
from scripts2.calculater import BalanceCalculate

def contracts(request):
    return render(request, 'contracts.html')

def contracts_result(request):
    if request.method == 'GET':
          list = 'GET'
          return render(request, 'calculate_result.html',list)

    elif request.method == 'POST':
        contract = request.POST['Ore_contract']
        buy_coefficient = request.POST['jita_buy']

        data_organize = Datamanage(contract)
        contract_list = data_organize.ContractTrim()
        data_calculate = BalanceCalculate(contract_list,buy_coefficient)
        contract_list = data_calculate.balances()

        dict = {
            'indi':contract_list[0],
            'total':contract_list[1]
        }

        return render(request,'contracts_result.html',dict)
