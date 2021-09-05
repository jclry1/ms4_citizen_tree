# Initial Setup
### Based on Django for Professinoals by William S. Vincent
Create virtual environment using pipenv
Install Django (this project uses 3.2.6 - see pipfile.lock)
Install psycopg2 for using postgres in development
Start the Django project and run the server to check - ok

Stop the virtual env.

Set up the Dockerfile and docker-compose files

Change settings so that default db is postgres and not sqlite3.

Before running migratinos, set up custom user model: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

# Set up static files
Based on:
* Django for Professionals
* Django docs
* Boutique Ado

## Problem using docker-compose to install packages
For much of the basic setup of the project, I'm following Django for Professionals by William S. Vincent. To install packages, eg Crispy Forms, he recommends the following command in the terminal:
```sh
$ docker-compose exec web pipenv install <django-crispy-forms==1.9.2>
```
I found that this did not work. The problem seems to be known but I didn't find a perfect solution.
See:
https://stackoverflow.com/questions/53400385/django-docker-and-pipenv-error-adding-new-packages
https://stackoverflow.com/questions/60949436/django-docker-and-pipenv-error-adding-new-packages-not-transfering-from-con

The command that seems to work is to remove the docker-compose element and just install using pipenv. The package gets added to the pipfile and pipfile.lock:
```sh
pipenv install django-crispy-forms
```

## Class-based generic views
I'm using some class-based generic views
Info tfor this has come from:
* Django for professionals
* Very Academy - Learn Django Class-Based View series - https://www.youtube.com/watch?v=GxA2I-n8NR8

For some issues passing context data (breaking if no user is logged in):
https://stackoverflow.com/questions/54444196/get-context-data-breaking-breaking-django-listview
https://stackoverflow.com/questions/51632952/get-the-user-id-class-based-view
https://stackoverflow.com/questions/65685752/getting-django-db-models-query-utils-deferredattribute-object-at-0x7fca8f1d3d50


## Calculator Page
The purpose of the calculator page is to give some context to the figures and emphasise the purpose of the project and the scales involved.
How it works:
The user can enter a Euro amount that they spend on transportation fuel weekly. 
Using figures from the AA re fuel price, this is converted to a litre amount of either petrol or diesel, as selected.

Using this litre amount, the CO2 emission for that amount of fuel is calculated and returned as the weekly and annual (*52) CO2 emissions arising from transport fuel usage.
Note: A future iteration of the site would have a more complete CO2 calculator (eg, food, other transport, heating etc). For the first iteration, the CO2 arising from fuel usage is relatively straightforward to calculate and it is also straightforward to isolate so it was chosen as an indicative metric.

After calculating the emissions, the user is presented with information relating to the potential sequestration arising from a donation to Citizen Tree and this is presented as a % of the fuel emission calculated previously. For example 'A 50 euro donation would amount to x trees and represent an offset of about 2% of your transport emissions.
The purpose here is to reinforce the scales involved and to serve as a call to action for the user.

To give legitimacy to the calculations and to the project, a further section outlines some background and FAQs.

Note on tech setup:
The page updates dynamically and asynchronously as the user progresses through it. The HTML is updated according to the inputs and some hard-coded HTML (template literal) in the corresponding JS functions. 
For the FAQs, the page is updated (no reload) using fetch (similar to Ajax). The API endpoints from which fetch retrieves the data are set up using the Django Rest Framework (DRF).

The following resources served as guidance for setting up DRF and fetch:
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

For calculations, the following resources were used:
#### Cost of fuel in Ireland
Info from the AA, April 2021:
https://www.theaa.ie/aa/motoring-advice/petrol-prices.aspx
Diesel: 133.8c round to 1.34
Petrol: 142.9c round to 1.43


#### Emissions from diesel/petrol
Diesel = 2600g/l
Comprises 720g C in the diesel + 1,920g O2 to combust it.

Petrol = 2300g/l
Comprises 652g C in the petrol and 1740g O2 to combust it.

Sources:
* https://www.tcd.ie/news_events/articles/are-diesel-cars-really-more-polluting-than-petrol-cars/
* https://ecoscore.be/en/info/ecoscore/co2

### Hazelnut orchards - sequestration (Italy)
https://www.researchgate.net/publication/340878646_Carbon_dioxide_sequestration_capability_of_hazelnut_orchards_daily_and_seasonal_trends
"Overall, during the year, from the structural maturation of leaves to the beginning of leaf senescence, the hazelnut
orchards, under consideration removed from the atmosphere, a total amount of CO2 equal to 58.8 ± 9.1 Mg(CO2) ha-1 year-1 (mean value), corresponding to an amount of C equal to 16.0 ± 2.5 Mg ha-1 year-1."
At 400 bushes/ha, that works out to approx 145Kg CO2/bush per year.

### Agroforestry systems
http://www.sidalc.net/repdoc/A3678i/A3678i.pdf

### Ireland:
COFORD report may be outdated: http://www.coford.ie/media/coford/content/publications/projectreports/carbonseq-Irishforests.pdf
Estimates: 1.8Mg/ha/year for oak/beech and 2.4Mg/ha per year for 'other conifers

### Planning woodland
http://woodlandsofireland.com/sites/default/files/No.%205%20-%20New%20Woodland%20Design%20%26%20Establishment.pdf

"As well as attaining conservation objectives over a shorter timeframe by accelerating canopy closure, closer spacings (e.g. 2.0 m x
2.5 m to give 2000 stems/ha) will also result in less follow-up maintenance, especially vegetation control (Fig. 5)."
 => 2000 trees/ha)

Donation conversion to trees = 50euro: 20 trees
 = 1% of a ha.
 
### UK 
https://cieem.net/wp-content/uploads/2021/05/Carbon-and-habitats-paper-v3.pdf


### Calculator example
https://standfortrees.org/footprint-calculator/?utm_source=google&utm_medium=cpc&utm_term=carbon%20footprint%20calculator&utm_campaign=NPM-SFT-FootprintCalculator&gclid=CjwKCAjw092IBhAwEiwAxR1lRosb5bShmxL5amr2H6RkgMF_I_Q7j-u6rCOfSkmzhIwmxH9Vf1bdaxoCEA4QAvD_BwE#calculator

