import stripe
from flask import Flask, request, jsonify
from config import Config  # Import the configuration settings

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration settings from config.py

stripe.api_key = app.config['STRIPE_SECRET_KEY']  # Set the Stripe secret key

# Define a route to handle payment requests
@app.route('/charge', methods=['POST'])
def charge():
    try:
        # Get the payment token ID and other details from the request
        token = request.form['stripeToken']
        amount = int(request.form['amount'])  # Amount should be in cents
        currency = 'usd'  # Currency (in this case, US dollars)

        # Create a charge using the Stripe API
        charge = stripe.Charge.create(
            amount=amount,
            currency=currency,
            description='Payment for Your App',
            source=token,
        )

        # Payment successful, you can handle success logic here
        return jsonify({'success': True, 'message': 'Payment was successful!'})

    except stripe.error.StripeError as e:
        # Payment failed, handle error logic here
        return jsonify({'success': False, 'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)