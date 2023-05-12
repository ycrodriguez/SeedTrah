from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO


def exportPDF(path: str, name: str, map):
    contents = render_to_string(path, map, )
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename={}.pdf'.format(name)
    result = BytesIO()
    pisa.pisaDocument(BytesIO(contents.encode('iso-8859-1')), result, show_error_as_pdf=True, encoding='iso-8859-1')
    response.write(result.getvalue())
    result.close()
    return response
