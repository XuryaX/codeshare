__author__ = 'Shaurya'

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from snips.models import Language,Snippet
from django.shortcuts import render_to_response

@login_required
def lang_all(request):
    args=dict()
    args['name'] = request.user.username
    args['language'] = Language.objects.all()
    return render_to_response("langlist.html",args)

@login_required
def lang_detail(request,slg):
    args=dict()
    args['name'] = request.user.username
    args['language'] = get_object_or_404(Language, slug=slg)
    snip=Snippet.objects.filter(language=args['language'])
    pagin=Paginator(snip,3)
    pageno=request.GET.get('page')
    try:
        args['snips'] = pagin.page(pageno)
    except PageNotAnInteger:
        args['snips'] = pagin.page(1)
    except EmptyPage:
        args['snips'] = pagin.page(pagin.num_pages)

    return render_to_response('snippet_list.html',args)
