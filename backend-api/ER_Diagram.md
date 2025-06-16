# ER Diagram for Super App Database

## Entities

- User
  - id (PK)
  - username
  - email
  - password_hash
  - phone_number
  - created_at
  - updated_at

- Ride
  - id (PK)
  - user_id (FK to User)
  - pickup_location
  - dropoff_location
  - ride_type
  - status
  - fare
  - created_at
  - updated_at

- CourierOrder
  - id (PK)
  - user_id (FK to User)
  - pickup_address
  - delivery_address
  - package_details
  - status
  - created_at
  - updated_at

- ChatMessage
  - id (PK)
  - sender_id (FK to User)
  - recipient_id (FK to User)
  - message_text
  - timestamp

## Relationships

- User has many Rides
- User has many CourierOrders
- User has many ChatMessages (sent and received)
