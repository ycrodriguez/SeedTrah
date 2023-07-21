from django.contrib import admin
from django.urls import path
from django.utils import timezone
from django.utils.html import format_html
from django.views.generic import DetailView

from SeedTrak.funcions import exportPDF
from main.admin.forms.venta import VentaForm
from main.models import Venta


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    search_fields = ['lugar_compra', 'fecha']
    list_display = ['prefactura', 'cliente', 'lugar_compra', 'fecha', 'ventas_por_lugar_de_compra']
    form = VentaForm
    change_list_template = 'admin/estadisticas_chabge_list_template.html'

    def cliente(self, obj):
        if obj:
            return obj.prefactura.cliente

    def get_urls(self):
        urls = super().get_urls()
        urls = [
                   path('pdf/estadisticas/', self.EstadisticasVentasPdfView.as_view()),
                   path('pdf/ventas_lugar_compra/<int:pk>/', self.VentasLugarComprasPdfView.as_view())
               ] + urls
        return urls

    def ventas_por_lugar_de_compra(self, obj: None):
        if obj:
            return format_html(
                r'<a data-toggle="tooltip" title="Ventas" style="color:red;" class="related-widget-wrapper-link add-related" href="pdf/ventas_lugar_compra/{}/"><i class="fa fa-file-pdf"></i></a>'.format(
                    obj.pk))
        return None

    class VentasLugarComprasPdfView(DetailView):
        def get(self, request, *args, **kwargs):
            ventaPk = kwargs.get('pk', None)
            venta = Venta.objects.get(pk=ventaPk)
            return exportPDF('pdf/ventas_lugar_compras/data.html',
                             '{}'.format('Ventas por lugar de compra'),
                             {
                                 'request': request,
                                 'data': timezone.now(),
                                 'lc': venta.lugar_compra,
                                 'ventas': Venta.objects.filter(lugar_compra=venta.lugar_compra),
                             }
                             )

    class EstadisticasVentasPdfView(DetailView):
        def ventas(self):
            array_ventas = []
            ventas = Venta.objects.all().order_by('-fecha')
            for v in ventas:
                ano = v.fecha.year
                mes = v.fecha.month
                if len(array_ventas) != 0:
                    if mes != array_ventas[len(array_ventas) - 1][1] or ano != array_ventas[len(array_ventas) - 1][0]:
                        array_ventas.append([ano, mes, Venta.objects.filter(fecha__month=mes, fecha__year=ano).count()])
                else:
                    array_ventas.append([ano, mes, Venta.objects.filter(fecha__month=mes, fecha__year=ano).count()])
            return array_ventas

        def promedio_mensual(self):
            ventas = Venta.objects.all()
            if ventas:
                if ventas.count() == 1:
                    return 1
                else:
                    try:
                        primero = Venta.objects.all().order_by('-fecha').last()
                        ultimo = Venta.objects.all().order_by('-fecha').first()
                        return ventas.count() / (
                                12 * (ultimo.fecha.year - primero.fecha.year) + (
                                ultimo.fecha.month - primero.fecha.month))
                    except:
                        return ventas.count()
            else:
                return 0

        def promedio_anual(self):
            ventas = Venta.objects.all()
            primero = Venta.objects.all().order_by('-fecha').last()
            ultimo = Venta.objects.all().order_by('-fecha').first()
            try:
                promedio = ventas.count() / ((ultimo.fecha.year - primero.fecha.year) + 1)
                return promedio
            except:
                return ventas.count()

        def get(self, request, *args, **kwargs):
            return exportPDF('pdf/estadisticas_ventas/data.html',
                             '{}'.format('Esatdísticas de Ventas'),
                             {
                                 'request': request,
                                 'data': timezone.now(),
                                 'ventas': self.ventas(),
                                 'pm': self.promedio_mensual(),
                                 'pa': self.promedio_anual(),
                             }
                             )
