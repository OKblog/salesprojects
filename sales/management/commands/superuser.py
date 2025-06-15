from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()
class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(account_id='your_name').exists():
            User.objects.create_superuser(
                account_id = 'your_name',
                password = 'your_password'
            )
            print("スーパーユーザー作成に成功しました")