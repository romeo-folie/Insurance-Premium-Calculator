from django.conf.urls import url
from calculateInsurance import views


urlpatterns=[
    url(r'^$', views.index, name = 'index'),
    url(r'^result/$',views.result, name='result'),
    url(r'^calculate_insurance/$', views.calculate_insurance, name='calculate_insurance'),
]
