from django.test import TestCase
from .models import Blog

# Create your tests here.
class BlogModelTests(TestCase):
    def test_blog_integrity(self):
        all_blogs = Blog.objects.all()
        tests = [blog.title == '""' for blog in all_blogs]        
        self.assertTrue(any(tests), "Blog Title cannot be an empty string.")

        