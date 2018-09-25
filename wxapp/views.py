#coding:utf-8

import json
import time
import requests
import traceback
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponse
from wxapp.models import order
from wxapp.models import test
from wxapp.models import CJsonEncoder
from django.http import JsonResponse
#from wxapp.wrapper import view_exception_safe
from django.forms.models import model_to_dict
from wxapp.models import comment

from utils.logger import logger_for_wxapp_view as logger

# Create your views here.


#def orderRooms(requests):
#	Data=order(name=requests.GET.get('name'),department=requests.GET.get('department'),tel=requests.GET.get('tel'),order_date=requests.GET.get('order_date'),start_time=requests.GET.get('start_time'),end_time=requests.GET.get('end_time'))
#	result=order.objects.filter(order_date=requests.GET.get('order_date'),start_time=requests.GET.get('start_time')).all()
#	msg1='failed'
#	msg2='successful'
#	ret_body1=dict(message=msg1)
#	ret_body2=dict(message=msg2)
#	if result.exists():
#		return HttpResponse(json.dumps(ret_body1))
#	else:
#		Data.save()
#		return HttpResponse(json.dumps(ret_body2))

def orderRooms(requests):
#	logger.debug(requests.GET)
	Data=order(index=requests.GET.get('index'),name=requests.GET.get('name'),department=requests.GET.get('department'),tel=requests.GET.get('tel'),order_date=requests.GET.get('order_date'),start_time=requests.GET.get('start_time'),end_time=requests.GET.get('end_time'))
	logger.info("Index: {0}".format(requests.GET.get('index')))
#	result=order.objects.filter(order_date=requests.GET.get('order_date'),start_time=requests.GET.get('start_time')).all()
	res=order.objects.filter(order_date=requests.GET.get('order_date'))
	first=requests.GET.get('start_time')
	last=requests.GET.get('end_time')
#	first1=str(first).join(":00")
#	last1=str(last).join(":00")
#	index=requests.GET.get('index')
	msg1='failed'
	msg2='successful'
	msg3='conflict'
	room_list=[]
	ret_body1=dict(message=msg1)


#	if result.exists():
#		return HttpResponse(json.dumps(ret_body1))
#	else:
	for room in res:
		room_info=dict()
		room_info['start_time']=str(room.start_time)
		room_info['end_time']=str(room.end_time)
#		if ((first<room_info['end_time'] and first>room_info['start_time']) or (last>room_info['start_time'] and last<room_info['end_time'])):
		if (((room_info['start_time'][0:5]<= first <room_info['end_time'][0:5]) or (room_info['start_time'][0:5]< last <=room_info['end_time'][0:5] )) or ((first < room_info['start_time'][0:5]) and (room_info['end_time'][0:5]<last ))):
#			a=first
#			b=room_info['start_time'][0:5]
#			c=room_info['end_time']
#			room_list.append(b)
#			ret_body3 = dict(message=msg3,data=room_list)
			ret_body3=dict(message=msg3)
			return HttpResponse(json.dumps(ret_body3))
	Data.save()
#	a = first
#	b = room_info['start_time']
#	c = room_info['end_time']
#	d=first
#	room_list.append(a)
#	ret_body2 = dict(message=msg2,data=room_list)
	ret_body2 = dict(message=msg2)
	return HttpResponse(json.dumps(ret_body2))


def testRooms(requests):
	res=test.objects.all()
	room_list=[]
	for room in res:
		room_info=dict()
		room_info['name']=room.name
		room_info['tel']=room.tel
		room_list.append(room_info)
	msg='get room msg successfully!'
	ret_body=dict(code=0,massg=msg,data=room_list)
	return HttpResponse(json.dumps(ret_body))


def queryRooms(requests):
	import pdb
	pdb.set_trace()
	res=order.objects.all()
#	res=serializers.serialize('python',order.objects.all(),ensure_scii=False)
	room_list=[]
	for room in res:
		room_info=dict()
		room_info['name']=room.name
		room_info['department']=room.department
		room_info['tel']=room.tel
		room_info['order_date']=str(room.order_date)
		room_info['start_time']=str(room.start_time)
		room_info['end_time']=str(room.end_time)
		room_info['meeting_content']=room.meeting_content
		room_list.append(room_info)	
	
	msg='get room msg successfully!'
	ret_body=dict(code=0,massg=msg,data=room_list)

	return HttpResponse(json.dumps(ret_body,cls=CJsonEncoder))

