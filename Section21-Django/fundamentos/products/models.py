from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    slug = models.SlugField()
    banner = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Product(\n"
            f"  id={self.id},\n"
            f"  name='{self.name}',\n"
            f"  description='{self.description}',\n"
            f"  price={self.price},\n"
            f"  stock={self.stock},\n"
            f"  slug='{self.slug}',\n"
            f"  banner='{self.banner}',\n"
            f"  created_at='{self.created_at}'\n"
            f")"
        )
