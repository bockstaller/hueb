from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from hueb.apps.hueb_legacy_latein import models as Legacy

# Register your models here.
from .models import (
    Archive,
    Country,
    DdcGerman,
    Document,
    Language,
    Location,
    Person,
    YearRange,
)


class LegacyAuthorNew(admin.TabularInline):
    model = Legacy.AuthorNew
    extra = 0


@admin.register(YearRange)
class YearRangeAdmin(admin.ModelAdmin):
    readonly_fields = ("app", "author_link", "translator_link")
    list_display = ("id", "timerange", "start_uncertainty", "end_uncertainty")
    search_fields = ("timerange", "id")
    fieldsets = (
        (
            "Timerange Information",
            {
                "description": ("Daterange information"),
                "fields": (
                    "timerange",
                    "start_uncertainty",
                    "end_uncertainty",
                    "parsed_string",
                ),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "author_link", "translator_link"),
            },
        ),
    )

    def author_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_authornew_change", args=[obj.author_ref.id]
        )
        link = '<a href="%s">%s</a>' % (url, obj.author_ref)
        return mark_safe(link)

    author_link.short_description = "Author"

    def translator_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translatornew_change",
            args=[obj.translator_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translator_ref)
        return mark_safe(link)

    translator_link.short_description = "Translator"


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ("app", "author_link", "translator_link")
    list_display = ("id", "name", "lifetime", "alias", "is_alias")
    search_fields = ("name", "id")
    fieldsets = (
        (
            "Person Information",
            {
                "description": ("All known data about a person"),
                "fields": ("name", "lifetime", "alias", "is_alias"),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "translator_link", "author_link"),
            },
        ),
    )

    def author_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_authornew_change", args=[obj.author_ref.id]
        )
        link = '<a href="%s">%s</a>' % (url, obj.author_ref)
        return mark_safe(link)

    author_link.short_description = "Author"

    def translator_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translatornew_change",
            args=[obj.translator_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translator_ref)
        return mark_safe(link)

    translator_link.short_description = "Translator"


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ("app", "country_link")
    list_display = (
        "id",
        "country",
    )
    search_fields = ("country", "id")
    fieldsets = (
        (
            "Country Information",
            {
                "description": ("Information stored about the country"),
                "fields": ("country", "source"),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "country_link"),
            },
        ),
    )

    def country_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_country_change", args=[obj.country_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.country_ref)
        return mark_safe(link)

    country_link.short_description = "Country"


@admin.register(DdcGerman)
class DdcGermanAdmin(admin.ModelAdmin):
    readonly_fields = ("app", "ddc_link")
    list_display = (
        "id",
        "ddc_number",
        "ddc_name",
    )
    search_fields = ("ddc_number", "ddc_name")

    fieldsets = (
        (
            "DDC Information",
            {"description": (" "), "fields": ("ddc_number", "ddc_name")},
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "ddc_link"),
            },
        ),
    )

    def ddc_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_ddcgerman_change", args=[obj.ddc_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.ddc_ref)
        return mark_safe(link)

    ddc_link.short_description = "DDC"


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    readonly_fields = ("app", "language_link")
    list_display = (
        "id",
        "language",
    )
    search_fields = ("language", "id")

    fieldsets = (
        (
            "Language Information",
            {"description": (" "), "fields": ("language", "language_ref")},
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "language_link"),
            },
        ),
    )

    def language_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_language_change", args=[obj.language_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.language_ref)
        return mark_safe(link)

    language_link.short_description = "Language"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ("app", "location_link")
    list_display = (
        "id",
        "name",
        "adress",
        "country",
        "hostname",
        "ip",
        "z3950_gateway",
    )

    search_fields = ("name", "address", "country")

    fieldsets = (
        (
            "Location Information",
            {
                "description": (" "),
                "fields": (
                    "name",
                    "adress",
                    "country",
                    "hostname",
                    "ip",
                    "z3950_gateway",
                ),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": ("app", "location_link"),
            },
        ),
    )

    def location_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_locationnew_change", args=[obj.location_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.location_ref)
        return mark_safe(link)

    location_link.short_description = "Location"


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    readonly_fields = ("app", "locAssign_link")
    list_display = ("id", "signatur", "link")
    search_fields = ("signatur", "id")
    fieldsets = (
        (
            "Archive Information",
            {
                "description": ("Stores the archive locations of documents"),
                "fields": ("signatur", "link"),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": (),
                "readonly_fields": ("app", "locAssign_link"),
            },
        ),
    )

    def locAssign_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_locassign_change", args=[obj.locAssign_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.locAssign_ref)
        return mark_safe(link)

    locAssign_link.short_description = "Archive Location"


