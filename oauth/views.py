
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext

def home(request):
   # context = RequestContext(request,
   #                         {'request': request,
   #                          'user': request.user})
   # return render_to_response('loginpg.html',
   #                           context_instance=context)
   return render(request,'loginpg.html')