#!/usr/bin/python
#coding=utf8

import ystockquote

#获取该股票所有信息
print ystockquote.get_all('GOOG')

#获取当前股价
print ystockquote.get_ask_realtime('GOOG')

#获取2012.11.22到2013.10.1历史报价
print ystockquote.get_historical_prices("GOOG",'2012.11.22','2013.10.1')
