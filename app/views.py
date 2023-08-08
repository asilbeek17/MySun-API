from rest_framework.viewsets import ModelViewSet
from app.models import Product_Category, Product, Project_Category, Project, Blog, Contact, Review, Review_for_business, \
    Newsletter
from app.serializers import Product_CategorySerializers, ProductSerializers, Project_CategorySerializers, \
    ProjectSerializers, BlogSerializers, ContactSerializers, ReviewSerializers, Review_for_businessSerializers, \
    NewsLetterSerializers


class Product_CategoryView(ModelViewSet):
    queryset = Product_Category.objects.all().order_by('-id')
    serializer_class = Product_CategorySerializers

class ProductView(ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializers

class Project_CategoryView(ModelViewSet):
    queryset = Project_Category.objects.all().order_by('-id')
    serializer_class = Project_CategorySerializers

class ProjectView(ModelViewSet):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializers

class BlogView(ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializers

class ContactView(ModelViewSet):
    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializers

class ReviewView(ModelViewSet):
    queryset = Review.objects.all().order_by('-id')
    serializer_class = ReviewSerializers

class Review_for_businessView(ModelViewSet):
    queryset = Review_for_business.objects.all().order_by('-id')
    serializer_class = Review_for_businessSerializers

class NewsletterView(ModelViewSet):
    queryset = Newsletter.objects.all().order_by('-id')
    serializer_class = NewsLetterSerializers