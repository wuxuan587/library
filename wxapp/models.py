from django.db import models
import json
import datetime
import time

# Create your models here.

class order(models.Model):
	list_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=20,default='wx',null=True,blank=True)
	department=models.CharField(max_length=20,default='netcenter',null=True,blank=True)
	tel=models.BigIntegerField(default=319,null=True)
	order_date=models.DateField(default='2018-01-01',blank=True,null=True)
	start_time=models.TimeField(default='09:00',blank=True,null=True)
	end_time=models.TimeField(default='10:00',blank=True,null=True)
	meeting_content=models.TextField(max_length=100,blank=True,null=True)


class test(models.Model):
	name=models.CharField(primary_key=True,max_length=20)
	tel=models.IntegerField(default=25)



class CJsonEncoder(json.JSONEncoder):
	def default(self,obj):
		if isinstance(obj,datetime.datetime):
			return obj.strftime('%Y-%m-%d %H:%M:%S')
		elif isinstance(obj,datetime.date):
			return obj.strftime("%y-%m-%d")
		elif isinstance(obj,time.time()):
			return obj.strftime("%H:%M:%S")
		else:
			return json.JSONEncoder.default(self.obj)

class comment(models.Model):
	leave_message=models.CharField(primary_key=True,max_length=100)