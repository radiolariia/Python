from django.db import models

class Article(models.Model):
    article_title = models.CharField('arName', max_length = 200)
    article_text = models.TextField('text')
    pub_date = models.DateTimeField('date')

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('name', max_length = 50)
    comment_text = models.TextField('comment', max_length = 200)
    
    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
