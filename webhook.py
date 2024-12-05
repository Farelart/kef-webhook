from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/webhook")
async def webhook(request: Request):
    # Step 1: Get data sent by FixPay
    payload = await request.json()
    print("Webhook received:", payload)

    # Step 2: Process the data
    event = payload.get("event")  # e.g., "payment_success"
    user_email = payload.get("user_email")  # Customer's email
    amount = payload.get("amount")  # Payment amount

    if event == "payment_success":
        # Step 3: Perform your action (e.g., send an email)
        print(f"Payment confirmed for {user_email}, amount: {amount}")
        # (Later, we'll add email-sending functionality here.)

    # Step 4: Respond to FixPay
    return {"status": "success"}
