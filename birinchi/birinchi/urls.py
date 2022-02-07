
from django.contrib import admin
from django.urls import path
from app1.views import homepage,name,kitoblar,record,mualliflar,kitob_ochir,muallif_ochir,record_ochir


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/',homepage),
    path('name/',name),
    path("kitoblar/",kitoblar, name="kitoblar"),
    path("kitoblar/<int:son>/", kitob_ochir),
    path("record/",record,name="record"),
    path("mualliflar/",mualliflar,name='mualliflar'),
    path("mualliflar/<int:son>/",muallif_ochir),
    path("record/<int:son>/",record_ochir),
]
