# Generated by Django 4.0.1 on 2022-05-28 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PollQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(max_length=122)),
                ('que_text', models.TextField()),
                ('que_image', models.ImageField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField(null=True)),
                ('choice_image', models.ImageField(null=True, upload_to='')),
                ('votes', models.IntegerField(default=0)),
                ('poll_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PollApp.pollquestion')),
            ],
        ),
    ]
