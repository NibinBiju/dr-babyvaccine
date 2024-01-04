from django.urls import path
from .views import *

urlpatterns=[
    path('authtoken/',Registeruser.as_view()),
    path('authlogin/',LoginView.as_view(),name='logins'),
    path('logoutt/',logoutview.as_view),
    
    #view all child,and post child detail

    path('childcreate/', ChildListCreateView.as_view(), name='child-list'),
<<<<<<< HEAD
    
    #get one child,udate,delete
    path('modifychildren/<int:pk>/', ChildDetailView.as_view(), name='child-detail'),
#
    path('vax-program-names/', VaxProgramNameListCreateView.as_view(), name='vax-program-name-list'),
    path('vax-program-names/<int:pk>/', VaxProgramNameDetailView.as_view(), name='vax-program-name-detail'),

    path('vax-cycle-names/', VaxCycleNameListCreateView.as_view(), name='vax-cycle-name-list'),
    path('vax-cycle-names/<int:pk>/', VaxCycleNameDetailView.as_view(), name='vax-cycle-name-detail'),
=======
    path('children/<int:pk>/', ChildDetailView.as_view(), name='child-detail'),

    
>>>>>>> 04383191e441f26652f9805ac9a814cdfbc17735

    path('vax-names/', VaxNameListCreateView.as_view(), name='vax-name-list'),
    path('vax-names/<int:pk>/', VaxNameDetailView.as_view(), name='vax-name-detail'),

    # path('vax-programscreate/', VaxProgramView.as_view(), name='vax-program-list'),
    # path('vax-programs-modify/<int:pk>/', VaxProgramDelete_Update.as_view(), name='vax-program-detail'),

    path('vax-cycles/', VaxCycleAPIView.as_view(), name='vax-cycle-list'),
    path('vax-cycles/<int:pk>/', VaxCycleDelete_Update.as_view(), name='vax-cycle-detail'),

<<<<<<< HEAD
    path('vaxes/', VaxListCreateView.as_view(), name='vax-list'),
    path('vaxes/<int:pk>/', VaxDetailView.as_view(), name='vax-detail'),
    #
=======
    path('vaxes/', VaxAPIView.as_view(), name='vax-list'),
    path('vaxes/<int:pk>/', VaxDelete_Update.as_view(), name='vax-detail'),


     path('childcreate/<int:child_id>/vaccination-dates/',vaccination_dates_view, name='vaccination_dates'),
    #  path('vaccination/<int:child_id>/', VaccinationProgramView.as_view(), name='vaccination_programs'),
    
    # path('vaccination-dates/<int:child_id>/', VaccinationDatesAPIView.as_view(), name='vaccination-dates'),
   
   
>>>>>>> 04383191e441f26652f9805ac9a814cdfbc17735

    #notification
    path('send_mail_date/',send_mail_to_parent),
    #  path('send-mail/', SendMailToParentView.as_view(), name='send-mail'),
    
<<<<<<< HEAD
    #dates
    path('childcreate/<int:child_id>/vaccination-dates/',vaccination_dates_view, name='vaccination_dates')
=======

    #chat
    # path('chat/', ChatbotAPI.as_view(), name='chat'),
    path('chatbot/', ChatbotAPI.as_view(), name='chatbot_api'),

>>>>>>> 04383191e441f26652f9805ac9a814cdfbc17735



]