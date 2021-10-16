from core.models import Blog


b = Blog(name='Beatles', tagline='A;; the latest Beatles news.')
b.save()

b.name = 'New name'
b.save()