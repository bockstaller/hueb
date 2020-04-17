# Generated by Django 3.0.5 on 2020-04-15 21:55

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
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('datum', models.DateField(blank=True, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='AuthorNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('datum', models.DateField(blank=True, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
            ],
            options={
                'db_table': 'author_new',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=255)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='DdcGerman',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ddc_number', models.CharField(max_length=3)),
                ('ddc_name', models.CharField(max_length=255)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
            ],
            options={
                'db_table': 'ddc_german',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('language', models.CharField(max_length=255)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('adress', models.TextField(blank=True, null=True)),
                ('country', models.IntegerField(blank=True, null=True)),
                ('hostname', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('z3950_gateway', models.CharField(blank=True, max_length=255, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='LocationNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('adress', models.TextField(blank=True, null=True)),
                ('country', models.IntegerField(blank=True, null=True)),
                ('hostname', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('z3950_gateway', models.CharField(blank=True, max_length=255, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
            ],
            options={
                'db_table': 'location_new',
            },
        ),
        migrations.CreateModel(
            name='Original',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('subtitle1', models.TextField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('published_location', models.CharField(blank=True, max_length=255, null=True)),
                ('edition', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('real_year', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('datum', models.DateField(blank=True, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Country')),
                ('ddc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.DdcGerman')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Language')),
            ],
            options={
                'db_table': 'original',
            },
        ),
        migrations.CreateModel(
            name='OriginalNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('subtitle1', models.TextField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('published_location', models.CharField(blank=True, max_length=255, null=True)),
                ('edition', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('real_year', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('datum', models.DateField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Country')),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
                ('ddc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.DdcGerman')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Language')),
            ],
            options={
                'db_table': 'original_new',
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Author')),
                ('title', models.TextField(blank=True, null=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('subtitle1', models.TextField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('published_location', models.CharField(blank=True, max_length=255, null=True)),
                ('edition', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('real_year', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('datum', models.DateField(blank=True, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
                ('author_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.AuthorNew')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Country')),
                ('ddc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.DdcGerman')),
            ],
            options={
                'db_table': 'translation',
            },
        ),
        migrations.CreateModel(
            name='TranslationNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Author')),
                ('title', models.TextField(blank=True, null=True)),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('subtitle1', models.TextField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=100, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('published_location', models.CharField(blank=True, max_length=255, null=True)),
                ('edition', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('real_year', models.IntegerField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('datum', models.DateField(blank=True, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
                ('author_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.AuthorNew')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Country')),
                ('ddc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.DdcGerman')),
            ],
            options={
                'db_table': 'translation_new',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('loginname', models.CharField(max_length=255)),
                ('passwort', models.CharField(max_length=12)),
                ('anmerkungen', models.TextField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='TranslatorNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('datum', models.DateField(blank=True, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.User')),
            ],
            options={
                'db_table': 'translator_new',
            },
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('datum', models.DateField(blank=True, null=True)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.User')),
            ],
            options={
                'db_table': 'translator',
            },
        ),
        migrations.CreateModel(
            name='TranslationTranslatorNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('translation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Translation')),
                ('translator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.TranslatorNew')),
            ],
            options={
                'db_table': 'translation_translator_new',
            },
        ),
        migrations.CreateModel(
            name='TranslationTranslator',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('translation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Translation')),
                ('translator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Translator')),
            ],
            options={
                'db_table': 'translation_translator',
            },
        ),
        migrations.CreateModel(
            name='TranslationNewTranslatorNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('translation_new', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.TranslationNew')),
                ('translator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.TranslatorNew')),
            ],
            options={
                'db_table': 'translation_new_translator_new',
            },
        ),
        migrations.CreateModel(
            name='TranslationNewTranslator',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('translation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.TranslationNew')),
                ('translator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Translator')),
            ],
            options={
                'db_table': 'translation_new_translator',
            },
        ),
        migrations.AddField(
            model_name='translationnew',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.User'),
        ),
        migrations.AddField(
            model_name='translationnew',
            name='via_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='new_via_language', to='hueb_legacy_latein.Language'),
        ),
        migrations.AddField(
            model_name='translationnew',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Language'),
        ),
        migrations.AddField(
            model_name='translation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.User'),
        ),
        migrations.AddField(
            model_name='translation',
            name='via_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='via_language', to='hueb_legacy_latein.Language'),
        ),
        migrations.AddField(
            model_name='translation',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Language'),
        ),
        migrations.CreateModel(
            name='OriginalNewAuthorNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.AuthorNew')),
                ('original_new', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.OriginalNew')),
            ],
            options={
                'db_table': 'original_new_author_new',
            },
        ),
        migrations.CreateModel(
            name='OriginalNewAuthor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Author')),
                ('original', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.OriginalNew')),
            ],
            options={
                'db_table': 'original_new_author',
            },
        ),
        migrations.AddField(
            model_name='originalnew',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.User'),
        ),
        migrations.CreateModel(
            name='OriginalAuthorNew',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.AuthorNew')),
                ('original', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Original')),
            ],
            options={
                'db_table': 'original_author_new',
            },
        ),
        migrations.CreateModel(
            name='OriginalAuthor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Author')),
                ('original', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Original')),
            ],
            options={
                'db_table': 'original_author',
            },
        ),
        migrations.AddField(
            model_name='original',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.User'),
        ),
        migrations.CreateModel(
            name='OrigAssign',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('orig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Original')),
                ('trans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Translation')),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
                ('orig_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.OriginalNew')),
                ('trans_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.TranslationNew')),
                ('orig_diff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Original', related_name='orig_diff')),
                ('orig_diff_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.OriginalNew', related_name='orig_diff_new')),
                ('trans_diff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Translation', related_name='trans_diff')),
                ('trans_diff_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.TranslationNew', related_name='trans_diff_new')),
            ],
            options={
                'db_table': 'orig_assign',
            },
        ),
        migrations.CreateModel(
            name='LocAssign',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('signatur', models.CharField(max_length=255)),
                ('migration_notes', models.CharField(blank=True, max_length=1023, null=True)),
                ('migration_generated', models.BooleanField()),
                ('loc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Location')),
                ('loc_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.LocationNew')),
                ('orig', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Original')),
                ('orig_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.OriginalNew')),
                ('trans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.Translation')),
                ('trans_new', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.TranslationNew')),
            ],
            options={
                'db_table': 'loc_assign',
            },
        ),
        migrations.AddField(
            model_name='authornew',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.User'),
        ),
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hueb_legacy_latein.User'),
        ),
    ]
