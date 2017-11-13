import ssl
import json
import sys, os
import logging
from time import sleep
from urllib.request import Request, urlopen

def get_info_from_web(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        info = json.loads(urlopen(req).read().decode('utf-8'))
    except:
        info = "error"
    return info
def get_profits(url):
    info = get_info_from_web(url)
    if info == 'error':
        return 0
    else:
        decode_Json(info)
def decode_Json(info):
    print(info['coins']['Ethereum']['btc_revenue24'])
    print(info['coins']['Zcash']['btc_revenue24'])
    print(info['coins']['EthereumClassic']['btc_revenue24'])
    print(info['coins']['Monero']['btc_revenue24'])
if __name__ == '__main__':
    get_profits('https://whattomine.com/coins.json?utf8=%E2%9C%93&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=3&adapt_q_570=0&adapt_q_580=0&adapt_q_750Ti=0&adapt_q_1050Ti=0&adapt_q_10606=0&adapt_q_1070=0&adapt_q_1080=5&adapt_q_1080Ti=7&adapt_1080Ti=true&eth=true&factor%5Beth_hr%5D=245.0&factor%5Beth_p%5D=980.0&grof=true&factor%5Bgro_hr%5D=406.0&factor%5Bgro_p%5D=1470.0&x11gf=true&factor%5Bx11g_hr%5D=136.5&factor%5Bx11g_p%5D=1190.0&cn=true&factor%5Bcn_hr%5D=5810.0&factor%5Bcn_p%5D=980.0&eq=true&factor%5Beq_hr%5D=4795.0&factor%5Beq_p%5D=1330.0&lre=true&factor%5Blrev2_hr%5D=448000.0&factor%5Blrev2_p%5D=1330.0&ns=true&factor%5Bns_hr%5D=9800.0&factor%5Bns_p%5D=1330.0&lbry=true&factor%5Blbry_hr%5D=3220.0&factor%5Blbry_p%5D=1330.0&bk2bf=true&factor%5Bbk2b_hr%5D=19600.0&factor%5Bbk2b_p%5D=1330.0&bk14=true&factor%5Bbk14_hr%5D=30450.0&factor%5Bbk14_p%5D=1470.0&pas=true&factor%5Bpas_hr%5D=11900.0&factor%5Bpas_p%5D=1470.0&skh=true&factor%5Bskh_hr%5D=332.5&factor%5Bskh_p%5D=1330.0&factor%5Bl2z_hr%5D=420.0&factor%5Bl2z_p%5D=300.0&factor%5Bcost%5D=0.1&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=bleutrade&factor%5Bexchanges%5D%5B%5D=c_cex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate')