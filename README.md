# Receipt Processor API

A FastAPI-based web service that processes receipts, assigns unique IDs, and calculates reward points based on receipt details.

## Features
- Accepts JSON receipt submissions.
- Generates a unique `ID` for each receipt.
- Calculates reward points based on predefined rules.
- Provides an API to retrieve points for a given receipt.
- Uses FastAPI for high performance.
- Supports deployment via Docker.

---

## API Endpoints

### **1️⃣ Process Receipt**
#### **`POST /receipts/process`**
✔ Accepts a receipt JSON and returns a unique receipt ID.

#### **📥 Request Body (Example)**
```json
{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    { "shortDescription": "Mountain Dew 12PK", "price": "6.49" },
    { "shortDescription": "Emils Cheese Pizza", "price": "12.25" }
  ],
  "total": "35.35"
}
