import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")


def test_key(df, columns):
    """
    Test whether a column or combination of columns uniquely
    identifies every row in a DataFrame.
    """

    total_rows = len(df)
    unique_rows = df[columns].drop_duplicates().shape[0]

    print(f"Testing: {columns}")
    print(f"Total rows: {total_rows:,}")
    print(f"Unique combinations: {unique_rows:,}")

    if total_rows == unique_rows:
        print("RESULT: UNIQUE ✓")
    else:
        duplicates = total_rows - unique_rows
        print(f"RESULT: NOT UNIQUE ✗")
        print(f"Duplicate combinations: {duplicates:,}")

    print()


# --------------------------------------------------
# ORDERS
# --------------------------------------------------

orders = pd.read_csv(DATA_DIR / "olist_orders_dataset.csv")

print("=" * 60)
print("ORDERS")
print("=" * 60)

test_key(orders, ["order_id"])


# --------------------------------------------------
# ORDER ITEMS
# --------------------------------------------------

order_items = pd.read_csv(DATA_DIR / "olist_order_items_dataset.csv")

print("=" * 60)
print("ORDER ITEMS")
print("=" * 60)

test_key(order_items, ["order_id"])
test_key(order_items, ["order_id", "order_item_id"])


# --------------------------------------------------
# PAYMENTS
# --------------------------------------------------

payments = pd.read_csv(DATA_DIR / "olist_order_payments_dataset.csv")

print("=" * 60)
print("PAYMENTS")
print("=" * 60)

test_key(payments, ["order_id"])
test_key(payments, ["order_id", "payment_sequential"])


# --------------------------------------------------
# REVIEWS
# --------------------------------------------------

reviews = pd.read_csv(DATA_DIR / "olist_order_reviews_dataset.csv")

print("=" * 60)
print("REVIEWS")
print("=" * 60)

test_key(reviews, ["review_id"])
test_key(reviews, ["order_id"])
test_key(reviews, ["review_id", "order_id"])


# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------

products = pd.read_csv(DATA_DIR / "olist_products_dataset.csv")

print("=" * 60)
print("PRODUCTS")
print("=" * 60)

test_key(products, ["product_id"])


# --------------------------------------------------
# SELLERS
# --------------------------------------------------

sellers = pd.read_csv(DATA_DIR / "olist_sellers_dataset.csv")

print("=" * 60)
print("SELLERS")
print("=" * 60)

test_key(sellers, ["seller_id"])