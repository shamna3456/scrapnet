from django.conf.urls import url
from certificate import views

urlpatterns=[
    url('manage_certificate_rto/',views.rto_manage_certificate),
    url('user_view/',views.user_view_certificate),
    url('post/(?P<idd>\w+)',views.post_certificate),
    url('delete/(?P<idd>\w+)',views.delete),
    url('generate_certficate(?P<idd>\w+)',views.generate_certificate),

    url('download/(?P<idd>\w+)', views.generate_certificate),
    url('check/(?P<idd>\w+)', views.check),

    url('add/(?P<idd>\w+)',views.add_certi_req),
    url('user_view/',views.user_view),
    url('rto/',views.rto_view),

    url('issue/(?P<idd>\w+)',views.post_certificate1)

]