from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class TreeMenu_MPTT(MPTTModel):
    name = models.CharField('Название', max_length=64, unique=True)
    slug = models.SlugField('slug', max_length=255, unique=True, null=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        super(TreeMenu_MPTT, self).save(*args, **kwargs)
        try:
            trees = TreeMenu_MPTT.objects.all()
            for tree in trees:
                if tree.lft or tree.rght or tree.tree_id == 0:
                    TreeMenu_MPTT.objects.rebuild()
        except Exception as e:
            print(e)
            pass

    def get_absolute_url(self):
        return reverse('TreeViewMenu:menu_detail_MPTT',
                       args=[self.id, self.slug])

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'MPTT'

    class MPTTMeta:
        order_insertion_by = ['name']
