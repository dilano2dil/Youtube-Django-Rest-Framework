import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def home(request):

    if request.method == 'POST':

        post_data = request.body
        data = json.loads(post_data)

        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        product = Product.objects.create(
            name=name,
            description=description,
            price=price
        )

        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'created_at': product.created_at,
            'updated_at': product.updated_at
        })

    products = Product.objects.all()

    data = [{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': str(product.price),
    } for product in products]

    return JsonResponse(data, safe=False)