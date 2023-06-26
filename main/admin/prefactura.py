from django.contrib import admin
from django.urls import path
from django.utils import timezone

from SeedTrak.funcions import exportPDF
from main.models import Prefactura


@admin.register(Prefactura)
class PrefacturaAdmin(admin.ModelAdmin):
    search_fields = ['pk']
    list_display = ['id', 'cantidad', 'costo_total', 'costo_unitario', 'lugar_recogida', 'cliente']
    change_list_template = 'admin/prefactura_change_list_template.html'

    def id(self):
        return self.pk

    def get_urls(self):
        urls = super().get_urls()
        urls = [
                   path('pdf/prefacturas/', self.admin_site.admin_view(self.reporte_prefacturas, cacheable=True))
               ] + urls
        return urls

    def reporte_prefacturas(self, request):
        return exportPDF('pdf/prefacturas/data.html',
                         '{}'.format('PDF Reporte Prefactura'),
                         {
                             'request': request,
                             'data': timezone.now(),
                             'prefacturas': Prefactura.objects.all()
                         }
                         )
