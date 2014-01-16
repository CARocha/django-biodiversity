from datetime import datetime
from precio.models import TipoCambio, Moneda
from django.core.management.base import NoArgsCommand
import urllib

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        extranjera = Moneda.objects.get(codigo='USD')
        for local in Moneda.objects.all():
            result = urllib.urlopen("http://rate-exchange.appspot.com/currency?from=%s&to=USD" % local.codigo).read()
            equivalente = result.split(',')[1].split(': ')[1].replace('"', '').split(' ')[0]
            params = dict(cantidad_local=1, 
                          moneda_local=local,
                          cantidad_extranjera=float(equivalente),
                          fecha = datetime.today(),
                          moneda_extranjera=extranjera)
            tipo_cambio = TipoCambio(**params)
            tipo_cambio.save()
