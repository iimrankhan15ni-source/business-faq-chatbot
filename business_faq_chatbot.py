
# business_faq_chatbot.py

print("=" * 40)
print("       ABC STORE - FAQ CHATBOT")
print("=" * 40)
print("Ask about hours, delivery, payment, or returns.")
print("Type 'exit' to quit.")

faq = {
    "hours": "Our store is open from 9 AM to 8 PM.",
    "delivery": "Delivery usually takes 2 to 5 days.",
    "payment": "We accept cash and online payments.",
    "returns": "Items can be returned within 7 days."
}

while True:
    question = input("\nYou: ").lower().strip()

    if question == "exit":
        print("Bot: Thank you for contacting ABC Store!")
        break

    elif question in faq:
        print("Bot:", faq[question])

    else:
        print("Bot: Sorry, I don't have an answer for that question.")
        print("Try: hours, delivery, payment, or returns.")
