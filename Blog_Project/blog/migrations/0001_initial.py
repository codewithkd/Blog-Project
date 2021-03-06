# Generated by Django 4.0.1 on 2022-02-22 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_Title', models.CharField(max_length=200)),
                ('Date_Posted', models.DateField(auto_now_add=True)),
                ('Blog_Image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Blog_Body', models.TextField()),
                ('User_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
