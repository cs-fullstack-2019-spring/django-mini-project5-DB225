# Generated by Django 2.0.6 on 2019-03-11 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniApp', '0002_userloginmodel_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipesmodel',
            name='recipeForeignKey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniApp.UserLoginModel'),
        ),
    ]
