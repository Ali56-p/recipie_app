# Generated by Django 5.0.6 on 2024-07-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_page_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='student_Rollno',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='student_course',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='student_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='student_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
