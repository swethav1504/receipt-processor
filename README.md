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
```

#### **Response (Example)**
```json
{
  "id": "7fb1377b-b223-49d9-a31a-5a02701dd310"
}
```
### **2️⃣ Get Receipt Points**
✔ Retrieves the number of points awarded for a given receipt.
#### **📥 Request Example**
```sh
curl -X GET "http://localhost:8080/receipts/7fb1377b-b223-49d9-a31a-5a02701dd310/points"
```

#### **📥 Response Example**
```json
{
  "points": 28
}
```
# 📜 Receipt Processor API

A FastAPI-based web service that processes receipts, assigns unique IDs, and calculates reward points based on receipt details.

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/receipt-processor.git
cd receipt-processor
```
### **2️⃣ Set up virtual environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
### **4️⃣ Run the FastAPI Server**
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```
✔ Open API docs at: http://localhost:8080/docs

## 🐳 Run with Docker
### **1️⃣ Build the Docker Image**
```sh
docker build -t receipt-processor .
```
### **2️⃣ Run the Container**
```sh
docker run -p 8080:8080 receipt-processor
```
### **3️⃣ Test API**
```sh
curl -X POST "http://localhost:8080/receipts/process" -H "Content-Type: application/json" -d @receipt.json
```
## ✅ Run Tests
```sh
pytest tests/
```








