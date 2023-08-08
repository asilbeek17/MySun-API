from rest_framework.viewsets import ModelViewSet
from app.models import Product_Category, Product, Project_Category, Project, Blog, Contact, Review, Review_for_business, \
    Newsletter
from app.serializers import *


class Product_CategoryView(ModelViewSet):
    queryset = Product_Category.objects.all().order_by('-id')
    serializer_class = ProductCategorySerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer


class Project_CategoryView(ModelViewSet):
    queryset = Project_Category.objects.all().order_by('-id')
    serializer_class = ProjectCategorySerializer


class ProjectView(ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer


class BlogView(ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer


class ContactView(ModelViewSet):
    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializer


class ReviewView(ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer


class Review_for_businessView(ModelViewSet):
    queryset = Review_for_business.objects.all().order_by('-id')
    serializer_class = ReviewForBusinessSerializer


class NewsletterView(ModelViewSet):
    queryset = Newsletter.objects.all().order_by('-id')
    serializer_class = NewsletterReviewSerializer