print('введите время в секундах, до 86400')
time=int(input())
if time < 86401:
    h=time//3600 
    min=(time-h*3600)//60
    sec=(time-h*3600)-(min*60)
    print(h,' ',min,' ',sec )
else:
    print('wrong number')
    print("(h+min+sec)*0")