# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from invoice.models import StickerOrder


@login_required
def index(request):
    return render(request, 'invoice/index.html', {
        'stickerOrder_list': StickerOrder.objects.order_by('store'),
    })


@login_required
def stickerDetail(request, sticker_id):
    stickerOrder = get_object_or_404(StickerOrder, pk=sticker_id)
    return render(request, 'invoice/stickerDetail.html', {'stickerOrder': stickerOrder})


@login_required
def stickerUnprinted(request):
    stickerOrder_list = StickerOrder.objects.filter(printed=False)
    return render(request, 'invoice/stickerList.html', {'stickerOrder_list': stickerOrder_list})
