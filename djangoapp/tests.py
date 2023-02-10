from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.utils import timezone

from .forms import ArticlesForm
from .models import Articles
from django.conf import settings


# Define a test case class
class ArticleTestCase(TestCase):

    def test_model(self):
        # Create a task instance
        Article = Articles.objects.create(title={settings.LANGUAGE_CODE: 'Test Task'})

        # Check if the task instance has been created successfully
        self.assertTrue(Articles.objects.filter(id=Article.id).exists())

        # Check if the task title is returned correctly
        self.assertEqual(str(Article), 'Test Task')

        # Check if the task is_done field is set to False by default
        self.assertFalse(Article.is_done)

        # Check if the task created field has the correct value
        self.assertLessEqual(Article.created, timezone.now())

        # Check if the task updated field has the correct value
        self.assertLessEqual(Article.updated, timezone.now())

    def test_form(self):
        # Create a task instance
        Article = Articles.objects.create(title={settings.LANGUAGE_CODE: 'Test Article'})

        # Check if the form data is correctly saved
        form = ArticlesForm(data={'Author': "monica", f'title_{settings.LANGUAGE_CODE}': 'Test Article2'}, instance=Article)
        self.assertTrue(form.is_valid())
        Article = form.save()
        self.assertEqual(Article.title, {settings.LANGUAGE_CODE: 'Test Article2', 'fr': '', 'hi': ''})
        self.assertTrue(Article.is_done)