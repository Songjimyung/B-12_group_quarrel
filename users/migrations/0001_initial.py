# Generated by Django 4.2 on 2023-05-09 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=50, verbose_name='사용자 이름')),
                ('date_of_birth', models.DateField(verbose_name='생일')),
                ('gender', models.CharField(choices=[('M', '남성'), ('F', '여성')], default='unknown', max_length=5, verbose_name='성별')),
                ('profile_photo', models.ImageField(upload_to='', verbose_name='프로필 사진')),
                ('subscript', models.TextField(verbose_name='자기소개')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='가입 날짜')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]