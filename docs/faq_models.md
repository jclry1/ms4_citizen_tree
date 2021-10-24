
[Back to README](../README.md#design---database)

The faq model holds the content for the FAQs that a user accesses at the bottom of the calculator page. These are served using fetch (asynch) and the Django Rest Framework (the API endpoints from which fetch retrieves the data are set up using the Django Rest Framework (DRF)).

![FAQ Model](/docs/readme_images/faq_model.png)

The following resources served as guidance for setting up DRF and fetch:

DRF:
* https://howtocreateapps.com/fetch-and-display-json-html-javascript/
* https://stackoverflow.com/questions/66318099/passing-django-model-properties-to-javascript-with-the-fetch-api
* https://www.pluralsight.com/guides/work-with-ajax-django
* https://www.geeksforgeeks.org/render-a-html-template-as-response-django-views/
* https://www.youtube.com/watch?v=DG4obitDvUA&list=PLBMLLI9khn4f1ydlbn3jsuvkf4HEmRtoX
* https://docs.djangoproject.com/en/3.2/topics/db/queries/
* https://stackoverflow.com/questions/65369567/import-rest-framework-could-not-be-resolved-but-i-have-installed-djangorestfr
* https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
* https://www.geeksforgeeks.org/textfield-django-models/
* https://www.geeksforgeeks.org/render-a-html-template-as-response-django-views/
* https://selmi.tech/post/how-to-use-ajax-in-django-using-the-javascript-fetch-api-no-jquery
* https://www.youtube.com/watch?v=263xt_4mBNc
* https://www.youtube.com/watch?v=3Qdy-FvUEcY
* https://www.django-rest-framework.org/tutorial/quickstart/
  
  Fetch:
* https://gomakethings.com/getting-html-with-fetch-in-vanilla-js/
* https://css-tricks.com/using-fetch/
* https://www.brennantymrak.com/articles/fetching-data-with-ajax-and-django.html
* https://stackoverflow.com/questions/64020495/trouble-with-fetch-from-js-to-django-view
* https://timonweb.com/django/how-to-make-django-requestis_ajax-work-with-js-fetch/
* https://stackoverflow.com/questions/58725652/inserting-data-from-fetch-into-a-html-div