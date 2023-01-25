from django.shortcuts import render, get_object_or_404

from .models import TreeMenu_MPTT


def main(request):
    context = {
        'menu': TreeMenu_MPTT.objects.all(),
    }
    return render(request, 'base.html', context)


def menu_detail_MPTT(request, id, slug):
    menu_items = get_object_or_404(TreeMenu_MPTT,
                             id=id,
                             slug=slug)
    context = {
        'menu_items': menu_items,
        'menu': TreeMenu_MPTT.objects.all(),
    }
    return render(request, 'detail.html', context)