import random
from django.utils.text import slugify

def slugify_instance_title(instance, save=False, newSlug=None):
    rand_int = random.randint(100_000, 900_000)
    if newSlug is None:
        slug = slugify(instance.title)
    else:
        slug = newSlug
    qs = instance.__class__.objects.filter(slug=slug).exclude(id=instance.id)

    if qs.exists():
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance, save=save, newSlug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance
