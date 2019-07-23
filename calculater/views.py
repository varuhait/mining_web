from django.shortcuts import render
import sys,os
sys.path.append(os.path.dirname(__file__))

from scripts.organize import Datamanage
from scripts.calculater import BalanceCalculate
from scripts.setting import InitOrePrice

# Create your views here.
def calculater(request):
    return render(request, 'calculater.html')

def home(request):
    return render(request, 'home.html')

def calculate_result(request):
    if request.method == 'GET':
          list = 'GET'
          return render(request, 'calculate_result.html',list)

    elif request.method == 'POST':

        loot = request.POST['loots']
        ignore = request.POST['ignores']
        buy_coefficient = float(request.POST['jita_buy'])/100
        fuel_tax = float(request.POST['fuel_tax'])/100
        admin = request.POST['administrator']

        data_organize = Datamanage(loot,ignore)
        loot_list = data_organize.LootTrim()
        ignore_list = data_organize.IgnoreTrim()
        Trimed_list = data_organize.ReflectIgnore(loot_list,ignore_list)

        calculate = BalanceCalculate(Trimed_list,buy_coefficient,fuel_tax)
        balance = calculate.balances()

        ore_prices = InitOrePrice()


        dict = {
            'personal': balance[0],
            'ore': balance[1],
            'ratio': balance[2],
            'p_ores': balance[3],
            'p_ores_q': balance[4],
            'datas' : balance[5],
            'total': balance[6],
            'admin': admin,
            'inits': ore_prices,
            'jita_buy': buy_coefficient*100,
            'ignores': ignore_list,
            'loots':loot_list,
            'Trimed':Trimed_list
        }

        return render(request, 'calculate_result.html',dict)
