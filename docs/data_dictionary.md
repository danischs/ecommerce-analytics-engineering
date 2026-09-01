# Olist E-Commerce Data Dictionary

## Overview

This project uses the Brazilian Olist e-commerce dataset to build an
analytics engineering pipeline from raw CSV data through transformed
analytics models and ultimately into Power BI.

Initial profiling was performed using Python to understand:

- Table structure
- Row counts
- Missing values
- Duplicate rows
- Column uniqueness
- Candidate keys
- Table grain

---

## Tables

### 1. Customers

**Source:** `olist_customers_dataset.csv`

**Rows:** 99,441

**Grain:** One row per `customer_id`

**Candidate primary key:** `customer_id`

| Column | Description |
|---|---|
| `customer_id` | Unique identifier for the customer record |
| `customer_unique_id` | Identifier representing the underlying customer |
| `customer_zip_code_prefix` | Customer ZIP code prefix |
| `customer_city` | Customer city |
| `customer_state` | Customer state |

### Data Quality Observations

- No completely duplicated rows.
- `customer_id` is unique across all 99,441 rows.
- `customer_unique_id` contains 96,096 unique values.
- This indicates that multiple `customer_id` records can be associated
  with the same `customer_unique_id`.

---

### 2. Orders

**Source:** `olist_orders_dataset.csv`

**Rows:** 99,441

**Grain:** One row per order

**Candidate primary key:** `order_id`

| Column | Description |
|---|---|
| `order_id` | Unique identifier for an order |
| `customer_id` | Customer associated with the order |
| `order_status` | Current order status |
| `order_purchase_timestamp` | Timestamp when the order was purchased |
| `order_approved_at` | Timestamp when payment/order was approved |
| `order_delivered_carrier_date` | Date the order was handed to the carrier |
| `order_delivered_customer_date` | Date the order was delivered to the customer |
| `order_estimated_delivery_date` | Estimated delivery date |

### Data Quality Observations

- No completely duplicated rows.
- `order_id` is unique across all 99,441 rows.
- Missing values exist in several order lifecycle timestamps.
- Missing delivery timestamps may be associated with orders that did not
  reach that stage of the order lifecycle.

---

### 3. Order Items

**Source:** `olist_order_items_dataset.csv`

**Rows:** 112,650

**Grain:** One row per item within an order

**Candidate primary key:** `order_id + order_item_id`

| Column | Description |
|---|---|
| `order_id` | Order associated with the item |
| `order_item_id` | Sequential identifier for an item within an order |
| `product_id` | Product associated with the item |
| `seller_id` | Seller associated with the item |
| `shipping_limit_date` | Shipping deadline |
| `price` | Item price |
| `freight_value` | Freight/shipping cost |

### Key Validation

`order_id` alone is **not unique**.

- Rows: 112,650
- Unique `order_id` values: 98,666

The combination of:

`order_id + order_item_id`

is unique across all 112,650 rows.

Therefore, the table grain is one row per item within an order.

---

### 4. Payments

**Source:** `olist_order_payments_dataset.csv`

**Rows:** 103,886

**Grain:** One row per payment record within an order

**Candidate primary key:** `order_id + payment_sequential`

| Column | Description |
|---|---|
| `order_id` | Order associated with the payment |
| `payment_sequential` | Sequential identifier for payment records |
| `payment_type` | Payment method |
| `payment_installments` | Number of installments |
| `payment_value` | Payment amount |

### Key Validation

`order_id` alone is **not unique**.

- Rows: 103,886
- Unique `order_id` values: 99,440

The combination of:

`order_id + payment_sequential`

is unique across all 103,886 rows.

Therefore, multiple payment records can exist for a single order.

---

### 5. Reviews

**Source:** `olist_order_reviews_dataset.csv`

**Rows:** 99,224

**Grain:** One review record associated with an order

**Candidate primary key:** `review_id + order_id`

| Column | Description |
|---|---|
| `review_id` | Review identifier |
| `order_id` | Order associated with the review |
| `review_score` | Customer review score |
| `review_comment_title` | Review title |
| `review_comment_message` | Review message |
| `review_creation_date` | Review creation date |
| `review_answer_timestamp` | Timestamp of review response |

### Key Validation

Neither `review_id` nor `order_id` is unique independently.

The combination of:

`review_id + order_id`

is unique across all 99,224 rows.

### Data Quality Observations

- `review_comment_title`: 88.34% missing
- `review_comment_message`: 58.70% missing
- No completely duplicated rows.

Missing review text should not automatically be treated as invalid data because
a customer can submit a review score without providing written comments.

---

### 6. Products

**Source:** `olist_products_dataset.csv`

**Rows:** 32,951

**Grain:** One row per product

**Candidate primary key:** `product_id`

| Column | Description |
|---|---|
| `product_id` | Unique product identifier |
| `product_category_name` | Product category |
| `product_name_lenght` | Product name length |
| `product_description_lenght` | Product description length |
| `product_photos_qty` | Number of product photos |
| `product_weight_g` | Product weight in grams |
| `product_length_cm` | Product length |
| `product_height_cm` | Product height |
| `product_width_cm` | Product width |

### Data Quality Observations

- No completely duplicated rows.
- `product_id` is unique across all 32,951 rows.
- Several product attributes contain missing values.

---

### 7. Sellers

**Source:** `olist_sellers_dataset.csv`

**Rows:** 3,095

**Grain:** One row per seller

**Candidate primary key:** `seller_id`

| Column | Description |
|---|---|
| `seller_id` | Unique seller identifier |
| `seller_zip_code_prefix` | Seller ZIP code prefix |
| `seller_city` | Seller city |
| `seller_state` | Seller state |

### Data Quality Observations

- No completely duplicated rows.
- `seller_id` is unique across all 3,095 rows.

---

### 8. Geolocation

**Source:** `olist_geolocation_dataset.csv`

**Rows:** 1,000,163

**Grain:** Multiple geographic records per ZIP code prefix

**Candidate key:** Not yet established

| Column | Description |
|---|---|
| `geolocation_zip_code_prefix` | ZIP code prefix |
| `geolocation_lat` | Latitude |
| `geolocation_lng` | Longitude |
| `geolocation_city` | City |
| `geolocation_state` | State |

### Data Quality Observations

- 261,831 completely duplicated rows.
- `geolocation_zip_code_prefix` has 19,015 unique values.
- ZIP code prefixes are therefore not unique.
- The table requires additional treatment before being safely joined to
  customer or seller data.

---

### 9. Product Category Translation

**Source:** `product_category_name_translation.csv`

**Rows:** 71

**Grain:** One row per product category translation

**Candidate primary key:** `product_category_name`

| Column | Description |
|---|---|
| `product_category_name` | Original product category |
| `product_category_name_english` | English product category |

### Data Quality Observations

- No completely duplicated rows.
- Both category columns contain 71 unique values.

---

# Initial Relationship Map

```text
customers
    │
    │ customer_id
    ▼
orders
    │
    ├───────────────► payments
    │
    └───────────────► reviews
    │
    │ order_id
    ▼
order_items
    │
    ├───────────────► products
    │
    └───────────────► sellers