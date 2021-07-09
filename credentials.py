DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "awxpass",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "RzZXckcyYWw1elpwbWRTWGlKNGpoY2c2LklLYzhVZjpqZFNYOmF4X3lIOm5hTnZqM21mLVNhLkJxMUt0ZTFOckVSX2hCLWNwR0Q0Um5wT2EuNzpwaW1leEJMWkJ4bUhPWnlLOXIwOnRGbmdjN3dmN0tWbHhmOU5BUmxsSC0tbmg="
