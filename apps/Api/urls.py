from rest_framework.routers import DefaultRouter

from . import views
from .login_and_register import urlpatterns

router = DefaultRouter()

router.register(prefix='Cinema', viewset=views.CinemaViewset, basename='cinema')
router.register(prefix='Gender', viewset=views.GenderViewset, basename='gender')
router.register(prefix='Movies', viewset=views.MovieViewset, basename='movie')

urlpatterns = router.urls + urlpatterns