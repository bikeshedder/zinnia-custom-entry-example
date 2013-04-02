from django.db import models
from taggit.managers import TaggableManager
from zinnia.models import entry as ze


class TagsEntry(models.Model):
    tags = TaggableManager()

    @property
    def tags_list(self):
        '''
        Return iterable list of tags.
        '''
        return self.tags.all()

    class Meta:
        abstract = True


class ExtEntry(
        ze.CoreEntry,
        ze.ContentEntry,
        ze.DiscussionsEntry,
        ze.RelatedEntry,
        ze.ExcerptEntry,
        ze.ImageEntry,
        ze.FeaturedEntry,
        ze.AuthorsEntry,
        ze.CategoriesEntry,
        TagsEntry,
        ze.LoginRequiredEntry,
        ze.PasswordRequiredEntry,
        ze.ContentTemplateEntry,
        ze.DetailTemplateEntry):
    '''
    Abstract entry model class which uses the abstract TagsEntry
    model that uses django-taggit instead of django-tagging.
    '''

    class Meta(ze.CoreEntry.Meta):
        abstract = True
