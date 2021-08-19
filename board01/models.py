from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

# # SQLAlchemy
# from sqlalchemy import Sequence, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

class Board(models.Model):
    b_no = models.AutoField(db_column='b_no', primary_key=True)
    b_title = models.CharField(db_column='b_title', max_length=255)
    # b_note = models.TextField(db_column='b_note', )
    # b_note = RichTextField()
    # b_note = RichTextUploadingField()
    b_note = RichTextUploadingField(blank=True,null=True)
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    parent_no = models.IntegerField(db_column='parent_no', default=0)
    b_count = models.IntegerField(db_column='b_count', default=0)
    b_date = models.DateTimeField(db_column='b_date', )
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default='1')


    #  내부 class - form에서는 기본 필드의 값을 재정의할 때 사용한다
    class Meta:
        managed = False
        db_table = 'board01'

    # __str__ : 데이터를 보기 쉽게 변환
    def __str__(self):
        return "제목 : " + self.b_title + ", 작성자 : " + self.b_writer
