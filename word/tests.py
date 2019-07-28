from django.test import TestCase,client
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Daily_words
class WordTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
        username='test',
        email='test@email.com',
        password='secret'
        ) 
        self.shabd=Daily_words.objects.create(
            Word='sample',
            Meaning='meaning',
            Synonyms='synonyms',
            Antonyms='antonyms',
            Examples='examples',
            AddedBy=self.user,
        )

    def test_string_representation(self):
        shabd=Daily_words(Word='sample')
        self.assertEqual(str(shabd),shabd.Word)

    def test_get_absolute_url(self):
        self.assertEqual(self.shabd.get_absolute_url(),'/word/1/')
 
    def test_word_content(self):
        self.assertEqual(f'{self.shabd.Word}', 'sample')
        self.assertEqual(f'{self.shabd.AddedBy}','test')
        self.assertEqual(f'{self.shabd.Meaning}','meaning')
        self.assertEqual(f'{self.shabd.Synonyms}','synonyms')
        self.assertEqual(f'{self.shabd.Antonyms}','antonyms')
        self.assertEqual(f'{self.shabd.Examples}','examples')

    def test_list_view(self):
        response=self.client.get(reverse('HOME'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'Home.html')
        self.assertContains(response,'meaning')

    def test_detail_view(self):
        response=self.client.get('/word/1/')
        no_response=self.client.get('/word/1000/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'Word.html')
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'examples')

    def test_create_view(self):
        response=self.client.post(reverse('NEW'),{
            'Word':'sample2',
            'Meaning':'meaning2',
            'Synonyms':'synonyms2',
            'Antonyms':'antonyms2',
            'Examples':'example2s',
            'AddedBy':self.user
        })
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'sample2')
        self.assertTemplateUsed(response,'new_word.html')
    def test_update_view(self):
        response=self.client.post(reverse('Update',args='1'),{
            'Word':'word3',
            'Meaning':'mean'
        })
        self.assertEqual(response.status_code,302)
    
    def test_delete_view(self):
        response=self.client.get(reverse('Delete', args='1'))
        self.assertEqual(response.status_code,200)