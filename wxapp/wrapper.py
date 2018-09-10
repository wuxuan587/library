import traceback

def view_exception_safe(fn):
	def wrapper(*args,**kwargs):
		try:
			return fn(*args,**kwargs)
		except Exception,e:
			return HttpResponse(
			json.dumps({
				'code':-1,
				'msg':str(e)
				   }))
		return wrapper
