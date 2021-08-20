# render >> 데이터 값을 받아온 뒤 html로 데이터를 보내기 위한 함수
from django.http import JsonResponse
from django.shortcuts import render, redirect
from requests import Response

from board01.models import Board
import logging
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.db import connection
import pymysql


# # SQL Alchemy part
# from sqlalchemy import create_engine, select
# DB_URL = 'mysql+mysqldb://root:0429@ㅣlocalhost:3306/example_db_01?charset=utf8'
# engine = create_engine(DB_URL)
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker()
# sess = Session()

# ****************************************
# render >> rendering : model data 를 html 코드로 변환
# 404 error >>
# from django.shortcuts import render, get__object_or_404
# (ex -> question = get_objcet_or_404(Question, pk=question_id)

logger = logging.getLogger('log')

def home(request):
    return render(request, "home.html")

def board(request):
    rsBoard = Board.objects.all()
    print(rsBoard)

    return render(request, "board_list.html", {
        'rsBoard': rsBoard
    })

def board_write(request):

    # form = CreateBoard()

    return render(request, "board_write.html")

def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
        return redirect('/board')

    else:
        return redirect('/board_write')

def board_view(request):
    bno = request.GET['b_no']
    # filter : b_no = bno 의 조건을 충족하는 모델 데이터 조회
    # but filter 함수의 return값은 queryset이므로 1개의 데이터만 조회하고 싶다면 get함수를 쓰는 것이 좋다
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_view.html", {
        'rsDetail': rsDetail
    })

def board_edit(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_edit.html", {
        'rsDetail': rsDetail
    })


def board_update(request):
    bno = request.GET['b_no']
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote
        if bwriter != "":
            board.b_writer = bwriter

        try:
            board.save()
            return redirect('/board')
        except ValueError:
            return Response({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return Response({"success": False, "msg": "게시글 없음"})

def board_delete(request):
    bno = request.GET['b_no']
    rows = Board.objects.get(b_no=bno).delete()

    return redirect('/board')

# dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

# Ajax
def board_ajax(request):
    # rsBoard = Board.objects.all()
    # print(rsBoard)
    rsBoard = Board.objects.all()

    return render(request, "board_ajax.html", {
        'rsBoard': rsBoard
    })

@csrf_exempt
def board_deleteajax(request):

    bno = request.GET['b_no']

    rsBoard = Board.objects.get(b_no=bno).delete()
    # rsBoard.save()

    data = {}
    data['result_msg'] = 'Deleted...'

    logger.info('******************************************')
    logger.info(data)

    return JsonResponse(data, content_type="application/json")


