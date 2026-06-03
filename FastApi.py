import razorpay
from fastapi import FastAPI

app = FastAPI()

client = razorpay.Client(
    auth=("YOUR_KEY_ID", "YOUR_KEY_SECRET")
)

@app.post("/create-order")
def create_order():

    order = client.order.create({
        "amount": 1000,   # ₹10 = 1000 paise
        "currency": "INR",
        "payment_capture": 
    })

    return order

    