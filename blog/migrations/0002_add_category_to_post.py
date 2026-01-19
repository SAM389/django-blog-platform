from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('science', 'Science'), ('history', 'History'), ('entertainment', 'Entertainment'), ('sports', 'Sports')], default='science', max_length=20),
        ),
    ]
