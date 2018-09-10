from django.conf.urls import patterns,url
from wxapp.views import orderRooms
from wxapp.views import testRooms
from wxapp.views import queryRooms
from wxapp.views import queryDate
from wxapp.views import findRoom
from wxapp.views import deleteRoom
from wxapp.views import makeComment
from wxapp.views import register
from wxapp.views import testify
from wxapp.views import loginin
from wxapp.views import quit
from wxapp.views import modifypassword

urlpatterns=patterns(
	'',
	url(r'^order_room/$',orderRooms,name='orderRooms'),
	url(r'^test_info/$',testRooms,name='testRooms'),
	url(r'^query_room/$',queryRooms,name='queryRooms'),
	url(r'^query_room_date/$',queryDate,name='queryDate'),
	url(r'^find_room/$',findRoom,name='findRoom'),
	url(r'^delete_room/$',deleteRoom,name='deleteRoom'),
	url(r'^make_comment/$',makeComment,name='makeComment'),
	url(r'^register/$',register,name='register'),
	url(r'^testify/$',testify,name='testify'),
	url(r'^login_page/$',loginin,name='loginin'),
	url(r'^quit_page/$',quit,name="quit"),
	url(r'^modify_password',modifypassword,name='modifypassword'),
)

