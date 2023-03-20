from django.db import models
from django.utils.text import slugify
from base.models import BaseModel


def get_last_number(number):
    number = str(number)
    num = str(int(number[0]) + int(number[1]) + int(number[2]))
    num = ("%02d" % int(num))
    return(num[1])
    

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    open_entry_time = models.TimeField()
    close_entry_time = models.TimeField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name


class EntryField(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='entryfield')
    is_post = models.BooleanField(default=False)
    open = models.CharField(max_length=3)
    close = models.CharField(max_length=3)
    open_sum = models.CharField(max_length=1)
    close_sum = models.CharField(max_length=1)

    def uid_field(self, cat_name):
        field = EntryField.objects.filter(category__category_name = cat_name, is_post=False)
        return field[0]

    
    def __str__(self) -> str:
        return self.category.category_name
    

    def save(self, *args, **kwargs):
        if self.open == '***' and self.close == "***":
            self.open_sum = '*'
            self.close_sum = '*'
            super(EntryField, self).save(*args, **kwargs)
        try:
            if self.open is not None:
                self.open_sum = get_last_number(self.open)
                super(EntryField, self).save(*args, **kwargs)
            if self.close is not None:
                self.close_sum = get_last_number(self.close)
                super(EntryField, self).save(*args, **kwargs)
        except Exception as e:
            print(e)

        else:
            print()