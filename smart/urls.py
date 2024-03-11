from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('gallery/',pic,name='gallery'),
    path('',home,name='index'),
    path('home/',home,name='home'),
    path('events/',events,name='events'),
    path('contact/',contact,name='contact'),
    path('events/cradle',cradle,name='cradle'),
    path('events/birthday/',birthday,name='birthday'),
    path('events/anniversary/',anniversary,name='anniversary'),
    path('events/getTogether/',getTogether,name='getTogether'),
    path('events/party/',party,name='party'),
    path('events/wedding/',wedding,name='wedding'),
    path('events/privateMeeting/',privateMeeting,name='privateMeeting'),
    path('userLogin/',userLogin,name='userLogin'),
    path('login/',log_in,name='log_in'),
    path('logout/',logOut,name='logOut'),
    path('admin_home/',adminHome,name='adminHome'),
    path('CeremoAdmin/index/',dashboard,name='dashboard'),
    path("CeremoAdmin/upload_picture",picture_upload,name='picture_upload'),
    path("CeremoAdmin/delete_user/<int:id>",delete_user,name='delete_user'),
    path("CeremoAdmin/update_user/<int:id>",update_user,name='update_user'),
    path('update_profile/',update_profile, name='update_profile'),
    path('my_bookings/',my_bookings, name='my_bookings'),
    path("CeremoAdmin/volunteers",volunteers,name='volunteers'),
    path("CeremoAdmin/all_bookings",all_bookings,name='all_bookings'),
    path("CeremoAdmin/admin_login",admin_login,name='admin_login'),
    path('my_bookings/<int:id>',cancel_booking, name='cancel_booking'),
    path("CeremoAdmin/all_bookings/<int:id>",delete_booking,name='delete_booking'),
    path("CeremoAdmin/assign_volunteer/<int:id>",assign,name='assign'),
    path("CeremoAdmin/to_gallery",to_gallery,name='to_gallery'),
    path("CeremoAdmin/delete_volunteers/<int:id>",delete_volunteer,name='delete_volunteer'),



]   
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)