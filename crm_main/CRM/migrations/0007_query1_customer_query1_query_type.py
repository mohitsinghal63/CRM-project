# Generated by Django 4.0.3 on 2022-04-06 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0006_rename_query_query1'),
    ]

    operations = [
        migrations.AddField(
            model_name='query1',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRM.customer'),
        ),
        migrations.AddField(
            model_name='query1',
            name='query_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRM.detail'),
        ),
    ]