#@view_exception_safe
def queryDate(requests):
#	try:
		res=order.objects.filter(order_date=requests.GET.get('order_date')).all().order_by("start_time")
		room_list=[]
		for room in res:
			room_info=dict()
			room_info['name']=room.name
			room_info['department']=room.department
			room_info['start_time']=str(room.start_time)
			room_info['end_time']=str(room.end_time)
			room_list.append(room_info)

		msg='get room msg successfully!'
		ret_body=dict(code=0,msg=msg,data=room_list)
		return HttpResponse(json.dumps(ret_body))

#	except Exception as e:
#			msg=traceback.format_exc()
#			ret_body=dict(code=-1,msg=msg)
#			return HttpResponse(json.dumps(ret_body))

def findRoom(requests):
		res=order.objects.filter(name=requests.GET.get('name'),order_date=requests.GET.get('order_date'),start_time=requests.GET.get('start_time')).all()
		room_list=[]
		for room in res:
			room_info=dict()
			room_info['name']=room.name
			room_info['department']=room.department
			room_info['tel']=room.tel
			room_info['order_date']=str(room.order_date)
			room_info['start_time']=str(room.start_time)
			room_info['end_time']=str(room.end_time)
			room_list.append(room_info)

		msg='get room msg successfully!'
		ret_body=dict(code=0,msg=msg,data=room_list)
		return HttpResponse(json.dumps(ret_body))

def deleteRoom(requests):
		res = order.objects.filter(name=requests.GET.get('name'), order_date=requests.GET.get('order_date'),start_time=requests.GET.get('start_time')).all()
		aa=res.delete()
		return HttpResponse("<p>删除记录成功！<p>")

def makeComment(requests):
		Comment=comment(leave_message=requests.GET.get('comment'))
		Comment.save()
		return HttpResponse("<p>评论成功！<p>")

def register(requests):
	pd1=requests.GET.get('password1')
	pd2=requests.GET.get('password2')
	result=User.objects.filter(email=requests.GET.get('email')).all()
	msg1 = 'success'
	msg2 = 'failed'
	msg3 = 'same'
	if result.exists():
		ret_body3=dict(message=msg3)
		return HttpResponse(json.dumps(ret_body3))
	elif pd1==pd2:
		ret_body2=dict(message=msg1)
		user = User.objects.create_user(username=requests.GET.get('username'), email=requests.GET.get('email'),password=requests.GET.get('password1'))
		user.save()
		return HttpResponse(json.dumps(ret_body2))

	else:
		ret_body1=dict(message=msg2)
		return HttpResponse(json.dumps(ret_body1))

def loginin(requests):
	user=authenticate(username=requests.GET.get('username'),password=requests.GET.get('password'))
	msg1='success'
	msg2='failed'
	if user is not None:
		if user.is_active:
			ret_body1=dict(message=msg1)
			login(requests,user)
			return HttpResponse(json.dumps(ret_body1))
		else:
			ret_body2=dict(message=msg2)
			return HttpResponse(json.dumps(ret_body2))
	else:
		ret_body2 = dict(message=msg2)
		return HttpResponse(json.dumps(ret_body2))

def quit(requests):
	msg="success"
	ret_body=dict(message=msg)
	logout(requests)
	return HttpResponse(json.dumps(ret_body))

def testify(requests):
	example=User.objects.filter(username=requests.GET.get('username')).all()
	msg1='success'
	msg2='failed'
	if example.exists():
		ret_body1=dict(message=msg2)
		return HttpResponse(json.dumps(ret_body1))
	else:
		ret_body2=dict(message=msg1)
		return  HttpResponse(json.dumps(ret_body2))

def modifypassword(requests):
	result=User.objects.get(username=requests.GET.get('username'),email=requests.GET.get('email'))
	pd1=requests.GET.get('password1')
	pd2=requests.GET.get('password2')
	msg1 = 'success'
	msg2 = 'failed'
	msg3 = 'different'
#	if  not result.exists():
	if result is None:
		ret_body=dict(message=msg2)
		return HttpResponse(json.dumps(ret_body))
	elif pd1==pd2:
		ret_body2=dict(message=msg1)
		result.set_password(pd2)
		result.save()
		return HttpResponse(json.dumps(ret_body2))
	else:
		ret_body3=dict(message=msg3)
		return HttpResponse(json.dumps(ret_body3))