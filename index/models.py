# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Admissionsforms(models.Model):
    sid = models.IntegerField(primary_key=True)
    cname = models.ForeignKey('Clazz', models.DO_NOTHING, db_column='cname', blank=True, null=True)
    sname = models.CharField(max_length=12)
    indate = models.DateField()
    inscore = models.DecimalField(max_digits=8, decimal_places=2)
    agent = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'admissionsforms'


class Bookborrow(models.Model):
    bid = models.ForeignKey('Bookinfo', models.DO_NOTHING, db_column='bid')
    sid = models.ForeignKey('Stuinfo', models.DO_NOTHING, db_column='sid')
    borrowdate = models.DateField()
    returndate = models.DateField()
    operator = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'bookborrow'


class Bookinfo(models.Model):
    bid = models.IntegerField(primary_key=True)
    bname = models.CharField(max_length=12)
    author = models.CharField(max_length=12)
    category = models.CharField(max_length=12)
    publication = models.CharField(max_length=12)
    pubdate = models.DateField()
    bnum = models.IntegerField()
    indate = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    intro = models.CharField(max_length=100)
    operator = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'bookinfo'



class Choosecur(models.Model):
    sid = models.ForeignKey('Stuinfo', models.DO_NOTHING, db_column='sid')
    curid = models.ForeignKey('Course', models.DO_NOTHING, db_column='curid')
    score = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'choosecur'


class Clazz(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=24)

    gid = models.ForeignKey('Grade', models.DO_NOTHING, db_column='gid', blank=True, null=True)
    mid = models.ForeignKey('Major', models.DO_NOTHING, db_column='mid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clazz'


class Course(models.Model):
    curid = models.IntegerField(primary_key=True)
    curname = models.CharField(max_length=12)
    examdate = models.DateField()
    examtype = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'course'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Grade(models.Model):
    gid = models.IntegerField(primary_key=True)
    gname = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'grade'


class Login(models.Model):
    uaccount = models.CharField(primary_key=True, max_length=12)
    upwd = models.CharField(max_length=12)
    uname = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'login'


class Major(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'major'


class Stuinfo(models.Model):
    sid = models.ForeignKey(Admissionsforms, models.DO_NOTHING, db_column='sid', primary_key=True)
    identitynum = models.CharField(db_column='identityNum', max_length=18)  # Field name made lowercase.
    gender = models.CharField(max_length=5)
    birthdate = models.DateField()
    address = models.CharField(max_length=20)
    age = models.IntegerField()
    tel = models.CharField(max_length=11)
    politicstatus = models.CharField(max_length=12)
    health = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'stuinfo'


class Teacherinfo(models.Model):
    tid = models.AutoField(primary_key=True)
    mid = models.ForeignKey(Major, models.DO_NOTHING, db_column='mid', blank=True, null=True)
    tname = models.CharField(max_length=12)
    gender = models.CharField(max_length=5)
    age = models.IntegerField()
    married = models.CharField(max_length=12)
    idnum = models.CharField(max_length=18)
    politicstatus = models.CharField(max_length=10)
    nation = models.CharField(max_length=12)
    edu = models.CharField(max_length=12)
    birthdate = models.DateField()
    tel = models.CharField(max_length=11)
    workdate = models.DateField()
    description = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'teacherinfo'


class Techcourse(models.Model):
    tid = models.ForeignKey(Teacherinfo, models.DO_NOTHING, db_column='tid')
    curid = models.ForeignKey(Course, models.DO_NOTHING, db_column='curid')

    class Meta:
        managed = False
        db_table = 'techcourse'
