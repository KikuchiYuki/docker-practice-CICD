# Generated by Django 4.2 on 2024-06-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タスク名')),
                ('description', models.TextField(blank=True, null=True, verbose_name='詳細')),
                ('complite', models.IntegerField(default=0, verbose_name='完了フラグ')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='開始日')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='終了日')),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]
