# Mini challenge 1Create the initial setup for our new blog application.
1. Create a new djangoproject within this folder.2. Create the following apps:
  2.1. pages
  2.2. posts
  2.3. accounts
3. Install your apps.
4. Create a model for posts (see below).
5. Make migrations.
6. Migrate.
7. Create a ListView, DetailView and CreateView for our new Post model.
8. Create 2 views for our pages app.
  8.1. Your home page view.
  8.2. An about us page.
9. Create url patterns to ensure everything works as expected (from the end user perspective).

Post model:
```
class Post(model.Model):
  title = models.CharField(max_length=128)subtitle = models.CharField(max_length=128)author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
    )
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
```