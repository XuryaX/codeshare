from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, HttpResponseRedirect
from snips.models import Snippet
from snips.forms import Snippet_Form

@login_required
def snipall(request):
    snipinfo =Snippet.objects.all()
    pagin = Paginator(snipinfo,3)
    page = request.GET.get('page')
    args = dict()
    try:
        args['snips'] = pagin.page(page)
    except PageNotAnInteger:
        args['snips'] = pagin.page(1)
    except EmptyPage:
        args['snips'] = pagin.page(pagin.num_pages)
    args['name'] = request.user.username
    return render_to_response('snippet_list.html',args)

@login_required
def snip_detail(request,object_id=1):
    args=dict()
    args['name'] = request.user.username
    args['snip']=Snippet.objects.get(id=object_id)
    return render_to_response('snippet_detail.html',args)


def create_snippet(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    if request.POST:
        form = Snippet_Form(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            setattr(snippet,'author',request.user)
            snippet.save()
            return HttpResponseRedirect('/snips/all/')
    else:
        form = Snippet_Form()
    args = dict()
    args['form'] = form
    args['name'] = request.user.username
    args.update(csrf(request))
    return render_to_response('createsnippet.html',args)