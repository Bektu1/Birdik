from django.db import models

class TravelItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='travel_images/')
    tour_date = models.DateField()

    def __str__(self):
        return self.name


class Review(models.Model):
    travel_item = models.ForeignKey(TravelItem, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.travel_item.name} by {self.author}"


