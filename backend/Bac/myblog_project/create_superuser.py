from django.contrib.auth import get_user_model
User = get_user_model()
username = 'admin'
email = 'admin@example.com'
password = 'Admin1234!'
if User.objects.filter(username=username).exists():
    print('SUPERUSER ALREADY EXISTS')
else:
    User.objects.create_superuser(username, email, password)
    print('SUPERUSER CREATED')
