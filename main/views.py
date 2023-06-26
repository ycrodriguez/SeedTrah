from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, CreateView
from django.contrib.auth import authenticate, login

from main.forms import UserForm, ClienteForm, PersonaNaturalForm, EntidadEstatalForm, PrefacturaForm
from main.models import Cliente, Prefactura, Producto, Semilla, Venta, Almacen


class Index(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'custom/index.html')


class Login(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {'form': form}
        return render(request, 'custom/login.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('panel')
        form = UserForm()
        context['msg'] = True
        context['form'] = form
        return render(request, 'custom/login.html', context)


class Register(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        formRegisterUser = UserCreationForm()
        context = {'form': formRegisterUser}
        return render(request, 'custom/register.html', context)

    def post(self, request, *args, **kwargs):
        formRegisterUser = UserCreationForm(request.POST)
        if formRegisterUser.is_valid():
            formRegisterUser.save()
            return redirect('login')
        return render(request, 'custom/register.html', {'form': formRegisterUser})


class Panel(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        context = {}
        cliente = Cliente.objects.filter(usuario=request.user).first()
        context['cliente'] = cliente
        context['cant_prefactura'] = \
            Prefactura.objects.filter(venta__isnull=True, cliente=cliente).aggregate(cantidad=Count('id'))[
                'cantidad']
        context['cant_producto'] = Producto.objects.all().count()
        context['semillas'] = Semilla.objects.all()
        context['cant_ventas'] = Venta.objects.filter(prefactura__cliente=cliente).count()
        gasto = 0
        for p in Prefactura.objects.filter(cliente=cliente):
            if not Venta.objects.filter(prefactura=p):
                gasto += p.costo_total
        context['gasto'] = gasto
        return render(request, 'custom/panel.html', context)


class ProductosView(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        context = {}
        cliente = Cliente.objects.filter(usuario=request.user).first()
        context['cliente'] = cliente
        context['producto'] = Producto.objects.all()
        return render(request, 'custom/productos.html', context)


class PrefacturaView(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        context = {}
        cliente = Cliente.objects.filter(usuario=request.user).first()
        context['cliente'] = cliente
        prefactura = Prefactura.objects.filter(cliente=cliente)
        context['prefactura'] = prefactura
        venta = Venta.objects.filter(prefactura=prefactura.first()).first()
        context['venta'] = venta
        return render(request, 'custom/prefacturas.html', context)


class AddCliente(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        context = {}
        cliente = Cliente.objects.filter(usuario=request.user).first()
        context['cliente'] = cliente
        formCliente = ClienteForm()
        context['formClient'] = formCliente
        formPersona = PersonaNaturalForm()
        context['formPersona'] = formPersona
        formEntidad = EntidadEstatalForm()
        context['formEntidad'] = formEntidad
        return render(request, 'custom/add_cliente.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        cliente = Cliente.objects.filter(usuario=request.user).first()
        context['cliente'] = cliente
        if cliente:
            if cliente.tipo == 'Persona Natural':
                formPersona = PersonaNaturalForm(request.POST)
                if formPersona.is_valid():
                    PersonaNatural = formPersona.save()
                    cliente.persona_natural = PersonaNatural
                    cliente.save()
                formPersona = PersonaNaturalForm()
                context['formPersona'] = formPersona
                return redirect('panel')

            if cliente.tipo == 'Entidad Estatal':
                formEntidad = EntidadEstatalForm(request.POST)
                if formEntidad.is_valid():
                    EntidadEstatal = formEntidad.save()
                    cliente.entidad_estatal = EntidadEstatal
                    cliente.save()
                formEntidad = EntidadEstatalForm()
                context['formEntidad'] = formEntidad
                return redirect('panel')
        else:
            formCliente = ClienteForm(request.POST)
            if formCliente.is_valid():
                nombre = formCliente.cleaned_data['nombre']
                direccion = formCliente.cleaned_data['direccion']
                telefono = formCliente.cleaned_data['telefono']
                empresa = formCliente.cleaned_data['empresa']
                tipo = formCliente.cleaned_data['tipo']
                usuario = request.user
                obj = Cliente.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, empresa=empresa,
                                             tipo=tipo, usuario=usuario)
                return redirect('add_cliente')
            formCliente = ClienteForm()
            context['formClient'] = formCliente
            return render(request, 'custom/add_cliente.html', context)
        return render(request, 'custom/add_cliente.html', context)


class AddPrefactura(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        context = {}
        formPrefactura = PrefacturaForm()
        producto = Producto.objects.get(pk=pk)
        almacen = Almacen.objects.all()
        context['almacen'] = almacen
        context['producto'] = producto
        context['error_pn'] = False
        context['formPrefactura'] = formPrefactura
        return render(request, 'custom/add_prefactura.html', context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        context = {}
        hoy = timezone.now()
        producto = Producto.objects.get(pk=pk)
        context['producto'] = producto
        almacen = producto.almacen
        context['almacen'] = almacen
        cliente = Cliente.objects.filter(usuario=request.user).first()
        cantidad_comprada = Prefactura.objects.filter(
            cliente=cliente,
            producto=producto,
            fecha__gte=hoy - timezone.timedelta(hours=24)).aggregate(total=Sum('cantidad'))['total'] or 0
        formPrefactura = PrefacturaForm(request.POST)
        if formPrefactura.is_valid():
            cantidad = formPrefactura.cleaned_data['cantidad']
            lugar_recogida = formPrefactura.cleaned_data['lugar_recogida']
            costo_total = cantidad * producto.valor
            costo_unitario = cantidad * producto.valor
            context['limite'] = False
            if almacen:
                if cantidad <= producto.cantidad_existente:
                    if cliente.persona_natural and cantidad_comprada + cantidad > 100:
                        context['es_persona_natural'] = True
                    else:
                        prefactura = Prefactura(
                            costo_total=costo_total,
                            costo_unitario=costo_unitario,
                            cantidad=cantidad,
                            lugar_recogida=lugar_recogida,
                            almacen=almacen,
                            cliente=cliente,
                        )
                        prefactura.save()
                        producto.prefactura_set.add(prefactura)
                        producto.cantidad_existente -= prefactura.cantidad

                        producto.save()
                        return redirect('prefacturas')
                else:
                    context['cantidad_existente'] = True
        formPrefactura = PrefacturaForm()
        context['formPrefactura'] = formPrefactura
        return render(request, 'custom/add_prefactura.html', context)


class DeletePrefactura(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        prefactura = Prefactura.objects.get(pk=pk)
        prefactura.delete()
        return redirect('prefacturas')


class DeleteCuenta(ListView, CreateView):
    def get(self, request, *args, **kwargs):
        pk = request.user.pk
        user = User.objects.get(pk=pk)
        user.delete()
        return redirect('login')
