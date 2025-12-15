import hmac
import hashlib
import json
import time
import requests
import os

# --- 1. ข้อมูล API ของคุณ (กรุณาเปลี่ยนเป็นของจริง) ---
API_KEY = os.getenv("BITKUB_API_KEY")
API_SECRET = os.getenv("BITKUB_API_SECRET")
BASE_URL = "https://api.bitkub.com"

# --- 2. ฟังก์ชันสำหรับสร้างลายเซ็น (Signature) ---
def generate_signature(timestamp, method, request_path, body, api_secret):
    payload = str(timestamp) + method.upper() + request_path + (body or '')
    return hmac.new(
        api_secret.encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()

# --- 3. ข้อมูลคำสั่งซื้อ (Payload) ---
# เราจะทำการซื้อ KUB ด้วยเงิน 100 THB ที่ราคา 20 THB ต่อ KUB (Limit Order)
current_millis = int(time.time() * 1000)
client_id_string = str(current_millis)
payload = {
"sym":"btc_thb",  # คู่เหรียญที่ต้องการซื้อ
"amt":108.0,       # จำนวนเงิน THB ที่ต้องการใช้ซื้อ (100 บาท)
"rat":0.0,        # ราคา Rate ต่อ BTC ที่ต้องการซื้อ
"typ":"market",   # ชนิดคำสั่ง: 'limit' หรือ 'market'
"client_id":client_id_string,
"post_only":True
}

# --- 4. การสร้าง Request และส่งคำสั่ง ---

# สร้างลายเซ็น

# Endpoint สำหรับส่งคำสั่งซื้อ (Place Bid)
endpoint = "/api/v3/market/place-bid"
timestamp = int(time.time() * 1000)
timestampstr = str(timestamp)
method = 'POST'
body = json.dumps(payload)

signature = generate_signature(timestamp, method, endpoint, body, API_SECRET)

# กำหนด Header ที่จำเป็น
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-BTK-APIKEY': API_KEY,
    'X-BTK-SIGN': signature,
    'X-BTK-TIMESTAMP': timestampstr
}

print(f"Payload ที่ใช้ในการสร้าง Signature: {json.dumps(payload)}")
print(f"Generated Signature: {signature}")

try:
    response = requests.post(
        BASE_URL + endpoint,
        headers=headers,
        data=json.dumps(payload)
    )
    
    # ตรวจสอบสถานะการตอบกลับ
    if response.status_code == 200:
        result = response.json()
        print("\n✅ การส่งคำสั่งซื้อสำเร็จ:")
        print(json.dumps(result, indent=4))
        
        # ตัวอย่างการตอบกลับที่สำคัญ:
        # "txn_id": "หมายเลขธุรกรรม",
        # "id": "หมายเลขคำสั่งซื้อ",
        # "status": "สถานะ: 'new' หรือ 'filled'",
        # "rate": 20.0,
        # "amount": 100.0
        
    else:
        print(f"\n❌ เกิดข้อผิดพลาดในการส่งคำสั่ง (HTTP Status: {response.status_code})")
        print("Response Error:", response.text)

except Exception as e:
    print(f"\n⚠️ เกิดข้อผิดพลาดที่ไม่คาดคิด: {e}")

