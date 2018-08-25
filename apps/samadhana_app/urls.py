from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),


    url(r'^logout$', views.logout),
    

    url(r'^home$', views.home ),
    url(r'^california$', views.california ),
    url(r'^kerala$', views.kerala ),
    url(r'^freetown$', views.freetown ),
    url(r'^support$', views.support ),
    url(r'^food$', views.food ),
    url(r'^shelter$', views.shelter ),
    url(r'^organizations$', views.organizations ),
    url(r'^medical', views.medical ),
    url(r'^technology$', views.technology ),
    # url(r'^process$', views.process),
    # url(r'^(?P<id>\d+)/join$', views.join ),
    # url(r'^(?P<id>\d+)/cancel$', views.cancel ),
    # url(r'^(?P<id>\d+)/delete$', views.delete ),

    # url(r'^(?P<id>\d+)/show$', views.show ),
    # url(r'^(?P<id>\d+)/update$', views.update ),

    url(r'^admin$', views.admin),
    url(r'^add_disaster$', views.add_disaster),
    url(r'^add_ngo$', views.add_ngo),
    url(r'^(?P<id>\d+)/link_org$', views.link_org),
    # url(r'^(?P<id>\d+)/rem_org$', views.rem_org),
    url(r'^posts_kerala$', views.posts_kerala),
    url(r'^(?P<o_id>\d+)/(?P<d_id>\d+)/rem_org$', views.rem_org),
    url(r'^(?P<id>\d+)/link_org_process$', views.link_org_process),
    url(r'^(?P<id>\d+)/delete_cause$', views.delete_cause),
]