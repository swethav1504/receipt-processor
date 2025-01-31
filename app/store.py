import uuid

receipts = {}

def save_receipt(receipt):
    receipt_id = str(uuid.uuid4())
    receipts[receipt_id] = receipt
    return receipt_id

def get_receipt(receipt_id):
    return receipts.get(receipt_id)
