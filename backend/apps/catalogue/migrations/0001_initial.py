# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import re
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=25)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=25)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=25)),
                ('hex_code', models.CharField(validators=[django.core.validators.RegexValidator(regex=re.compile('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', 32), message='HEX color code')], verbose_name='Color', help_text='HEX code like #000000', max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, db_index=True, verbose_name='Name', max_length=50)),
                ('description', models.TextField(verbose_name='Description')),
                ('sku', models.CharField(unique=True, db_index=True, verbose_name='SKU', max_length=20)),
                ('style', models.CharField(unique=True, db_index=True, verbose_name='Style', max_length=20)),
                ('price', models.PositiveSmallIntegerField(verbose_name='Price', default=1, choices=[(3, '$$$'), (2, '$$'), (1, '$')])),
                ('collection', models.ForeignKey(to='catalogue.Collection')),
                ('colors', models.ManyToManyField(to='catalogue.Color')),
            ],
            options={
                'verbose_name_plural': 'Dresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DressImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('original', sorl.thumbnail.fields.ImageField(upload_to='photos', verbose_name='Original')),
                ('caption', models.CharField(blank=True, verbose_name='Caption', max_length=200)),
                ('position', models.PositiveIntegerField(verbose_name='Position', help_text='An image with a first position will be the primary image for a product')),
                ('color', models.ForeignKey(to='catalogue.Color')),
                ('dress', models.ForeignKey(verbose_name='Dress', to='catalogue.Dress', related_name='images')),
            ],
            options={
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=25)),
                ('position', models.PositiveIntegerField(verbose_name='Position')),
                ('colors', models.ManyToManyField(to='catalogue.Color')),
                ('dress', models.ForeignKey(verbose_name='Dress', to='catalogue.Dress', related_name='fabrics')),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=20)),
                ('position', models.PositiveIntegerField(verbose_name='Position')),
                ('colors', models.ManyToManyField(to='catalogue.Color')),
                ('dress', models.ForeignKey(verbose_name='Dress', to='catalogue.Dress', related_name='parts')),
            ],
            options={
                'ordering': ['position'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, verbose_name='Name', max_length=50)),
                ('size_from', models.PositiveSmallIntegerField(default=0)),
                ('size_to', models.PositiveSmallIntegerField(default=24)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='fabric',
            unique_together=set([('dress', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='dressimage',
            unique_together=set([('dress', 'position')]),
        ),
        migrations.AddField(
            model_name='dress',
            name='size',
            field=models.ForeignKey(to='catalogue.Size'),
            preserve_default=True,
        ),
    ]
