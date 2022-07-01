# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&(*UEJDHF*&(Y#Ew&_di+struia^f2io!r*^7z+rv^$$vd5@#4r6v9pi$nb)(h3pi'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'drfjwt_tutorial_project_database',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'password',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}