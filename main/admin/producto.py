from django.contrib import admin
from django.urls import path
from django.utils import timezone
from django.utils.html import format_html
from django.views.generic import DetailView
from SeedTrak.funcions.export_pdf import exportPDF

from main.models import Producto, Venta


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['semilla', 'tipo', 'cantidad_existente', 'cantidad_vendida', 'valor']
    list_display = ['semilla', 'tipo', 'cantidad_existente', 'cantidad_vendida', 'valor', 'ventas_por_producto']

    def get_urls(self):
        url = super().get_urls()
        url = [
                  path('pdf/ventas_productos/<int:pk>/', self.VentasProductoPdfView.as_view())
              ] + url
        return url

    def ventas_por_producto(self, obj: None):
        if obj:
            return format_html(
                r'<a data-toggle="tooltip" title="Ventas" style="color:blue;" class="related-widget-wrapper-link add-related" href="pdf/ventas_productos/{}/"><i class="fa fa-file-pdf"></i></a>'.format(
                    obj.pk))
        return None

    class VentasProductoPdfView(DetailView):
        def get(self, request, *args, **kwargs):
            producto = kwargs.get('pk', None)
            return exportPDF('pdf/ventas_productos/data.html',
                             '{}'.format('Ventas por Producto'),
                             {
                                 'request': request,
                                 'data': timezone.now(),
                                 'producto': Producto.objects.get(pk=producto),
                                 'ventas': Venta.objects.filter(producto__pk=producto)
                             }
                             )
