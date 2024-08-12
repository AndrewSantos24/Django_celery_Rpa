from rest_framework import views ,response,status
from stocks.models import stock
from stocks.serializers import StockSerializer
from stocks.tasks import get_stock_price

class StockPriceView(views.APIView):
    def post (self,request):
        stock_name = request.data.get('stock_name')
        get_stock_price.delay(stock_name)
        return response.Response(
            data={'mensage':'Tarefa Disparada com Sucesso!'},
            status=status.HTTP_200_OK
        )
    def get(self,request):
        stocks=stock.objects.all()
        return response.Response(
            data=StockSerializer(stocks,many=True).data,
            status=status.HTTP_200_OK,
        )