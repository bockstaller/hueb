# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    loginname = models.CharField(max_length=255)
    passwort = models.CharField(max_length=12)
    anmerkungen = models.TextField()


    class Meta:
        db_table = 'user'

class Translator(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'translator'


class TranslatorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'translator_new'


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'author'


class AuthorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'author_new'


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'country'


class DdcGerman(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc_number = models.CharField(max_length=3)
    ddc_name = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'ddc_german'


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    language = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'language'


class LocAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    loc = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True)
    orig = models.ForeignKey('Original', models.DO_NOTHING, blank=True, null=True)
    trans = models.ForeignKey('Translation', models.DO_NOTHING, blank=True, null=True)
    signatur = models.CharField(max_length=255)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    loc_new = models.ForeignKey('LocationNew', models.DO_NOTHING, blank=True, null=True)
    orig_new = models.ForeignKey('OriginalNew', models.DO_NOTHING, blank=True, null=True)
    trans_new = models.ForeignKey('TranslationNew', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'loc_assign'


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'location'


class LocationNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    country = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    z3950_gateway = models.CharField(max_length=255, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()

    class Meta:
        db_table = 'location_new'


class OrigAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    orig_id = models.BigIntegerField(blank=True, null=True)
    trans_id = models.BigIntegerField(blank=True, null=True)
    orig_diff = models.ForeignKey('Original', models.DO_NOTHING, blank=True, null=True)
    trans_diff = models.ForeignKey('Translation', models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    orig_new_id = models.BigIntegerField(blank=True, null=True)
    trans_new_id = models.BigIntegerField(blank=True, null=True)
    orig_diff_new = models.ForeignKey('OriginalNew', models.DO_NOTHING, blank=True, null=True)
    trans_diff_new = models.ForeignKey('TranslationNew', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'orig_assign'




class Original(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    author = models.ManyToManyField(Author, through='OriginalAuthor')
    author_new = models.ManyToManyField(AuthorNew, through='OriginalAuthorNew')

    class Meta:
        db_table = 'original'

class OriginalNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    author = models.ManyToManyField(Author, through='OriginalNewAuthor')
    author_new = models.ManyToManyField(AuthorNew, through='OriginalNewAuthorNew')

    class Meta:
        db_table = 'original_new'


class Translation(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language_id = models.BigIntegerField(blank=True, null=True)
    via_language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    author_new = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    translator = models.ManyToManyField(Translator, through='TranslationTranslator')
    translator_new = models.ManyToManyField(TranslatorNew, through='TranslationTranslatorNew')

    class Meta:
        db_table = 'translation'


class TranslationNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    ddc = models.ForeignKey(DdcGerman, models.DO_NOTHING, blank=True, null=True)
    author_id = models.BigIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    subtitle1 = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_location = models.CharField(max_length=255, blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    language_id = models.BigIntegerField(blank=True, null=True)
    via_language = models.ForeignKey(Language, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    real_year = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    datum = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    migration_notes = models.CharField(max_length=1023, blank=True, null=True)
    migration_generated = models.BooleanField()
    author_new = models.ForeignKey(Author, models.DO_NOTHING, blank=True, null=True)
    translator = models.ManyToManyField(Translator, through='TranslationNewTranslator')
    translator_new = models.ManyToManyField(TranslatorNew, through='TranslationNewTranslatorNew')

    class Meta:
        db_table = 'translation_new'


class OriginalAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey(Original, models.DO_NOTHING)
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        db_table = 'original_author'


class OriginalAuthorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey(Original, models.DO_NOTHING)
    author = models.ForeignKey(AuthorNew, models.DO_NOTHING)

    class Meta:
        db_table = 'original_author_new'


class OriginalNewAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    original = models.ForeignKey(OriginalNew, models.DO_NOTHING)
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        db_table = 'original_new_author'


class OriginalNewAuthorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    original_new = models.ForeignKey(OriginalNew, models.DO_NOTHING)
    author = models.ForeignKey(AuthorNew, models.DO_NOTHING)

    class Meta:
        db_table = 'original_new_author_new'


class TranslationNewTranslator(models.Model):
    id = models.BigAutoField(primary_key=True)
    translation = models.ForeignKey(TranslationNew, models.DO_NOTHING)
    translator = models.ForeignKey('Translator', models.DO_NOTHING)

    class Meta:
        db_table = 'translation_new_translator'


class TranslationNewTranslatorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    translation_new = models.ForeignKey(TranslationNew, models.DO_NOTHING)
    translator = models.ForeignKey('TranslatorNew', models.DO_NOTHING)

    class Meta:
        db_table = 'translation_new_translator_new'


class TranslationTranslator(models.Model):
    id = models.BigAutoField(primary_key=True)
    translation = models.ForeignKey(Translation, models.DO_NOTHING)
    translator = models.ForeignKey('Translator', models.DO_NOTHING)

    class Meta:
        db_table = 'translation_translator'


class TranslationTranslatorNew(models.Model):
    id = models.BigAutoField(primary_key=True)
    translation = models.ForeignKey(Translation, models.DO_NOTHING)
    translator = models.ForeignKey('TranslatorNew', models.DO_NOTHING)

    class Meta:
        db_table = 'translation_translator_new'
