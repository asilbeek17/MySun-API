from rest_framework.serializers import ModelSerializer
from app.models import *


class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model = Product_Category
        exclude = ()


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        exclude = ()


class ProjectCategorySerializer(ModelSerializer):

    class Meta:
        model = Project_Category
        exclude = ()


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        exclude = ()


class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        exclude = ()


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        exclude = ()


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        exclude = ()


class ReviewForBusinessSerializer(ModelSerializer):

    class Meta:
        model = Review_for_business
        exclude = ()


class NewsletterReviewSerializer(ModelSerializer):

    class Meta:
        model = Newsletter
        exclude = ()