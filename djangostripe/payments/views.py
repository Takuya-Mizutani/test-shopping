from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe


class HomePageView(TemplateView):
    template_name = 'home.html'\


@csrf_exempt
def stripe_config(request):
	if request.method == 'GET':
		stripe_config = {'publicKey':settings.STRIPE_PUBLISHABLE_KEY}
		return JsonResponse(stripe_config, safe=False)
		

@csrf_exempt
def create_checkout_session(request):
	if request.method == 'GET':
		domain_url = 'http://localhost:8000/'
		stripe.api_key = settings.STRIPE_SECRET_KEY
		try:
			checkout_session = stripe.checkout.Session.create(
				success_url = domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
				cancel_url = domain_url + 'cancelled/',
				payment_method_type = ['card'],
				mode = 'payment',
				line_items = [
					{
						'name':'T-shirt',
						'quantity':1,
						'currency':'jpy',
						'amount':'200000',
					}
				]
			)
			return JsonResponse({'sessionId':checkout_session['id']})
		except Exception as e:
			return JsonResponse({'error':str(e)})
