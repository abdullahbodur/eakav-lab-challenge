from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_username_user_first_name_user_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='eth_address',
            field=models.CharField(max_length=42, blank=True, null=True),
        ),
    ]