from django.shortcuts import render

# Create your views here.
def blah(request):
	context = {
	"msg" : "Hello World!"
	}
	return render(request,'blah.html',context)