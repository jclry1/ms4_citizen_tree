## Using Class-Based Views

For handling information on projects and project updates, I'm using class-based views.
These are integrated with dynamic URLS using get_absolute_url and dynamic filtering of content using foreign keys and get_queryset.

The main resources for putting this in place (with some code snippets used) were:
* [Django documentation - get_queryset()](https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects)
* [Django documentation - get_absolute_url](https://docs.djangoproject.com/en/3.2/ref/models/instances/)
* [Django documentation - ForeignKey](https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey)
* [URL Mapping](https://www.youtube.com/watch?v=YT60BZJjySg)
* [get_absolute_url -- GoDjango](https://www.youtube.com/watch?v=dv1Sm2Rlyao)
* [Class-Based Views - Very Academy](https://www.youtube.com/watch?v=RwWhQTSV44Q&list=PLBMLLI9khn4ewoLazztY1eepWFCvujPB9&index=7&t=1024s)
* [Slug Field](https://learndjango.com/tutorials/django-slug-tutorial)
* [List and Detail Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
* [Model Queries](https://www.youtube.com/watch?v=WimXjp0ryOo)
* [self.request.user as filter for class-based view](https://stackoverflow.com/questions/38471260/django-filtering-by-user-id-in-class-based-listview)