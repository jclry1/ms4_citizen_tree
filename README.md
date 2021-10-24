# Citizen Tree <!-- omit in toc -->
Citizen Tree is an online space to foster networks of people interested in growing trees from seed through to woodland. 

<a href="https://ms4-citizen-tree.herokuapp.com/" target="_blank">View the live project here</a>

# Table of Contents <!-- omit in toc -->  
- [Scenario Outline / Strategy](#scenario-outline--strategy)
- [User Experience](#user-experience)
  - [User Stories by User Type](#user-stories-by-user-type)
      - [Non-Registered Visitor](#non-registered-visitor)
    - [Registered Non-Contributing User](#registered-non-contributing-user)
    - [Registered Contributing User](#registered-contributing-user)
    - [Admin/Site-Owner](#adminsite-owner)
- [Design - UI](#design---ui)
    - [Additional Design Notes](#additional-design-notes)
- [Design - Database](#design---database)
      - [Using the CustomUser Model](#using-the-customuser-model)
- [Features](#features)
  - [Admin perspective](#admin-perspective)
    - [Email Verification](#email-verification)
    - [User Image Upload](#user-image-upload)
    - [Donations with Stripe](#donations-with-stripe)
  - [Technical Info](#technical-info)
    - [Initial Setup based on Django for Professinoals by William S. Vincent](#initial-setup-based-on-django-for-professinoals-by-william-s-vincent)
  - [Set up static files](#set-up-static-files)
  - [Problem using docker-compose to install packages](#problem-using-docker-compose-to-install-packages)
  - [Class-based generic views](#class-based-generic-views)
  - [Calculator Page](#calculator-page)
  - [Stripe](#stripe)
  - [Git](#git)
  - [Development](#development)
      - [Why not use Gitpod?](#why-not-use-gitpod)
      - [Resources on Docker, Docker Compose, and Pipenv](#resources-on-docker-docker-compose-and-pipenv)
      - [Installing Docker](#installing-docker)
      - [Setting up the Virtual Environment and Managing Dependencies](#setting-up-the-virtual-environment-and-managing-dependencies)
      - [Using Docker Compose](#using-docker-compose)
  - [Deployment](#deployment)
      - [Note on Procfile](#note-on-procfile)
      - [Environment Variables](#environment-variables)
      - [Staticfiles](#staticfiles)
      - [WSGI](#wsgi)
      - [Heroku as Allowed Host](#heroku-as-allowed-host)
      - [Heroku.yml](#herokuyml)
      - [Create the app in Heroku:](#create-the-app-in-heroku)
      - [Pushing Code](#pushing-code)
  - [Run the App Locally](#run-the-app-locally)
      - [Environment Variables](#environment-variables-1)
      - [Forking](#forking)
  - [Credits](#credits)
    - [Shop App](#shop-app)
    - [Projects App](#projects-app)
    - [Donations App](#donations-app)
    - [Initial Project Setup and Allauth](#initial-project-setup-and-allauth)
    - [Environment variables](#environment-variables-2)
    - [Stripe CLI and Payments](#stripe-cli-and-payments)
  - [Acknowledgements](#acknowledgements)
  - [Disclaimer](#disclaimer)



# Scenario Outline / Strategy
The intended user of Citizen Tree falls broadly into one of three posible categories:
1. User with time and interest in growing trees but no space/land to do so.
   An example of this might be a school. As part of their learning about climate change, biodiversity etc, kids are introduced to the value of trees. Perhaps they visit a local forest on occasion. The kids would be interested in contributing to a tree-growing project but the school has no land to facilitate that. However, they do have space for 2-3 raised beds in which the kids could grow seeds to the seedling or one-year-old stage.At that point they would need to partner with a landowner to get those trees planted into a space where they could grow to maturity.
   Other potential users in this category might be individuals with small (or large) gardens, community groups, allotment groups, retirement groups, mens sheds etc.
2. User with space/land to grow trees but in need of help and/or trees. 
   The other side of the coin is the person or institution who owns some land and would like to have it planted with trees and are interested in community engagement. Maybe they don't have enough land to justify a commercial approach or perhaps they are just not interested in becoming commercial forestry owners. Rather they would be happy for a group of interested people to come and plant the land with them, for free, and provide the trees for free. It might also suit a company who has a land bank and sees the opportunity for devloping a positive profile using the partnerships facilitated bythe site.
3. A user who is interested in the aims of theproject and wishes to support it by making a donation or purchasing trees for their own use.

The site aims to help foster connections between people in the first two categories so that land might get planted and long-standing relationships might develop to help manage the trees and enjoy the spaces they create.

It also has a donation page where supporters can support the project financially and a shop where users can buy a specific subset of trees grown at project sites.

# User Experience
Users envisaged for the site are as follows:
* An admin superuser who can see and edit all content on the site. When a new project joins, it must be set up in the Django Admin by an admin user.This person is also required to give authoring rights to the designated 'author' for a project. This user is essentially the site owner and in a real world scenario would work together with a board to decide how donations were spent, whether requesting projects would be invited to join etc.
* The admin user is also responsible for adding products tot he site shop absed on real-world info and for setting initial stock numbers and prices.
* A project coordinator/author who is responsible for maintaing the information for a project - whether the project details page or periodic updates for the project progress. The rights associated with this user are limited to authoring for a specified subset of projects and cannot be self-assigned.
* A general user with read-only access. Although this user may be registered with the site, and may be a member of a project that is affiliated with the site, they do not have authoring or upload rights. They can make donations, use the shop, and view all content.
* A non-registered visitor has limited access. In order to make a donation or check out from the shop, users are required to register. A non-registered visitor can use the calculator app without restriction.


## User Stories by User Type

#### Non-Registered Visitor
* As a first-time or non-registered vistor to the site, I have access to the content but I cannot make a donation.
However, as an enticement to register and to set up a degreee of trust in the site and establish the scientific basis for the site's aims:
* I can interact with the CO2 calculator and get a sense of my personal CO2 emission (currently from transport fuel only) and how this might be counter-balanced by trees.
* I can clearly get a sense of the sites aims.
* I can add items from the shop to my cart but cannot check out without registering.
  
### Registered Non-Contributing User
* I can access any content that is available to a non-registered user.
* In addition, I can use the shop and make donations.

### Registered Contributing User
* I have access to all content that a non-registered user has. 
* If my user has been designated the 'author' for one or more projects, I can update the information for a project and and can add or delete updates (no edit option for project updates).

### Admin/Site-Owner
The interaction of this user with the site assumes integration with offline processes. For example, potential projects need to be vetted in person. Assuming this is all in place, the main points in relation to site use are:
* I can add a project and assign an 'author' - the designated person for a project to edit the project details page and add project updates.
* I can access information about donations.
* I can add products to the shop and edit price and stock information.
* I can view order information and payment status with a view to order fulfillment.
* I can edit or delete any project or update content.

# Design - UI
Wireframes and initial mockups:

* [Desktop](docs/MS4_Desktop.pdf)
* [Mobile](docs/MS4_Mobile.pdf)
* [Initial Outline](docs/MS4Draft_InitialOutline.pdf)

### Additional Design Notes
The aim is to maintain an 'earthy' look and feel to the site. The same background image is used throughout and colours for bottons and the background for project inof etc pick up on the greens and browns that would be familiar from a forest or farm setting.
Further input on the look and feel would be on the list of to-dos for the first update.

# Design - Database

The models used on the different apps interact across the project as a whole. For ease of reading, I have separated out the most important models per app:

* [FAQ model in the calculator app, plus resource info on DRF and fetch](/docs/faq_models.md)
* [Shop-related models](/docs/shop_models.md)
* [Project-related models](/docs/projects_models.md)
* [Donations-related models](/docs/donations_models.md)


#### Using the CustomUser Model
The Django docs explicitly recommend using a custom user model: "If you’re starting a new project, it’s highly recommended to set up a custom user model, even if the default User model is sufficient for you."
This advice was echoed in Django for Beginners and Django for Professionals books and I went with it. In retrospect, for this project I think it was a bad idea and if I were to start over, I think I would use the default user model.
Main resources on setting up and using the custom user model:

* [Django for Professionals](https://djangoforprofessionals.com/) book by William S. Vincent
* [Django Docs](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)
* [Django Best Practices: Referencing the User Model](https://learndjango.com/tutorials/django-best-practices-referencing-user-model)

Using it did not really bring any benefit and there was a small extra overhead when trying to figure out how to access the user. Resources consulted at various points for this are commented in the code.


# Features
(For testing, go to [Testing](/docs/testing.md))

## Admin perspective
It is easy for users to register with the site using an email and password or some level of social authentication (currently GitHub only).
It is not possible for an email account to be associated with 2 users.
Donation functionality on the site is user-friendly and professional. In addition to the success page, users get an email when their donation has been processed, but not before.

### Email Verification
Based on the functionality provided by django-allauth and the direction in 'Django for Professionals'
all-auth email templates: https://github.com/pennersr/django-allauth/tree/master/allauth/templates/account/email
all-auth settings: https://django-allauth.readthedocs.io/en/latest/configuration.html

Password reset functionality based on django-allauth and uses the allauth templates only slightly modified:
https://github.com/pennersr/django-allauth/tree/master/allauth/templates/account
Additional resource: https://www.youtube.com/watch?v=d9aCpxQfnOg

### User Image Upload
Image upload is available for users who are designated as the 'author' for a project. The option is part of the form when editing the project details or adding a new update.
Images uploaded by users in this way are stored and served from an Amazon S3 bucket.
![S3 Image Storage](/docs/readme_images/s3_image_storage.png)

### Donations with Stripe
The app uses Stripe to take donations payments. Options are limited to 3 donation levels and a user must be logged in to access the donate page.
The payment process can be cancelled by a user in which case they are redirected to a cancel page. Otherwise, when they commit to the payment, they are redirected to a success page.
In addition to the success page that confirms the amount they have paid, the user is also sent an email from the app to confirm the payment.
This email only issues after the payment has been successful. This is implemented using a webhook:
```python
@csrf_exempt
def stripe_webhook(request):
  endpoint_secret = settings.STRIPE_WH_SECRET
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event - send confirmation email
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']
    customer_email = session["customer_details"]["email"]
    amount = session["amount_total"]
    display_amount = "{0:.2f}".format(amount / 100)

    print(session)
    send_mail('Your donation', f'Thank you for your donation of {display_amount} euros to Citizen Tree.', 'ms4.citizentree@gmail.com', [customer_email], fail_silently=False)

```
The email is sent using SendGrid.

## Technical Info
### Initial Setup based on Django for Professinoals by William S. Vincent
Create virtual environment using pipenv
Install Django (this project uses 3.2.6 - see pipfile.lock)
Install psycopg2 for using postgres in development
Start the Django project and run the server to check - ok

Stop the virtual env.

Set up the Dockerfile and docker-compose files

Change settings so that default db is postgres and not sqlite3.

Before running migrations, set up custom user model: https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

## Set up static files
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
I'm using mostly class-based views in the project.
For the Projects app, info for this has come from:
* Django for professionals
* Very Academy - Learn Django Class-Based View series - https://www.youtube.com/watch?v=GxA2I-n8NR8

Other Resources included:
For some issues passing context data (breaking if no user is logged in):
https://stackoverflow.com/questions/54444196/get-context-data-breaking-breaking-django-listview
https://stackoverflow.com/questions/51632952/get-the-user-id-class-based-view
https://stackoverflow.com/questions/65685752/getting-django-db-models-query-utils-deferredattribute-object-at-0x7fca8f1d3d50

Also, class-based edit views.
Resources for DeleteView:
https://www.codingforentrepreneurs.com/projects/try-django/class-based-views-deleteview
https://www.geeksforgeeks.org/deleteview-class-based-views-django/
https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#django.views.generic.edit.DeleteView

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

Additional information on the assumptions used for the calculation and relevant resources are here.


## Stripe
Stripe integration is based on:
* Boutique Ado
* Stripe docs
* JustDjango tutorial: https://justdjango.com/blog/django-stripe-payments-tutorial and https://www.youtube.com/watch?v=722A27IoQnk
* testdriven.io tutorial: https://testdriven.io/blog/django-stripe-tutorial/
* re session object: https://stripe.com/docs/api/checkout/sessions/line_items
* https://bhoey.com/blog/stripe-checkout-with-django/

## Git
Branching and merging: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

## Development
in contrast with the my previous milestone projects, this project was developed lcally using VSCode and Docker Compose (as opposed to GitPod).
This hasd knock-on effects for deployment, installation, dependency management.

#### Why not use Gitpod?
Gitpod had served well for the three milestone projects so far. I decided to switch to using VS Code locally in combination with Docker Compose for a couple of reasons:

* To expand my learning in relation to handling a development environment.
* Docker seemed like a useful technology/tool to become familiar with.
* When I started the MS4 project, I misjudged the time I had available.

All in all I think it was a good decision but it did add an additional load on the learning required to complete the project. 

#### Resources on Docker, Docker Compose, and Pipenv
For information on installing and using Docker and Docker Compose, I relied on these primary resources:

* [Django for Professionals](https://djangoforprofessionals.com/) book by William S. Vincent
* [Dive into Docker](https://nickjanetakis.com/courses/#dive-into-docker) online course by Nick Janetakis
* [Virtual Environment Setup](https://djangoforbeginners.com/initial-setup/) 
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

#### Installing Docker
To install Docker, I followed the steps outlined in the [Docker documentation](https://docs.docker.com/engine/install/ubuntu/).

To install Docker Compose, I followed the steps [here](https://docs.docker.com/compose/install/)
The versions used are: 

![Docker](/docs/readme_images/docker_verify_install.png)

#### Setting up the Virtual Environment and Managing Dependencies
Pipenv was used to install and manage dependencies (e.g. Django itself, crispy forms etc), using the following command:
```shell
pipenv install django
```
Because I used Pipenv, the ```requirements.txt``` file is replaced by ```Pipfile``` and ```Pipfile.lock```. Pipfile lists the dependencies and Pipfile.lock includes the versions used so that an exact repica of the development environment can be created. These files are updated automatically by Pipenv whenever a new package is installed.

Resources on using Pipenv included:
* [Django for Professionals](https://djangoforprofessionals.com/) book by William S. Vincent
* [pypi.org](https://pypi.org/project/pipenv/2021.5.29/)
* [Pipenv docs](https://pipenv.pypa.io/en/latest/)
* [Real Python](https://realpython.com/pipenv-guide/) 

#### Using Docker Compose
Once the project was set up, all manage.py commands were run via docker-compose, using the following pattern (using makemigrations for the projects app as example):
```sh
docker-compose exec web python manage.py makemigrations projects
``` 

Command to start the local server:
```sh
docker-compose up
```
OR
```sh
docker-compose up -d
```
The difference bewtween the two commands above being the terminal output was disabled with the ```-d``` flag.

## Deployment
The follwing subsections onutline the deployment process followed for this project.

#### Note on Procfile
As mentioned above, the project was deloped on VS Code locally (as opposed to GitPod) and uses Docker Compose.
For that reason, as well as there being no requirements.txt file, there is also no Procfile. This is replaced with a .yml file: ```heroku.yml```.
```heroku.yml``` is to the production build what the docker-compose file is to the development build. It sets some initial patameters and indicates the Dockerfile to be built.

#### Environment Variables
Assumption throughout the process below is that all secret keys are stored in environment variables (.env file) and these are replicated in Heroku's config vars once the Heroku app is set up.
The following secret keys are required in Heroku:

![Heroku Config Vars](/docs/readme_images/heroku_config_vars.png)

An example of how these are maintained in settings.py:

![Settings Secret Keys](/docs/readme_images/secret_keys_settings_py.png)

#### Staticfiles
Staticfiles are handled using WhiteNoise.
To enable this, install WhiteNoise using the instructions [here](http://whitenoise.evans.io/en/stable/).
During deployment, I had issues with staticfiles. The current setting in settings.py is working fine and commented with link to related stackoverflow.

#### WSGI
For WSGI, install [Gunicorn](https://docs.gunicorn.org/en/stable/).

#### Heroku as Allowed Host
Add '.herokuapp.com' to allowed hosts in the app settings.py:
```
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.herokuapp.com']
```
#### Heroku.yml
Create a [heroku.yml](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml#heroku-yml-overview) file for deploying with Docker:
In the case of this app:
```sh
setup:
  addons:
  - plan: heroku-postgresql
build:
  docker:
    web: Dockerfile
release:
  image: web
  command:
    - python manage.py collectstatic --noinput
run:
  web: gunicorn config.wsgi
  ```

#### Create the app in Heroku:

![Heroku Setup](/docs/readme_images/heroku_app_info.png)

Basically, the steps are:
1. Log in to your Heroku account.
2. Choose *New -> Create New App*.
3. Enter an app name.
4. Choose the region.
5. Make sure the Stack option is set as 'Container'. 
   If it is not possible to set this when setting up the app in the dashboard, you can do so using the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install). When you have the Heroku CLI connected, the following command will set the stack:
   ```
  heroku stack:set container -a <app name>
   ```
6. Click *Create App*.

Once this is in place, you can set the required config vars mentioned above.

#### Pushing Code
Once the above settings are in place, there are two ways to push code and deploy the app. Both have been used for this project (mostly GitHub manual deploys).

1. Connect the heroku app with the corresponding GitHub repository and deploy the latest code from the Heroku dashboard. This can be set up to run every time new code is pushed to GitHub. I did not use this option as it seemed a needless repetition of redeploying the app for minor changes. Rather I used the manual deploy option.
This is convenient as it also allows deployment of a branch. In a few cases, this allowed changes can be checked before merging into the main/master branch.
![GitHub Connected](/docs/readme_images/heroku_github_connect.png)

2. The alternative to using GitHub is to connect a [git repository on heroku](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote) itself.

Note: A prereqiusite for this is to have the [Heroku CLI installed](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

The connection from the local git with Heroku is established with the following command:

```sh
heroku git:remote -a <app-name>
```

Once that is set up, committed code can be deployed directly to heroku using:
```sh
git push heroku master
```

When changes are made locally, they cam be pushed to heroku directly or via GitHub.

In either case, heroku rebuilds the app and deploys the updated version automatically.


## Run the App Locally
To download the code and open it in your own IDE, do the following steps. Note, these steps assume the use of VSCode. They might differ depending on the IDE.
1. On the repository home page on Github, find the download code button above the table with the commit history and open the dropdown menu.
2. Choose *Download ZIP*.
3. Locate the download in the *Downloads* folder on your computer and store it in a suitable dedicated folder.
4. Extract the ZIP.
5. Open the project files from your IDE. For example, if using VSCode, choose *File* -> *Open Folder* and choose the folder just created in step 4.
6. Outside of your IDE donload and install Docker and Docker Compose.
7. Verify your installation by checking the version. In the terminal:
   ```
   docker-compose --version
   ```
   ```
   docker --version
   ```
8. Go back to your opened folder in VSCode.
9. Verify that the project files are present and that there is a docker-compose.yml file present.
10. In the terminal inside VSCode, verify that you are located in the correct folder and type the following command:
    ```sh
    docker-compose up
    ```
11. This should call the docker-compose.yml file which will in turn call the Dockerfile. It will take a little time while the dependencies are installed.
12. the ```docker-compose up``` command is equivalent to running the server. You can now use manage.py commands by prefacing them with ``` docker-compose exec web```. For example, ```docker-compose exec web python manage.py createsuperuser```
13. To stop the server: ``` docker-compose down```
    
#### Environment Variables
Secret keys have not been pushed to GitHub so will not be included in athe downloaded ZIP. Without these, the app will not run. You would need to create an alternative set of valid environment variables (see above re config vars).


#### Forking
If you have a Github account, you can fork the repository to your own account. This will create a copy with which you can then work.
Provisos remain regarding environment variables and Docker. I have not tested how this might work (or not).

Full deatils about forking a Github repository can be found here: https://docs.github.com/en/github/getting-started-with-github/fork-a-repo

## Credits
Aspects of this project rely heavily on the following resources:

### Shop App
The shop app is based on, and closely follows, the 'Business Logic' and 'Stripe' parts of the Just Django tutorial on building an ecommerce site. The [tutorial can be found here](https://learn.justdjango.com/roadmaps/django-advanced) and this is the [corresponding GitHub repository](https://github.com/justdjango/django-simple-ecommerce).

Although I followed the tutorial closely, some aspects were removed and others added. For example, I have not included hte functionality to remember cards and I have added:

* Add in the buyer's (user) email address to the Stripe payment intent so that a receipt can be sent.
* Updating the stock of products based on successful payments.

Obviously, variable names and model fields have also changed as appropriate to the MS4 project.

### Projects App
The projects app relies on class-based views and the background for using these was taken primarily from the Very Academy YouTube channel.

The class-based views are integrated with dynamic URLS using get_absolute_url and dynamic filtering of content using foreign keys and get_queryset.

The main resources for putting this in place (with some code snippets used) were:
* **NB [Class-Based Views - Very Academy](https://www.youtube.com/watch?v=RwWhQTSV44Q&list=PLBMLLI9khn4ewoLazztY1eepWFCvujPB9&index=7&t=1024s)
* [Django documentation - get_queryset()](https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#generic-views-of-objects)
* [Django documentation - get_absolute_url](https://docs.djangoproject.com/en/3.2/ref/models/instances/)
* [Django documentation - ForeignKey](https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey)
* [URL Mapping](https://www.youtube.com/watch?v=YT60BZJjySg)
* [get_absolute_url -- GoDjango](https://www.youtube.com/watch?v=dv1Sm2Rlyao)
* [Slug Field](https://learndjango.com/tutorials/django-slug-tutorial)
* [List and Detail Views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
* [Model Queries](https://www.youtube.com/watch?v=WimXjp0ryOo)
* [self.request.user as filter for class-based view](https://stackoverflow.com/questions/38471260/django-filtering-by-user-id-in-class-based-listview)

Re the CreateView and autopopulating the author field with the logged in user:
https://stackoverflow.com/questions/55556165/setting-model-user-to-request-user-with-createview-in-django-returns-null-value

### Donations App
The donations app and inparticular setting up the webhook, rely heavily on the following resources (including some code):
* Stripe documentation eg: https://stripe.com/docs/payments/checkout/fulfill-orders
* Tutorial 1: https://testdriven.io/blog/django-stripe-tutorial/
* Tutorial 2: https://justdjango.com/blog/django-stripe-payments-tutorial

### Initial Project Setup and Allauth
Project set up, social login, using the CustomUser relies heavily on:
* Django for Beginners and Django for Profesinals books by William S. Vincent, together with the sister website [here](https://learndjango.com/). 

### Environment variables
https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f
https://djangocentral.com/environment-variables-in-django/

### Stripe CLI and Payments
Stripe CLI:
https://github.com/stripe/stripe-cli/wiki/installation
https://stackoverflow.com/questions/66217436/gpg-keyserver-receive-failed-no-name/68132500#68132500?newreg=b9ece6b73bdf4fe9aa656a6ff3f4af44
https://githubmemory.com/repo/stripe/stripe-cli/issues/689

Payments:
https://www.youtube.com/watch?v=722A27IoQnk
https://stripe.com/docs/payments/integration-builder


## Acknowledgements
I would like to acknowledge the following contributions to the project:
* My mentor Antonio Rodriguez for his guidance
* Tutor support (Sheryl and Michael) for their help with resolving an issue with JavaScript/StaticFiles.
 
 (See Credits section above for code sources and references)

## Disclaimer
This project is for educational purposes only. 