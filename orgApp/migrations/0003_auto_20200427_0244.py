# Generated by Django 3.0.4 on 2020-04-26 20:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orgApp', '0002_organisation_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgApp.City')),
            ],
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='district',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='orgproject',
            old_name='area',
            new_name='organization_name',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='division',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='thana',
        ),
        migrations.RemoveField(
            model_name='orgproject',
            name='image',
        ),
        migrations.AddField(
            model_name='orgproject',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='orgproject',
            name='selected_area',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organisation',
            name='postal_area',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='orgdetail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='orgdetail',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgApp.District')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgApp.Country'),
        ),
    ]
