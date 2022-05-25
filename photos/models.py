from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, new_url):
        try:
            self.image_link = new_url
            self.save()
            return self
        except self.DoesNotExist:
            print('Image you specified does not exist')

    @classmethod
    def get_all(cls):
        pics = Images.objects.all()
        return pics

    @classmethod
    def get_image_by_id(cls, id):
        retrieved = Images.objects.get(id = id)
        return retrieved

    @classmethod
    def search_category(cls, cat):
        retrieved = cls.objects.filter(category__name__contains=cat) #images assoc w/ this cat
        return retrieved #list of instances

    @classmethod
    def search_location(cls, nai):
        retrieved = cls.objects.filter(location__name__contains=nai) 

    @classmethod
    def filter_by_location(cls ,location):
        retrieved = Images.objects.filter(location__city__contains=location)
        return retrieved



class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

    @classmethod
    def update_category(cls, search_term , new_cat):
        try:
            to_update = Categories.objects.get(name = search_term)
            to_update.name = new_cat
            to_update.save()
            return to_update
        except Categories.DoesNotExist:
            print('Category you specified does not exist')

    

class Locations(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


    @classmethod
    def update_location(cls, search_term , new_locale):
        try:
            to_update = Locations.objects.get(country = search_term)
            to_update.city = new_locale
            to_update.save()
            return to_update
        except Locations.DoesNotExist:
            print('Location you specified does not exist')

    @classmethod
    def get_all(cls):
        cities = Locations.objects.all()
        return cities