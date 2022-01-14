from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import random
from datetime import date
from main.utils import render_to_pdf



# Create your views here.

class GenerateInvoice(View):
    def get(self, request):
        return render(request, 'main/index.html')
    
    def post(self, request):
        
        data = {
                'invoice_no' : random.randint(111111,999999),
                'invoice_date' : date.today()
        }

        for i in request.POST:
           data[i] = request.POST[i]
       
        table_data = ''
        k=0
        sno=1
        grand_total = 0 
        
        for j in request.POST:
            try:
                row = '<tr>'
                cell = '<td style="padding:2px; text-align:center; font-size:large; ">'+ str(sno) +'</td>'+'<td style="padding:2px; text-align:center; font-size:large;">'+request.POST['product_name_'+str(k)]+'</td>'+'<td style="padding:2px; text-align:center; font-size:large;">'+request.POST['quantity_'+str(k)]+'</td>'+'<td style="padding:2px; text-align:center; font-size:large;">'+request.POST['amount_'+str(k)]+'</td>'
                row = row+cell+'</tr>'
                table_data = table_data+row
                grand_total = grand_total + int(request.POST['amount_'+str(k)])
                k = k+1
                sno = sno +1
               
            except BaseException:
                k = k+1
                pass
            
        data['table_data'] = table_data
        data['grand_total'] = grand_total
        
        pdf = render_to_pdf('main/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')