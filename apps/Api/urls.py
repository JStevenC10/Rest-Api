from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(prefix='Cinema', viewset=views.CinemaViewset, basename='cinema')
router.register(prefix='Gender', viewset=views.GenderViewset, basename='gender')
router.register(prefix='Movies', viewset=views.MovieViewset, basename='movie')

urlpatterns = router.urls