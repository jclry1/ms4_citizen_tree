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

Re the CreateView and autopopulating the author field with the logged in user:
https://stackoverflow.com/questions/55556165/setting-model-user-to-request-user-with-createview-in-django-returns-null-value

Re requiring login:
https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-loginrequired-mixin



## Environment variables
https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f
https://djangocentral.com/environment-variables-in-django/


## Stripe
Stripe CLI:
https://github.com/stripe/stripe-cli/wiki/installation
https://stackoverflow.com/questions/66217436/gpg-keyserver-receive-failed-no-name/68132500#68132500?newreg=b9ece6b73bdf4fe9aa656a6ff3f4af44
https://githubmemory.com/repo/stripe/stripe-cli/issues/689

Payments:
https://www.youtube.com/watch?v=722A27IoQnk
https://stripe.com/docs/payments/integration-builder
