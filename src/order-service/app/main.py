from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pika  # For RabbitMQ

app = FastAPI()

# Mock database
orders = []
current_id = 1  # Simple counter for ID generation

class Order(BaseModel):
    product_id: int
    quantity: int

# RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='order_created')

@app.post("/orders")
def create_order(order: Order):
    global current_id
    new_order = {
        "id": current_id,
        "product_id": order.product_id,
        "quantity": order.quantity
    }
    orders.append(new_order)
    current_id += 1  # Increment ID for the next order

    # Publish a message to RabbitMQ
    channel.basic_publish(exchange='', routing_key='order_created', body=f"Order Created: {new_order['id']}")
    return new_order

@app.get("/orders/{id}")
def get_order(id: int):
    for order in orders:
        if order["id"] == id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")
