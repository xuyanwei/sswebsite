# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name=b'e-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gamebigleixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gameleixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Gameshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_time', models.DateTimeField()),
                ('game_vs', models.CharField(max_length=50)),
                ('game_important', models.BooleanField()),
                ('game_leixin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Gameleixin')),
            ],
            options={
                'ordering': ['game_time'],
            },
        ),
        migrations.CreateModel(
            name='Important',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('important', models.CharField(default=b'*', max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Jijin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outside', models.BooleanField()),
                ('addr_pc', models.CharField(max_length=1000)),
                ('addr_mobi', models.CharField(max_length=1000)),
                ('addr_ss', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=30)),
                ('english_name', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('gamenum', models.IntegerField(blank=True, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Career')),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('text', models.TextField()),
                ('time', models.DateTimeField()),
                ('orgin', models.CharField(blank=True, max_length=20, null=True)),
                ('tag1', models.CharField(blank=True, max_length=10, null=True)),
                ('tag2', models.CharField(blank=True, max_length=10, null=True)),
                ('important', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Author')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Newsleixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leixinname', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_exp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qua', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Regame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_time', models.DateTimeField()),
                ('game_players', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Author')),
                ('game_bigleixin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Gamebigleixin')),
                ('game_leixin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Gameleixin')),
                ('game_leixin_count', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Count')),
            ],
            options={
                'ordering': ['-game_time', 'game_leixin'],
            },
        ),
        migrations.CreateModel(
            name='Sharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=1000)),
                ('imp', models.BooleanField()),
                ('share_time', models.DateTimeField()),
                ('like_count', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Sponser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sportsleixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outside', models.BooleanField()),
                ('addr_pc_1', models.CharField(max_length=1200)),
                ('addr_pc_2', models.CharField(blank=True, max_length=1200, null=True)),
                ('addr_pc_extr', models.CharField(blank=True, max_length=1200, null=True)),
                ('addr_mobi_1', models.CharField(max_length=1200)),
                ('addr_mobi_2', models.CharField(blank=True, max_length=1200, null=True)),
                ('addr_mobi_extr', models.CharField(blank=True, max_length=1200, null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Streamtvlogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('src', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=80)),
                ('bbstext', models.TextField()),
                ('ttime', models.DateTimeField()),
                ('ttop', models.BooleanField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(max_length=30)),
                ('english_name', models.CharField(max_length=30)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('city', models.CharField(max_length=30)),
                ('ground', models.CharField(max_length=40)),
                ('website', models.URLField(blank=True, null=True)),
                ('clo_sponser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Sponser')),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Nation')),
            ],
        ),
        migrations.CreateModel(
            name='Tv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('langunage', models.CharField(blank=True, max_length=20, null=True)),
                ('address1', models.CharField(max_length=1000)),
                ('address2', models.CharField(blank=True, max_length=1500, null=True)),
                ('address3', models.CharField(blank=True, max_length=1500, null=True)),
                ('mob_addr', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videotvname', models.CharField(blank=True, max_length=20, null=True)),
                ('addr_baidu', models.URLField()),
                ('addr_xunlei', models.URLField(blank=True, null=True)),
                ('addr_ext_baidu', models.URLField(blank=True, null=True)),
                ('addr_ext_xunlei', models.URLField(blank=True, null=True)),
                ('video_size', models.CharField(max_length=20)),
                ('geshi', models.CharField(max_length=10)),
                ('vidoe_geshi', models.CharField(max_length=10)),
                ('sound_geshi', models.CharField(max_length=10)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Language')),
                ('quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Quality')),
            ],
        ),
        migrations.AddField(
            model_name='stream',
            name='orginname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Streamtvlogo'),
        ),
        migrations.AddField(
            model_name='stream',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Quality'),
        ),
        migrations.AddField(
            model_name='stream',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Video'),
        ),
        migrations.AddField(
            model_name='regame',
            name='gmsleixin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Sportsleixin'),
        ),
        migrations.AddField(
            model_name='regame',
            name='important',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Important'),
        ),
        migrations.AddField(
            model_name='regame',
            name='jijin',
            field=models.ManyToManyField(blank=True, null=True, to='scriptsports.Jijin'),
        ),
        migrations.AddField(
            model_name='regame',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.State'),
        ),
        migrations.AddField(
            model_name='regame',
            name='stream',
            field=models.ManyToManyField(blank=True, null=True, to='scriptsports.Stream'),
        ),
        migrations.AddField(
            model_name='regame',
            name='video',
            field=models.ManyToManyField(blank=True, null=True, to='scriptsports.Video'),
        ),
        migrations.AddField(
            model_name='news',
            name='newsleixin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Newsleixin'),
        ),
        migrations.AddField(
            model_name='news',
            name='sportsleixin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Sportsleixin'),
        ),
        migrations.AddField(
            model_name='man',
            name='clo_sponser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Sponser'),
        ),
        migrations.AddField(
            model_name='man',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Team'),
        ),
        migrations.AddField(
            model_name='man',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Nation'),
        ),
        migrations.AddField(
            model_name='man',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Position'),
        ),
        migrations.AddField(
            model_name='man',
            name='spleixin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Sportsleixin'),
        ),
        migrations.AddField(
            model_name='jijin',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Language'),
        ),
        migrations.AddField(
            model_name='gameshow',
            name='game_tv',
            field=models.ManyToManyField(to='scriptsports.Tv'),
        ),
        migrations.AddField(
            model_name='gameshow',
            name='sports_leixin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scriptsports.Sportsleixin'),
        ),
    ]
