from django.conf.urls import url, include
from django.urls import path

# from . import views
import board01.views
from board01 import views

urlpatterns = [
    path('', board01.views.home, name="home"),
    path('board', board01.views.board, name="board"),
    path('board_write', board01.views.board_write, name="board_write"),
    path('board_insert', board01.views.board_insert, name="board_insert"),
    path('board_view', board01.views.board_view, name="board_view"),
    path('board_edit', board01.views.board_edit, name="board_edit"),
    path('board_update', board01.views.board_update, name="board_update"),
    path('board_delete', board01.views.board_delete, name="board_delete"),
    path('dashboard', board01.views.dashboard, name="dashboard"),
    path('board_ajax', board01.views.board_ajax, name="board_ajax"),
    path('board_deleteajax', board01.views.board_deleteajax, name="board_deleteajax")
]

# path 에 숫자가 mapping 될 경우 : path('<int:board.bno>/', board.views.board_detail),
