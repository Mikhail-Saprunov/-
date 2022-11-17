per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = [5600, 5900, 4280, 4000]
a = (round(money*per_cent['ТКБ']//100))
b = (round(money*per_cent['СКБ']//100))
c = (round(money*per_cent['ВТБ']//100))
d = (round(money*per_cent['СБЕР']//100))
s = [a,b,c,d]
print ('Возможный заработок',[a,b,c,d])
print ('Максимальная сумма, которую вы можете заработать',(max(s)))