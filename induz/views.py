from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from induz.models import *
import hashlib
# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
	if request.method == 'POST':
		firstname=request.POST['fname']
		lastname=request.POST['lname']
		email=request.POST['email']
		upass=request.POST['password']
		hashpass=hashlib.md5(upass.encode('utf8')).hexdigest()
		query=first_tb(first_name=firstname,last_name=lastname,email=email,password=hashpass)
		query.save()
	return render(request,'contact.html')

def contact2(request):
	if request.method == 'POST':
		address=request.POST['addr']
		state=request.POST['st']
		pincode=request.POST['pin']
		mobile=request.POST['mobnmbr']
		query=register_tb(address_dr=address, state_dr=state, pincode=pincode,mobile=mobile)
		query.save()
	return render(request,'contact2.html')

def login(request):
	if request.method == 'POST':
	    email=request.POST['email1']
	    upass=request.POST['password1']
	    hashpass=hashlib.md5(upass.encode('utf8')).hexdigest()

	    check=first_tb.objects.all().filter(email=email,password=hashpass)
	    if check:
	    	for x in check:
	    
	    		request.session['userid']=x.id
	    	return render(request,'index.html')
	    else:
	    	return render(request,'loginform.html')	
	return render(request,'loginform.html')	


def logout(request):
	if request.session.has_key('userid'):
		del request.session['userid']
	return render(request,'index.html')	

def userprofile(request):
	if request.session.has_key('userid'):
		uid=request.session['userid']
		viewquery = first_tb.objects.all().filter(id=uid)
		return render(request,'contact.html',{'viewqueryinduz':viewquery})
	else:
	    return render(request,'loginform.html')	

			

def services(request):

	viewquery = img_tb.objects.all()
	return render(request,'services.html',{'viewqueryinduz':viewquery})
         

def viewdata(request):
	if request.session.has_key('userid'):
		uid=request.session['userid']
		viewquery = first_tb.objects.all().filter(id=uid)
		return render(request,'contact.html',{'viewqueryinduz':viewquery})
	else:
		return render(request,'loginform.html')



def tabledata(request):

	viewquery = first_tb.objects.all()
	return render(request,'tableinduz.html',{'viewqueryinduz':viewquery})

def datadelete(request):
	usid=request.GET['uid']
	vd=first_tb.objects.all().filter(id=usid).delete()
	viewquery = first_tb.objects.all()
	return render(request,'tableinduz.html',{'viewqueryinduz':viewquery})


def updatedata(request):
	usid=request.GET['uid']
	vd=first_tb.objects.all().filter(id=usid)
	print(vd)
	return render(request,'updateform.html',{'vd':vd})	


def updateformdata(request):
	if request.method == 'POST':
		usid=request.GET['uid']
		firstname=request.POST['fname']
		lastname=request.POST['lname']
		email=request.POST['email']
		password=request.POST['password']
		query=first_tb.objects.all().filter(id=usid).update(first_name=firstname,last_name=lastname,email=email,password=password)
	viewquery = first_tb.objects.all()
	return render(request,'tableinduz.html',{'viewqueryinduz':viewquery})
	

def imgupload(request):
	if request.method == 'POST':
		img=request.FILES['img']
		query=img_tb(image=img)
		query.save()
	return render(request,'img.html')

def imgupload1(request):
	if request.method == 'POST':
		img1=request.FILES['img1']
		query=img_tb(picture=img1)
		query.save()
	return render(request,'img1.html')



from reportlab.pdfgen import canvas 
from django.views.generic import View
from projectinduz.utils import render_to_pdf
def downloadtc(request):
	users=first_tb.objects.all()
	pdf=render_to_pdf('userpdf.html',{'users':users})
	return HttpResponse(pdf,content_type='application/pdf')

def favsteel(request):
    if request.session.has_key('userid'):
    	if request.method=='POST' :
    		favjob=request.POST['favsteel']
    		userid=request.session['userid']
    		uid=first_tb.objects.get(id=userid)
    		query=fav_steel(fav_steel_u=favjob,userid=uid)
    		query.save()
    		return render(request,'favsteel.html')
    	else:
    		return render(request,'favsteel.html')
    else:
    	return render(request,'loginform.html')
    	    	 	

def tabledatafav(request):

	viewquery = fav_steel.objects.all()
	return render(request,'favtable.html',{'viewqueryinduz':viewquery})    	    	 	



def viewuser(request):
    query=first_tb.objects.all()
    return render(request,'ajax.html',{'viewquery':query})	

def box(request):
	print("--------------------------------------------")
	boxid = request.GET.get('bid')
	data = first_tb.objects.all().filter(id=boxid)
	for x in data:
		name = x.last_name
		email = x.email
	dat={"bname":name,"bemail":email}
	print(dat)
	return JsonResponse(dat)	
