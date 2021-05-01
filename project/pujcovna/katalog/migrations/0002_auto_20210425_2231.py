# Generated by Django 3.2 on 2021-04-25 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vratka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vuz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('znacka_typ', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='vuz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.vuz'),
        ),
        migrations.AddField(
            model_name='vypujcka',
            name='vratka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.vratka'),
        ),
        migrations.AddField(
            model_name='vypujcka',
            name='vuz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.vuz'),
        ),
        migrations.AddField(
            model_name='zakaznik',
            name='vratka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.vratka'),
        ),
    ]