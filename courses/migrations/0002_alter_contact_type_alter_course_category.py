# Generated by Django 4.1.2 on 2022-10-20 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.IntegerField(choices=[(1, 'phone'), (2, 'facebook'), (3, 'email')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category'),
        ),
    ]
