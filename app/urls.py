from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import *

router = DefaultRouter()
router.register('Product_Category',Project_CategoryView)
router.register('Product',ProductView)
router.register('Project_Category',Project_CategoryView)
router.register('Project',ProjectView)
router.register('Blog',BlogView)
router.register('Contact',ContactView)
router.register('Review',ReviewView)
router.register('Review_for_business',Review_for_businessView)
router.register('Newsletter', NewsletterView)

urlpatterns = [
    path('',include(router.urls)),
]