from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=)e#qx!7h4cd0$vhzp7$qj*-o_gt$uyf@fk&nnf)on0qt=610b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # MS4 Apps
    'accounts',
    'home',
    'calculator',
    'projects',
    'donations',

    # Other apps
    'crispy_forms',
    'allauth',
    'allauth.account',
    'rest_framework',
    
    # Enable sign up with social accounts
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# Using postgres as development db, as seems recommended as best practice
# Setup based on Django for Professionals, p41

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# Static setup based on Django for Professionals
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),) #Development location
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles')) #Production location
STATICFILES_FINDERS = [ 
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Use CustomUser
AUTH_USER_MODEL = 'accounts.CustomUser'

# Additional Requirements and Configuration
CRISPY_TEMPLATE_PACK = 'bootstrap4' # Bootstrap add-in for crispy forms

# Settings for allauth
LOGIN_REDIRECT_URL = 'home:index'
ACCOUNT_LOGOUT_REDIRECT = 'home:index' 
SITE_ID = 1 # For allauth/django sites
ACCOUNT_SESSION_REMEMBER = True # Remove the default allauth 'remember me' checkbox
ACCOUNT_USERNAME_REQUIRED = True #Make the username a required field for signup
ACCOUNT_AUTHENTICATION_METHOD = 'email' # Make email the path for authenticating sign up
ACCOUNT_EMAIL_REQUIRED = True # Make email a required field for sign up
ACCOUNT_UNIQUE_EMAIL = True #Email cannot be used for more than one account
ACCOUNT_EMAIL_VERIFICATION = 'none' #Verification email is sent but not verification not required for login
ACCOUNT_SIGNUP_REDIRECT_URL = 'home:index'



AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', #Default django
    'allauth.account.auth_backends.AuthenticationBackend', # Allauth
)

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # Use console temporarily to output emails
SENDGRID_API_KEY = env('SENDGRID_API_KEY')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY

# Stripe
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY')
STRIPE_WH_SECRET = env('STRIPE_WH_SECRET')
#STRIPE_CURRENCY = 'eur'

#S3 Media Storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False