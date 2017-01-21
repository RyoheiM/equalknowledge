from django.shortcuts import render
from django.http import HttpResponse
from study.models import Study


def study_list(request):
    """学習一覧"""
    studys = Study.objects.all().order_by('id')
    return render(request,'study/study_list.html',{'studys':studys})


def study_edit(request, study_id=None):
    """クラスの編集"""
    return HttpResponse('クラスの編集')


def study_del(request, study_id):
    """クラスの削除"""
    return HttpResponse('クラスの削除')