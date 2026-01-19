from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_add_category_to_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('all', 'All'), ('science', 'Science'), ('history', 'History'), ('entertainment', 'Entertainment'), ('sports', 'Sports')], default='all', max_length=20),
        ),
    ]
