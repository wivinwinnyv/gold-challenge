import random
import time
import pyqrcode
import png
from pyqrcode import QRCode
c_data=(32.76,30.76)
u_data=(3140,3040,0)
flag=(1,2)
def start_test():
    print("performing magnetic test...")
    time.sleep(2)
    choice=random.choice(list(flag))
    if choice==1:
        print("magnetic test success!!")
        ultra_sound()
    else:
        print("magnetic test failed")
def ultra_sound():
    print("performing ultra sound test...")
    time.sleep(2)
    value=random.choice(list(u_data))
    if value<=3150 and value>=3130:
        karat="22K"
        print("ultra sound test success!! gold is "+karat+" carat")
        conductivity(karat)
    elif value<=3050 and value>=3030:
        karat = "18K"
        print("ultra sound test success!! gold is " + karat+" carat")
        conductivity(karat)
    else:
        print("ultra sound test failed!! gold below specified standards")
def conductivity(k):
    print("performing conductivity test...")
    time.sleep(2)
    value = random.choice(list(c_data))
    if value<=32.86 and value>=32.66:
        print("conductivity test success!! gold is "+k)
        issue_loan(k)
    elif value<=30.86 and value>=30.66:
        print("conductivity test success!! gold is " + k)
        issue_loan(k)
    else:
        print("conductivity test failed!! gold below specified standards")
def issue_loan(final):
    print("computing final gold rate per gram")
    time.sleep(2)
    if final=="22K":
        print("estimated gold amount per gram is 5775 per gram")
    elif final=="18K":
        print("estimated gold amount per gram is 4725 per gram")
def qrcode():
    s = "https://www.federalbank.co.in/gold-loans"
    url = pyqrcode.create(s)
    url.svg("myqr.svg", scale=8)
    url.png('myqr.png', scale=6)
name=input("enter user id : ")
password=input("enter password : ")
if name=="wivin" and password=="1234":
    print("generating qr code...")
    qrcode()
    time.sleep(2)
    print("starting test...")
    time.sleep(1)
    start_test()
