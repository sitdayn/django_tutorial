from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_future_question(self):
        """вопрос из будущего - не <<свежий>>."""
        time = timezone.now() + timedelta(days=30)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)

    def test_old_question(self):
        time = timezone.now() - timedelta(days=1, seconds=1)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), False)

    def test_recent_question(self):
        time = timezone.now() - timedelta(hours=23, minutes=59)
        question = Question(pub_date=time)
        self.assertIs(question.was_published_recently(), True)

    def create_question(text, days):
        """days < 0 - вопрос в прошлом, days > 0 - в будущем. """
        time = timezone.now() + timedelta(days=days)
        return Question.objects.create(
            question_text=text, pub_date=time
        )    

class IndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "пока нет ни одного опроса")    