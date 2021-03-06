# Generated by Django 3.2.9 on 2021-11-27 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('zipcode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='SelfAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.CharField(choices=[('fever', 'fever'), ('cold', 'cold'), ('cough', 'cough')], max_length=5)),
                ('travelHistory', models.BooleanField()),
                ('contactWithCovidPatient', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserModule.user')),
            ],
        ),
    ]
