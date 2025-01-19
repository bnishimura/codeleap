from django.db import models


class Item(models.Model):
    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    # content = models.TextField()  # no text field?
    content = models.CharField(max_length=32767)  # 2^14

    # app_label="forum"

    def __str__(self):
        return self.title
