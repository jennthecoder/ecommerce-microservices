# E-Commerce Microservices App

This is a simple e-commerce application built using a microservices architecture. The app consists of three main services:
1. **Product Service**: Manages product information.
2. **Order Service**: Handles order creation and processing.
3. **Notification Service**: Sends notifications when an order is placed.

The services communicate asynchronously using a **message broker** (RabbitMQ).

---

## Features
- **Product Service**:
  - CRUD operations for products.
- **Order Service**:
  - Create and retrieve orders.
  - Publishes "Order Created" messages to RabbitMQ.
- **Notification Service**:
  - Listens for "Order Created" messages and logs notifications.
- **Message Broker**:
  - RabbitMQ facilitates communication between services.

---

## Technologies Used
- **Programming Language**: Python
- **Frameworks**: FastAPI (for Product and Order Services)
- **Message Broker**: RabbitMQ
- **Containerization**: Docker
- **Orchestration**: Docker Compose

---

## Prerequisites
Before running the app, ensure you have the following installed:
1. **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
2. **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/jennthecoder/ecommerce-microservices.git
cd ecommerce-microservices
