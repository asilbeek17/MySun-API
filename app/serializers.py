from rest_framework import serializers
from .models import Product_Category, Product, Project_Category, Project, Blog, Contact, Review, Review_for_business,Newsletter


# PRODUCT #
# PRODUCT CATEGORY SERIALIZERS
class Product_CategorySerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title')
        model = Product_Category


# PRODUCT SERIALIZERS
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','category','title','price','info','descriptions','image_1','image_2','image_3','image_4','characteristic',
               )
        model = Product

# END PRODUCT SERIALIZERS #




# PROJECT #
# PROJECT CATEGORY SERIALIZERS
class Project_CategorySerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title')
        model = Project_Category

# PROJECT SERIALIZERS
class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','category','title','descriptions','power','annual_productivity','amount_of_savings','image_1','image_2','image_3','image_4','image_5','image_6')
        model = Project

# END PROJECT SERIALIZERS #




# BLOG SERIALIZERS #
class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','date','image','description')
        model = Blog

# END BLOG SERIALIZERS #



# CONTACT SERIALIZERS #
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'full_name', 'email', 'phone_number', 'message')
        model = Contact

# END CONTACT SERIALIZERS #




# REVIEW SERIALIZERS #
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'full_name','phone_number', 'message')
        model = Review

# END REVIEW SERIALIZERS #



# REVIEW FOR BUSINESS  SERIALIZERS #
class Review_for_businessSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'full_name','phone_number', 'company')
        model = Review_for_business

# END REVIEW FOR BUSINESS SERIALIZERS #



# NEWSLETTER SERIALIZERS #
class NewsLetterSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','email')
        model = Newsletter

# END NEWSLETTER SERIALIZERS #