class ArchiveInline(admin.TabularInline):
    # def get_queryset(self, request):
    #    qs = super(ArchiveInline, self).get_queryset(request)
    #    return qs.select_related("location")

    model = Document.located_in.through
    extra = 0
    verbose_name = "Archive Location"
    verbose_name_plural = verbose_name + "s"


class DocumentAuthorInline(admin.TabularInline):
    def get_queryset(self, request):
        qs = super(DocumentAuthorInline, self).get_queryset(request)
        return qs.select_related("person")

    model = Document.written_by.through
    extra = 0
    verbose_name = "Document-Author Relationship"
    verbose_name_plural = verbose_name + "s"


class DocumentPublisherInline(admin.TabularInline):
    def get_queryset(self, request):
        qs = super(DocumentPublisherInline, self).get_queryset(request)
        return qs.select_related("person")

    model = Document.publishers.through
    extra = 0
    verbose_name = "Document-Publisher Relationship"
    verbose_name_plural = verbose_name + "s"


class DocumentTranslatedFromInline(admin.TabularInline):
    def get_queryset(self, request):
        qs = super(DocumentTranslatedFromInline, self).get_queryset(request)
        return qs.select_related("from_document")

    model = Document.translated_from.through
    fk_name = "from_document"
    extra = 0
    verbose_name = "Orginal Document"
    verbose_name_plural = verbose_name + "s"


class DocumentTranslatedToInline(admin.TabularInline):
    def get_queryset(self, request):
        qs = super(DocumentTranslatedToInline, self).get_queryset(request)
        return qs.select_related("from_document")

    model = Document.translated_to.through
    fk_name = "from_document"
    extra = 0
    verbose_name = "Translated Document"
    verbose_name_plural = verbose_name + "s"


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    readonly_fields = (
        "app",
        "origAssign_link",
        "original_link",
        "translation_link",
        "originalAuthor_link",
        "translationTranslator_link",
    )
    list_display = (
        "id",
        "title",
        "subtitle",
        "published_location",
        "edition",
        "language",
        "year",
        "real_year",
        "ddc",
    )
    inlines = [
        DocumentAuthorInline,
        DocumentPublisherInline,
        DocumentTranslatedFromInline,
        DocumentTranslatedToInline,
        ArchiveInline,
    ]
    search_fields = ("id", "title", "author")
    fieldsets = (
        (
            "Document Information",
            {
                "description": ("Stores the information known about documents"),
                "fields": (
                    "title",
                    "subtitle",
                    "year",
                    "published_location",
                    "edition",
                    "language",
                    "real_year",
                    "country",
                    "ddc",
                ),
            },
        ),
        (
            "Datasource for reference",
            {
                "description": (
                    "The information for this entry were derived from this old database entry."
                ),
                "fields": (
                    "app",
                    "origAssign_link",
                    "original_link",
                    "originalAuthor_link",
                    "translationTranslator_link",
                    "translation_link",
                ),
            },
        ),
    )

    def origAssign_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_origassign_change", args=[obj.origAssign_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.origAssign_ref)
        return mark_safe(link)

    origAssign_link.short_description = "Original<->Translation Relationship"

    def original_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_originalnew_change", args=[obj.original_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.original_ref)
        return mark_safe(link)

    original_link.short_description = "Original Text"

    def translation_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translationnew_change",
            args=[obj.translation_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translation_ref)
        return mark_safe(link)

    translation_link.short_description = "Translation"

    def originalAuthor_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_originalnewauthornew_change",
            args=[obj.originalAuthor_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.originalAuthor_ref)
        return mark_safe(link)

    originalAuthor_link.short_description = "Author"

    def translationTranslator_link(self, obj):
        url = reverse(
            "admin:hueb_legacy_latein_translationnewtranslatornew_change",
            args=[obj.translationTranslator_ref.id],
        )
        link = '<a href="%s">%s</a>' % (url, obj.translationTranslator_ref)
        return mark_safe(link)

    translationTranslator_link.short_description = "Translator"
