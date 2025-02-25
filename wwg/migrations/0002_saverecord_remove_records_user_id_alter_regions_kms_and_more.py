# Generated by Django 4.2.4 on 2023-08-16 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wwg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='saveRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earnedCoin', models.IntegerField(default=0)),
                ('info', models.JSONField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wwg.kakaousers')),
            ],
        ),
        migrations.RemoveField(
            model_name='records',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='regions',
            name='kms',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='Markings',
        ),
        migrations.DeleteModel(
            name='Records',
        ),
    ]
