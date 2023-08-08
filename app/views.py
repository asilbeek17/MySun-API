from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from app.models import Product_Category, Product, Project_Category, Project, Blog, Contact, Review, Review_for_business, \
    Newsletter
from app.serializers import *


class Product_CategoryView(ModelViewSet):
    queryset = Product_Category.objects.all().order_by('-id')
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']


class ProductView(ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'characteristic']


class Project_CategoryView(ModelViewSet):
    queryset = Project_Category.objects.all().order_by('-id')
    serializer_class = ProjectCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']


class ProjectView(ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']


class BlogView(ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']


class ContactView(ModelViewSet):
    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['full_name', 'email', 'phone_number']
    search_fields = ['full_name', 'email', 'phone_number']


class ReviewView(ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['full_name', 'phone_number']
    search_fields = ['full_name', 'phone_number']


class Review_for_businessView(ModelViewSet):
    queryset = Review_for_business.objects.all().order_by('-id')
    serializer_class = ReviewForBusinessSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['full_name', 'company', 'phone_number']
    search_fields = ['full_name', 'company', 'phone_number']


class NewsletterView(ModelViewSet):
    queryset = Newsletter.objects.all().order_by('-id')
    serializer_class = NewsletterReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['email']
    search_fields = ['email']