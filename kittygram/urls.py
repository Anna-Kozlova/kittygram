from django.urls import include, path

# from cats.views import APICat
# from cats.views import CatList, CatDetail
from rest_framework.routers import DefaultRouter
from cats.views import CatViewSet

router = DefaultRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
