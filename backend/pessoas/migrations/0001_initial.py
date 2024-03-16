# Generated by Django 4.1.7 on 2023-02-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('data_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=255)),
                ('altura', models.DecimalField(max_digits=5, decimal_places=2)),
                ('peso', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
    ]