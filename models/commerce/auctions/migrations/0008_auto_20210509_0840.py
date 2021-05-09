# Generated by Django 3.2 on 2021-05-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='auctions.category'),
        ),
    ]
