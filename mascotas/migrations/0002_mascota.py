# Generated by Django 3.2.11 on 2022-02-08 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='mascotas')),
                ('fecha_rescate', models.DateField()),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.persona')),
                ('vacunas', models.ManyToManyField(to='mascotas.Vacuna')),
            ],
        ),
    ]
