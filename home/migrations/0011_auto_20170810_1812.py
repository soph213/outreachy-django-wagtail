# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 18:12
from __future__ import unicode_literals

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170808_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('logo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('date', wagtail.wagtailcore.blocks.DateBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('quote', wagtail.wagtailcore.blocks.RichTextBlock())]),
        ),
    ]
