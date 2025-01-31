import math
import re
from datetime import datetime

def calculate_points(receipt):
    points = 0

    points += len(re.sub(r'\W', '', receipt.retailer))

    total = float(receipt.total)
    if total == int(total):
        points += 50

    if total % 0.25 == 0:
        points += 25

    points += (len(receipt.items) // 2) * 5

    for item in receipt.items:
        desc_length = len(item.shortDescription.strip())
        if desc_length % 3 == 0:
            price = float(item.price)
            points += math.ceil(price * 0.2)

    purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
    if purchase_date.day % 2 == 1:
        points += 6

    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")
    if 14 <= purchase_time.hour < 16:
        points += 10

    return points
