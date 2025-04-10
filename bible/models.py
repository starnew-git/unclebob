from django.db import models

class Version(models.Model):
    """성경 번역본 정보를 저장하는 모델"""
    name = models.CharField(max_length=100, unique=True, verbose_name="번역본 이름")
    language = models.CharField(max_length=50, verbose_name="언어")
    description = models.TextField(blank=True, verbose_name="설명")

    class Meta:
        verbose_name = "성경 번역본"
        verbose_name_plural = "성경 번역본들"

    def __str__(self):
        return self.name

class Testament(models.Model):
    """성경의 구약과 신약 구분 정보를 저장하는 모델"""
    name = models.CharField(max_length=50, verbose_name="구분 이름")

    class Meta:
        verbose_name = "성경 구분"
        verbose_name_plural = "성경 구분들"

    def __str__(self):
        return self.name
    

class Book(models.Model):
    """성경의 각 권 정보를 저장하는 모델"""
    name = models.CharField(max_length=50, verbose_name="권 이름")
    abbreviation = models.CharField(max_length=10, verbose_name="약어")
    testament = models.ForeignKey(Testament, on_delete=models.CASCADE, related_name="books", verbose_name="구분")

    class Meta:
        verbose_name = "성경 권"
        verbose_name_plural = "성경 권들"

    def __str__(self):
        return f"{self.name}({self.abbreviation})"

class Verse(models.Model):
    """성경의 각 절 정보를 저장하는 모델"""
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name="verses", verbose_name="번역본")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="verses", verbose_name="권")
    chapter = models.IntegerField(verbose_name="장 번호")
    number = models.IntegerField(verbose_name="절 번호")
    content = models.TextField(verbose_name="내용")

    class Meta:
        verbose_name = "성경 절"
        verbose_name_plural = "성경 절들"
        ordering = ['version', 'book', 'chapter', 'number']

    def __str__(self):
        return f"{self.chapter}절"