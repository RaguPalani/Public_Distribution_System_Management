from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import DistrictSupplyOfficer
from .models import ProductPrice
from .models import ShopDetails
from .models import RationShopStocks
from .models import DistrictCollector
from .models import RationShopOfficer
# Create your views here.


#District Supply Officer
def register(request):
    if request.method == 'POST':
        member = DistrictSupplyOfficer(username=request.POST['username'], password=request.POST['password'],  idnumber=request.POST['userid'], designation=request.POST['designation'], district=request.POST['district'], phone=request.POST['phone'], mail=request.POST['mail'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'web/Register.html')

def login(request):
    return render(request, 'web/login.html')

def home(request):
    if request.method == 'POST':
        if DistrictSupplyOfficer.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = DistrictSupplyOfficer.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)
    return render(request,'web/home.html')
        
def addprice(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        price = request.POST['price']

        obj1 = ProductPrice()
        obj1.product_name = product_name
        obj1.price = price
        obj1.save()
        mydata=ProductPrice.objects.all()
        return render(request,'web/AddPrice.html',{'datas':mydata})
    return render(request,'web/AddPrice.html')

def pricelist(request):
    mydata=ProductPrice.objects.all()
    if(mydata!=''):
        return render(request,'web/PriceList.html',{'datas':mydata})
    else:
        return render(request,'web/PriceList.html')
    
def shopregister(request):
  
    if request.method == 'POST':
        shopno = request.POST['shop_number']
        district = request.POST['district']
        taluk = request.POST['taluk']
        location = request.POST['location']

        object_of_shop = ShopDetails()
        object_of_shop.shopno = shopno
        object_of_shop.district = district
        object_of_shop.taluk = taluk
        object_of_shop.location = location
        try:
            object_of_shop.save()
        except:
            context = {'msg': 'This Shop Details Already Registered '}
            return render(request, 'web/RationShops.html', context)        
        shopdata=ShopDetails.objects.all()
        return render(request,'web/RationShops.html',{'dataofshop':shopdata})
    return render(request,'web/RationShops.html')


def shoplist(request):
    shopdata=ShopDetails.objects.all()
    if(shopdata!=''):
        return render(request,'web/shoplist.html',{'dataofshop':shopdata})
    else:
        return render(request,'web/shoplist.html')

def shopstock(request):
    
    if request.method == 'POST':
            rationshop = request.POST['rationshop']
            date = request.POST['date']
            productname = request.POST['productname']
            quantity = request.POST['quantity']

            object_of_stock = RationShopStocks()
            object_of_stock.rationshop = rationshop
            object_of_stock.date = date
            object_of_stock.productname = productname
            object_of_stock.quantity = quantity
            try:
                object_of_stock.save()
            except:
                context = {'msg': 'This Details are Invalid!'}
                return render(request, 'web/stocklist.html', context)  
            stockdata=RationShopStocks.objects.all()
            if(stockdata!=''):
                return render(request,'web/stocklist.html',{'dataofstock':stockdata})
            else:
                return render(request,'web/stocklist.html')
            #return render(request,'web/stocklist.html',{'dataofstock':stockdata})
    return render(request,'web/stocklist.html')

def shopstocklist(request):
    stockdata=RationShopStocks.objects.all()
    if(stockdata!=''):
        return render(request,'district_collector/stock_list.html',{'dataofstock':stockdata})
    else:
        return render(request,'district_collector/stock_list.html')


def update_stock(request,id):
    stockdata = RationShopStocks.objects.get(id=id)

    return render(request,'web/updatestock.html',{'data':stockdata})
   
def update_price(request,id):
    pricedata = ProductPrice.objects.get(id=id)

    return render(request,'web/updateprice.html',{'data':pricedata})
    
#District Collector
def collector_register(request):
    if request.method == 'POST':
        member = DistrictCollector(collector_name=request.POST['collector_name'], password=request.POST['password'],  id_number=request.POST['userid'], district=request.POST['district'], phone=request.POST['phone'], mail=request.POST['mail'])
        member.save()
        return render(request,'district_collector/collector_login.html')
    else:
        return render(request, 'district_collector/collector_register.html')
    
def collector_login(request):
    if request.method == 'POST':
        collector_name = request.POST.get('collector_name')
        password = request.POST.get('password')
        try:
            user=DistrictCollector.objects.get(name = collector_name , password=password)
        except DistrictCollector.DoesNotExist:
            user = None
        if user is not None:
            return redirect('district_collector/collector_index.html')
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'district_collector/collector_login.html', context)
    return render(request,'district_collector/collector_login.html')

def collector_index(request):
    
    return render(request,'district_collector/index.html')

def collector_pricelist(request):
    mydata=ProductPrice.objects.all()
    if(mydata!=''):
        return render(request,'district_collector/price_list.html',{'datas':mydata})
    else:
        return render(request,'district_collector/price_list.html')
    
def collector_shoplist(request):
    shopdata=ShopDetails.objects.all()
    if(shopdata!=''):
        return render(request,'district_collector/shop_list.html',{'dataofshop':shopdata})
    else:
        return render(request,'district_collector/shop_list.html')
    
def collector_stocklist(request):
    stockdata=RationShopStocks.objects.all()
    if(stockdata!=''):
        return render(request,'district_collector/stock_list.html',{'dataofstock':stockdata})
    else:
        return render(request,'district_collector/stock_list.html')

#Ration Shop Officer
def rationshop_officer_register(request):
  
    if request.method == 'POST':
        R_userid = request.POST['r_userid']
        R_number = request.POST['ration_shop_no']
        R_officername = request.POST['officer_name']
        R_password = request.POST['password']
        R_address = request.POST['address']
        R_phone = request.POST['phone']
        R_mail = request.POST['mail']

        object_of_RationshopOfficer = RationShopOfficer()
        object_of_RationshopOfficer.id_number = R_userid
        object_of_RationshopOfficer.name = R_officername
        object_of_RationshopOfficer.shopno = R_number
        object_of_RationshopOfficer.password = R_password
        object_of_RationshopOfficer.address = R_address
        object_of_RationshopOfficer.phonenumber = R_phone
        object_of_RationshopOfficer.mail = R_mail
        try:
            object_of_RationshopOfficer.save()
        except:
            context = {'msg': 'This Officer Details Already Registered '}
            return render(request, 'Ration_Shop/Rationshop_officer_register.html', context)        
        officerdata=RationShopOfficer.objects.all()
        return render(request,'Ration_Shop/Rationshop_officer_register.html',{'dataofshop':officerdata})
    return render(request,'Ration_Shop/Rationshop_officer_register.html')