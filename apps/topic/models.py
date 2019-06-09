from django.db import models


# Create your models here.

# id: int
# topic_url: string
# title: string
# user_created: int
# created_date: date
# states: int 0 disable, 1 expire, 2 active


class Topics(models.Model):
    STATUS = (
        (1, "expire"),
        (2, "active"),
        (0, "disable"),
    )
    topic_url = models.CharField(max_length=80, default="", verbose_name="location", help_text="location")
    title = models.CharField(max_length=80, default="", verbose_name="title", help_text="title")
    userid = models.IntegerField(default=0, verbose_name="userid", help_text='userid')
    created_date = models.DateTimeField(verbose_name='data tiem', help_text='date time')
    states = models.IntegerField(choices=STATUS, verbose_name="status",
                                 help_text="status")

    class Meta:
        verbose_name = "Topics"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
