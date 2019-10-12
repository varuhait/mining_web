#スプレッドシートAPI
import sys
sys.path.append('/path/to/gspread')
import gspread
import json
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
json_file = 'JitaMarketer.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '1abefJQAXC9yEfC_10B9oUenf0HCulacVeK4LhsyE-5Q'

#共有設定したスプレッドシートのシート1を開く
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

#A1セルの値を受け取る
import_value = worksheet.acell('D6').value
#各種手動入力データ
efficiency = 0.85
#jita_buy 鉱石価格
class InitOrePrice:
    #ミネラル,月資源価格の初期設定
    testa = import_value
    materials = {
    #月じゃない
    'Tritanium' : 4.2,
    'Pyerite' : 2,
    'Mexallon' : 46.95,
    'Isogen' : 4.7,
    'Nocxium' : 227,
    'Zydrine' : 388.5,
    'Megacyte' : 328.5,
    'Morphite' : 14000,

    #月
    'Atmostpheric Gases' : 137.93,
    'Evaporite Deposits' : 2198.95,
    'Hydrocarbons' : 190.97,
    'Silicates' : 2184.92,
    'Cobalt' : 2068.95,
    'Scandium' : 3196.95,
    'Titanium' : 4397.97,
    'Tungsten' : 8898.85,
    'Cadmium' : 12500.01,
    'Vanadium' : 8746.96,
    'Chromium' : 14769.97,
    'Platinum' : 14999.97,
    'Caesium' : 12999.97,
    'Technetium' : 18477.93,
    'Hafnium' : 17844.93,
    'Mercury' : 9908.06,
    'Promethium' : 95634.00,
    'Dysprosium' : 91799.00,
    'Neodymium' : 90798.68,
    'Thulium' : 43997.45,

    #アイス精製物
    'Heavy Water' : 150,
    'Helium Isotopes': 560,
    'Hydrogen Isotopes': 580,
    'Liquid Ozone': 0,
    'Nitrogen Isotopes': 516,
    'Oxygen Isotopes': 585,
    'Strontium Clathrates': 850,
    }

    standard_ore_price = {
    #月じゃない
    'Arkonor':float(worksheet.acell('L2').value.replace(',',''))/100,
    'Omber':float(worksheet.acell('L3').value.replace(',',''))/100,
    'Crokite':float(worksheet.acell('L4').value.replace(',',''))/100,
    'Kernite':float(worksheet.acell('L5').value.replace(',',''))/100,
    'Jaspet':float(worksheet.acell('L6').value.replace(',',''))/100,
    'Scordite':float(worksheet.acell('L7').value.replace(',',''))/100,
    'Spodumain':float(worksheet.acell('L8').value.replace(',',''))/100,
    'Dark Ochre':float(worksheet.acell('L9').value.replace(',',''))/100,
    'Gneiss':float(worksheet.acell('L10').value.replace(',',''))/100,
    'Pyroxeres':float(worksheet.acell('L11').value.replace(',',''))/100,
    'Bistot':float(worksheet.acell('L12').value.replace(',',''))/100,
    'Plagioclase':float(worksheet.acell('L13').value.replace(',',''))/100,
    'Hedbergite':float(worksheet.acell('L14').value.replace(',',''))/100,
    'Hemorphite':float(worksheet.acell('L15').value.replace(',',''))/100,
    'Veldspar':float(worksheet.acell('L16').value.replace(',',''))/100,
    'Mercoxit':float(worksheet.acell('L17').value.replace(',',''))/100,

    #月
    'Bitumens' : (materials['Tritanium']*6000 + materials['Pyerite']*6000 + materials['Mexallon']*400 + materials['Hydrocarbons']*65) /100 *efficiency,

    'Carnotite' : (materials['Mexallon']*1000 + materials['Isogen']*1250 + materials['Zydrine']*50 + materials['Atmostpheric Gases']*15 + materials['Cobalt']*10 + materials['Technetium']*50) /100 *efficiency,

    'Chromite' : (materials['Pyerite']*5000 + materials['Mexallon']*1250 + materials['Isogen']*750 + materials['Nocxium']*50 + materials['Hydrocarbons']*10 + materials['Chromium']*40) /100 *efficiency,

    'Cinnabar' : (materials['Mexallon']*1500 + materials['Isogen']*750 + materials['Megacyte']*50 + materials['Mercury']*50 + materials['Tungsten']*10 + materials['Evaporite Deposits']*15) /100 *efficiency,

    'Cobaltite' : (materials['Tritanium']*7500 + materials['Pyerite']*10000 + materials['Mexallon']*500 + materials['Cobalt']*40) /100 *efficiency,

    'Coesite' : (materials['Tritanium']*10000 + materials['Pyerite']*2000 + materials['Mexallon']*400 + materials['Silicates']*65) /100 *efficiency,

    'Euxenite' : (materials['Tritanium']*10000 + materials['Pyerite']*7500 + materials['Mexallon']*500 + materials['Scandium']*40) /100 *efficiency,

    'Loparite' : (materials['Nocxium']*100 + materials['Zydrine']*200 + materials['Megacyte']*50 + materials['Promethium']*22 +materials['Platinum']*10 + materials['Scandium']*20 + materials['Hydrocarbons']*20) /100 *efficiency,

    'Monazite' : (materials['Nocxium']*50 + materials['Zydrine']*150 + materials['Megacyte']*150 + materials['Neodymium']*22 + materials['Chromium']*10 + materials['Tungsten']*20 + materials['Evaporite Deposits']*20) /100 *efficiency,

    'Otavite' : (materials['Tritanium']*5000 + materials['Mexallon']*1500 + materials['Isogen']*500 + materials['Nocxium']*50) /100 *efficiency,

    'Pollucite' : (materials['Mexallon']*1250 + materials['Isogen']*1000 + materials['Zydrine']*50 + materials['Caesium']*50 + materials['Scandium']*10 + materials['Hydrocarbons']*15) /100 *efficiency,

    'Scheelite' : (materials['Tritanium']*12500 + materials['Pyerite']*5000 + materials['Mexallon']*500 + materials['Tungsten']*40) /100 *efficiency,

    'Sperrylite' : (materials['Tritanium']*5000 + materials['Mexallon']*1000 + materials['Isogen']*1000 + materials['Zydrine']*50 + materials['Platinum']*40 + materials['Evaporite Deposits']*10) /100 *efficiency,

    'Sylvite' : (materials['Tritanium']*8000 + materials['Pyerite']*4000 + materials['Mexallon']*400 + materials['Evaporite Deposits']*65) /100 *efficiency,

    'Titanite' : (materials['Tritanium']*15000 + materials['Pyerite']*2500 + materials['Mexallon']*500 + materials['Titanium']*40) /100 *efficiency,

    'Vanadinite' : (materials['Pyerite']*5000 + materials['Mexallon']*750 + materials['Isogen']*1250 + materials['Zydrine']*50 + materials['Vanadium']*40 + materials['Silicates']*10) /100 *efficiency,

    'Xenotime' : (materials['Nocxium']*50 + materials['Zydrine']*100 + materials['Megacyte']*200 + materials['Dysprosium']*22 + materials['Vanadium']*10 + materials['Cobalt']*20 + materials['Atmostpheric Gases']*20) /100 *efficiency,

    'Ytterbite' : (materials['Nocxium']*200 + materials['Zydrine']*100 + materials['Megacyte']*50 + materials['Thulium']*22 + materials['Cadmium']*10 + materials['Titanium']*20 + materials['Silicates']*20) /100 *efficiency,

    'Zeolites' : (materials['Tritanium']*4000 + materials['Pyerite']*8000 + materials['Mexallon']*400 + materials['Atmostpheric Gases']*65) /100 *efficiency,

    'Zircon' : (materials['Mexallon']*1750 + materials['Isogen']*500 + materials['Megacyte']*50 + materials['Hafnium']*50 + materials['Titanium']*10 + materials['Silicates']*15) /100 *efficiency,

    #アイス
    'Blue Ice':float(worksheet.acell('L19').value.replace(',','')),
    'Clear Icicle':float(worksheet.acell('L20').value.replace(',','')),
    'Dark Glitter':float(worksheet.acell('L21').value.replace(',','')),
    'Enriched Clear Icicle':float(worksheet.acell('L22').value.replace(',','')),
    'Gelidus':float(worksheet.acell('L23').value.replace(',','')),
    'Glacial Mass':float(worksheet.acell('L24').value.replace(',','')),
    'Glare Crust':float(worksheet.acell('L25').value.replace(',','')),
    'Krystallos':float(worksheet.acell('L26').value.replace(',','')),
    'Pristine White Glaze':float(worksheet.acell('L27').value.replace(',','')),
    'Smooth Glacial Mass':float(worksheet.acell('L28').value.replace(',','')),
    'Thick Blue Ice':float(worksheet.acell('L29').value.replace(',','')),
    'White Glaze':float(worksheet.acell('L30').value.replace(',','')),
    }

    standard_ore_price_old = {
    #月じゃない
    'Arkonor': (materials['Tritanium']*22000 + materials['Mexallon']*2500 + materials['Megacyte']*320) /100 *efficiency,

    'Bistot': (materials['Pyerite']*12000 + materials['Zydrine']*450 + materials['Megacyte']*100) /100 *efficiency,

    'Crokite': (materials['Tritanium']*21000 + materials['Nocxium']*760 + materials['Zydrine']*135) /100 *efficiency,

    'Dark Ochre': (materials['Tritanium']*10000 + materials['Isogen']*1600 + materials['Nocxium']*120) /100 *efficiency,

    'Gneiss' : (materials['Pyerite']*2200 + materials['Mexallon']*2400 + materials['Isogen']*300) /100 *efficiency,

    'Hedbergite' : (materials['Pyerite']*1000 + materials['Isogen']*200 + materials['Nocxium']*100 + materials['Zydrine']*19) /100 *efficiency,

    'Hemorphite' : (materials['Tritanium']*2200 + materials['Isogen']*100 + materials['Nocxium']*120 + materials['Zydrine']*15) /100 *efficiency,

    'Jaspet' : (materials['Mexallon']*350 + materials['Nocxium']*75 + materials['Zydrine']*8) /100 *efficiency,

    'Kernite' : (materials['Tritanium']*134 + materials['Mexallon']*267 + materials['Isogen']*134)/100 *efficiency,

    'Mercoxit' : materials['Morphite']*300 /100 *efficiency,

    'Omber' : (materials['Tritanium']*800 + materials['Pyerite']*100 + materials['Isogen']*85) /100 *efficiency,

    'Plagioclase' : (materials['Tritanium']*107 + materials['Pyerite']*213 + materials['Mexallon']*107) /100 *efficiency,

    'Pyroxeres' : (materials['Tritanium']*351 + materials['Pyerite']*25 + materials['Mexallon']*50 + materials['Nocxium']*5) /100 *efficiency,

    'Scordite' : (materials['Tritanium']*346 + materials['Pyerite']*173) /100 *efficiency,

    'Spodumain' : (materials['Tritanium']*56000 + materials['Pyerite']*12050 + materials['Mexallon']*2100 + materials['Isogen']*450) /100 *efficiency,

    'Veldspar' : materials['Tritanium']*415 /100 *efficiency,
    #月
    'Bitumens' : (materials['Tritanium']*6000 + materials['Pyerite']*6000 + materials['Mexallon']*400 + materials['Hydrocarbons']*65) /100 *efficiency,

    'Carnotite' : (materials['Mexallon']*1000 + materials['Isogen']*1250 + materials['Zydrine']*50 + materials['Atmostpheric Gases']*15 + materials['Cobalt']*10 + materials['Technetium']*50) /100 *efficiency,

    'Chromite' : (materials['Pyerite']*5000 + materials['Mexallon']*1250 + materials['Isogen']*750 + materials['Nocxium']*50 + materials['Hydrocarbons']*10 + materials['Chromium']*40) /100 *efficiency,

    'Cinnabar' : (materials['Mexallon']*1500 + materials['Isogen']*750 + materials['Megacyte']*50 + materials['Mercury']*50 + materials['Tungsten']*10 + materials['Evaporite Deposits']*15) /100 *efficiency,

    'Cobaltite' : (materials['Tritanium']*7500 + materials['Pyerite']*10000 + materials['Mexallon']*500 + materials['Cobalt']*40) /100 *efficiency,

    'Coesite' : (materials['Tritanium']*10000 + materials['Pyerite']*2000 + materials['Mexallon']*400 + materials['Silicates']*65) /100 *efficiency,

    'Euxenite' : (materials['Tritanium']*10000 + materials['Pyerite']*7500 + materials['Mexallon']*500 + materials['Scandium']*40) /100 *efficiency,

    'Loparite' : (materials['Nocxium']*100 + materials['Zydrine']*200 + materials['Megacyte']*50 + materials['Promethium']*22 +materials['Platinum']*10 + materials['Scandium']*20 + materials['Hydrocarbons']*20) /100 *efficiency,

    'Monazite' : (materials['Nocxium']*50 + materials['Zydrine']*150 + materials['Megacyte']*150 + materials['Neodymium']*22 + materials['Chromium']*10 + materials['Tungsten']*20 + materials['Evaporite Deposits']*20) /100 *efficiency,

    'Otavite' : (materials['Tritanium']*5000 + materials['Mexallon']*1500 + materials['Isogen']*500 + materials['Nocxium']*50) /100 *efficiency,

    'Pollucite' : (materials['Mexallon']*1250 + materials['Isogen']*1000 + materials['Zydrine']*50 + materials['Caesium']*50 + materials['Scandium']*10 + materials['Hydrocarbons']*15) /100 *efficiency,

    'Scheelite' : (materials['Tritanium']*12500 + materials['Pyerite']*5000 + materials['Mexallon']*500 + materials['Tungsten']*40) /100 *efficiency,

    'Sperrylite' : (materials['Tritanium']*5000 + materials['Mexallon']*1000 + materials['Isogen']*1000 + materials['Zydrine']*50 + materials['Platinum']*40 + materials['Evaporite Deposits']*10) /100 *efficiency,

    'Sylvite' : (materials['Tritanium']*8000 + materials['Pyerite']*4000 + materials['Mexallon']*400 + materials['Evaporite Deposits']*65) /100 *efficiency,

    'Titanite' : (materials['Tritanium']*15000 + materials['Pyerite']*2500 + materials['Mexallon']*500 + materials['Titanium']*40) /100 *efficiency,

    'Vanadinite' : (materials['Pyerite']*5000 + materials['Mexallon']*750 + materials['Isogen']*1250 + materials['Zydrine']*50 + materials['Vanadium']*40 + materials['Silicates']*10) /100 *efficiency,

    'Xenotime' : (materials['Nocxium']*50 + materials['Zydrine']*100 + materials['Megacyte']*200 + materials['Dysprosium']*22 + materials['Vanadium']*10 + materials['Cobalt']*20 + materials['Atmostpheric Gases']*20) /100 *efficiency,

    'Ytterbite' : (materials['Nocxium']*200 + materials['Zydrine']*100 + materials['Megacyte']*50 + materials['Thulium']*22 + materials['Cadmium']*10 + materials['Titanium']*20 + materials['Silicates']*20) /100 *efficiency,

    'Zeolites' : (materials['Tritanium']*4000 + materials['Pyerite']*8000 + materials['Mexallon']*400 + materials['Atmostpheric Gases']*65) /100 *efficiency,

    'Zircon' : (materials['Mexallon']*1750 + materials['Isogen']*500 + materials['Megacyte']*50 + materials['Hafnium']*50 + materials['Titanium']*10 + materials['Silicates']*15) /100 *efficiency,

    #アイス
    'Clear Icicle': (materials['Heavy Water']*69 + materials['Liquid Ozone']*35 + materials['Helium Isotopes']*414 + materials['Strontium Clathrates']*1) *efficiency,

    'Glacial Mass': (materials['Heavy Water']*69 + materials['Liquid Ozone']*35 + materials['Hydrogen Isotopes']*414 + materials['Strontium Clathrates']*1) *efficiency,

    'Blue Ice': (materials['Heavy Water']*69 + materials['Liquid Ozone']*35 + materials['Oxygen Isotopes']*414 + materials['Strontium Clathrates']*1) *efficiency,

    'White Glaze': (materials['Heavy Water']*69 + materials['Liquid Ozone']*35 + materials['Nitrogen Isotopes']*414 + materials['Strontium Clathrates']*1) *efficiency,

    'Glare Crust': (materials['Heavy Water']*1381 + materials['Liquid Ozone']*691 + materials['Strontium Clathrates']*35) *efficiency,

    'Dark Glitter': (materials['Heavy Water']*691 + materials['Liquid Ozone']*1381 + materials['Strontium Clathrates']*69) *efficiency,

    'Gelidus': (materials['Heavy Water']*345 + materials['Liquid Ozone']*691 + materials['Strontium Clathrates']*104) *efficiency,

    'Krystallos': (materials['Heavy Water']*173 + materials['Liquid Ozone']*691 + materials['Strontium Clathrates']*173) *efficiency,

    'Thick Blue Ice': (materials['Heavy Water']*104 + materials['Liquid Ozone']*55 + materials['Strontium Clathrates']*1 + materials['Oxygen Isotopes']*483) *efficiency,

    'Pristine White Glaze': (materials['Heavy Water']*104 + materials['Liquid Ozone']*55 + materials['Strontium Clathrates']*1 + materials['Nitrogen Isotopes']*483) *efficiency,

    'Smooth Glacial Mass': (materials['Heavy Water']*104 + materials['Liquid Ozone']*55 + materials['Strontium Clathrates']*1 + materials['Hydrogen Isotopes']*483) *efficiency,

    'Enriched Clear Icicle': (materials['Heavy Water']*104 + materials['Liquid Ozone']*55 + materials['Strontium Clathrates']*1 + materials['Helium Isotopes']*483) *efficiency,
    }

    all_ore_price = {
    #月じゃない
    'Arkonor' : standard_ore_price['Arkonor'],
    'Crimson Arkonor' : standard_ore_price['Arkonor']*1.05,
    'Prime Arkonor' : standard_ore_price['Arkonor']*1.10,
    'Flawless Arkonor' : standard_ore_price['Arkonor']*1.15,

    'Bistot' : standard_ore_price['Bistot'],
    'Triclinic Bistot' : standard_ore_price['Bistot']*1.05,
    'Monoclinic Bistot' : standard_ore_price['Bistot']*1.10,
    'Cubic Bistot' : standard_ore_price['Bistot']*1.15,

    'Crokite' : standard_ore_price['Crokite'],
    'Sharp Crokite' : standard_ore_price['Crokite']*1.05,
    'Crystaline Crokite' : standard_ore_price['Crokite']*1.10,
    'Pellucid Crokite' : standard_ore_price['Crokite']*1.15,

    'Dark Ochre' : standard_ore_price['Dark Ochre'],
    'Onyx Ochre' : standard_ore_price['Dark Ochre']*1.05,
    'Obsidian Ochre' : standard_ore_price['Dark Ochre']*1.10,
    'Jet Ochre' : standard_ore_price['Dark Ochre']*1.15,

    'Gneiss' : standard_ore_price['Gneiss'],
    'Iridescent Gneiss' : standard_ore_price['Gneiss']*1.05,
    'Prismatic Gneiss' : standard_ore_price['Gneiss']*1.10,
    'Brilliant Gneiss' : standard_ore_price['Gneiss']*1.15,

    'Hedbergite' : standard_ore_price['Hedbergite'],
    'Virtric Hedbergite' : standard_ore_price['Hedbergite']*1.05,
    'Glazed Hedbergite' : standard_ore_price['Hedbergite']*1.10,
    'Lustrous Hedbergite' : standard_ore_price['Hedbergite']*1.15,

    'Hemorphite' : standard_ore_price['Hemorphite'],
    'Vivid Hemorphite' : standard_ore_price['Hemorphite']*1.05,
    'Radiant Hemorphite' : standard_ore_price['Hemorphite']*1.10,
    'Scintillating Hemorphite' : standard_ore_price['Hemorphite']*1.15,

    'Jaspet' : standard_ore_price['Jaspet'],
    'Pure Jaspet' : standard_ore_price['Jaspet']*1.05,
    'Pristine Jaspet' : standard_ore_price['Jaspet']*1.10,
    'Immaculate Jaspet' : standard_ore_price['Jaspet']*1.15,

    'Kernite' : standard_ore_price['Kernite'],
    'Luminous Kernite' : standard_ore_price['Kernite']*1.05,
    'Fiery Kernite' : standard_ore_price['Kernite']*1.10,
    'Resplendant Kernite' : standard_ore_price['Kernite']*1.15,

    'Mercoxit' : standard_ore_price['Mercoxit'],
    'Magma Mercoxit' : standard_ore_price['Mercoxit']*1.05,
    'Vitreous Mercoxit' : standard_ore_price['Mercoxit']*1.10,

    'Omber' : standard_ore_price['Omber'],
    'Silvery Omber' : standard_ore_price['Omber']*1.05,
    'Golden Omber' : standard_ore_price['Omber']*1.10,
    'Platinoid Omber' : standard_ore_price['Omber']*1.15,

    'Plagioclase' : standard_ore_price['Plagioclase'],
    'Azure Plagioclase' : standard_ore_price['Plagioclase']*1.05,
    'Rich Plagioclase' : standard_ore_price['Plagioclase']*1.10,
    'Sparkling Plagioclase' : standard_ore_price['Plagioclase']*1.15,

    'Pyroxeres' : standard_ore_price['Pyroxeres'],
    'Solid Pyroxeres' : standard_ore_price['Pyroxeres']*1.05,
    'Viscous Pyroxeres' : standard_ore_price['Pyroxeres']*1.10,
    'Opulent Pyroxeres' : standard_ore_price['Pyroxeres']*1.15,

    'Scordite' : standard_ore_price['Scordite'],
    'Condensed Scordite' : standard_ore_price['Scordite']*1.05,
    'Massive Scordite' : standard_ore_price['Scordite']*1.10,
    'Glossy Scordite' : standard_ore_price['Scordite']*1.15,

    'Spodumain' : standard_ore_price['Spodumain'],
    'Bright Spodumain' : standard_ore_price['Spodumain']*1.05,
    'Gleaming Spodumain' : standard_ore_price['Spodumain']*1.10,
    'Dazzling Spodumain' : standard_ore_price['Spodumain']*1.15,

    'Veldspar' : standard_ore_price['Veldspar'],
    'Concentrated Veldspar' : standard_ore_price['Veldspar']*1.05,
    'Dense Veldspar' : standard_ore_price['Veldspar']*1.10,
    'Stable Veldspar' : standard_ore_price['Veldspar']*1.15,

    #月
    'Bitumens' : standard_ore_price['Bitumens'],
    'Brimful Bitumens' : standard_ore_price['Bitumens']*1.15,
    'Glistening Bitumens' : standard_ore_price['Bitumens']*2.00,

    'Carnotite' : standard_ore_price['Carnotite'],
    'Replete Carnotite' : standard_ore_price['Carnotite']*1.15,
    'Glowing Carnotite' : standard_ore_price['Carnotite']*2.00,

    'Chromite' : standard_ore_price['Chromite'],
    'Lavish Chromite' : standard_ore_price['Chromite']*1.15,
    'Shirmmering Chromite' : standard_ore_price['Chromite']*2.00,

    'Cinnabar' : standard_ore_price['Cinnabar'],
    'Replate Cinnabar' : standard_ore_price['Cinnabar']*1.15,
    'Glistening Cinnabar' : standard_ore_price['Cinnabar']*2.00,

    'Cobaltite' : standard_ore_price['Cobaltite'],
    'Copious Cobaltite' : standard_ore_price['Cobaltite']*1.15,
    'Twinkling Cobaltite' : standard_ore_price['Cobaltite']*2.00,

    'Coesite' : standard_ore_price['Coesite'],
    'Brimful Coesite' : standard_ore_price['Coesite']*1.15,
    'Glistening Coesite' : standard_ore_price['Coesite']*2.00,

    'Euxenite' : standard_ore_price['Euxenite'],
    'Copious Euxenite' : standard_ore_price['Euxenite']*1.15,
    'Twinkling Euxenite' : standard_ore_price['Euxenite']*2.00,

    'Loparite' : standard_ore_price['Loparite'],
    'Bountiful Loparite' : standard_ore_price['Loparite']*1.15,
    'Shining Loparite' : standard_ore_price['Loparite']*2.00,

    'Monazite' : standard_ore_price['Monazite'],
    'Bountiful Monazite' : standard_ore_price['Monazite']*1.15,
    'Shining Monazite' : standard_ore_price['Monazite']*2.00,

    'Otavite' : standard_ore_price['Otavite'],
    'Lavish Otavite' : standard_ore_price['Otavite']*1.15,
    'Shimmering Otavite' : standard_ore_price['Otavite']*2.00,

    'Pollucite' : standard_ore_price['Pollucite'],
    'Replate Pollucite' : standard_ore_price['Pollucite']*1.15,
    'Glowing Pollucite' : standard_ore_price['Pollucite']*2.00,

    'Scheelite' : standard_ore_price['Scheelite'],
    'Copious Scheelite' : standard_ore_price['Scheelite']*1.15,
    'Twinkling Scheelite' : standard_ore_price['Scheelite']*2.00,

    'Sperrylite' : standard_ore_price['Sperrylite'],
    'Lavish Sperrylite' : standard_ore_price['Sperrylite']*1.15,
    'Shimmering Sperrylite' : standard_ore_price['Sperrylite']*2.00,

    'Sylvite' : standard_ore_price['Sylvite'],
    'Brimful Sylvite' : standard_ore_price['Sylvite']*1.15,
    'Glistening Sylvite' : standard_ore_price['Sylvite']*2.00,

    'Titanite' : standard_ore_price['Titanite'],
    'Copious Titanite' : standard_ore_price['Titanite']*1.15,
    'Twinkling Titanite' : standard_ore_price['Titanite']*2.00,

    'Vanadinite' : standard_ore_price['Vanadinite'],
    'Lavish Vanadinite' : standard_ore_price['Vanadinite']*1.15,
    'Shimmering Vanadinite' : standard_ore_price['Vanadinite']*2.00,

    'Xenotime' : standard_ore_price['Xenotime'],
    'Bountiful Xenotime' : standard_ore_price['Xenotime']*1.15,
    'Shining Xenotime' : standard_ore_price['Xenotime']*2.00,

    'Ytterbite' : standard_ore_price['Ytterbite'],
    'Bountiful Ytterbite' : standard_ore_price['Ytterbite']*1.15,
    'Shining Ytterbite' : standard_ore_price['Ytterbite']*2.00,

    'Zeolites' : standard_ore_price['Zeolites'],
    'Brimful Zeolites' : standard_ore_price['Zeolites']*1.15,
    'Glistening Zeolites' : standard_ore_price['Zeolites']*2.00,

    'Zircon' : standard_ore_price['Zircon'],
    'Replate Zircon' : standard_ore_price['Zircon']*1.15,
    'Glowing Zircon' : standard_ore_price['Zircon']*2.00,

    #アイス
    'Clear Icicle': standard_ore_price['Clear Icicle'],
    'Glacial Mass': standard_ore_price['Glacial Mass'],
    'Blue Ice': standard_ore_price['Blue Ice'],
    'White Glaze': standard_ore_price['White Glaze'],
    'Glare Crust': standard_ore_price['Glare Crust'],
    'Dark Glitter': standard_ore_price['Dark Glitter'],
    'Gelidus': standard_ore_price['Gelidus'],
    'Krystallos': standard_ore_price['Krystallos'],
    'Thick Blue Ice': standard_ore_price['Thick Blue Ice'],
    'Pristine White Glaze': standard_ore_price['Pristine White Glaze'],
    'Smooth Glacial Mass': standard_ore_price['Smooth Glacial Mass'],
    'Enriched Clear Icicle': standard_ore_price['Enriched Clear Icicle'],
    }

    ices = [
        'Clear Icicle',
        'Glacial Mass',
        'Blue Ice',
        'White Glaze',
        'Glare Crust',
        'Dark Glitter',
        'Gelidus',
        'Krystallos',
        'Thick Blue Ice',
        'Pristine White Glaze',
        'Smooth Glacial Mass',
        'Enriched Clear Icicle',
    ]
