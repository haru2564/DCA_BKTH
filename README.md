# DCA_BKTH 
# สามารถตั้งค่า https://www.bitkub.com/th/api-management
# วิธีการใช้ https://support.bitkub.com/th/support/solutions/articles/151000196181

# สามารถใส่ค่า API แทนสองค่าข้างล่างนี้ได้เลย
API_KEY = "BITKUB_API_KEY"
API_SECRET = "BITKUB_API_SECRET"

#### ถ้าไม่ต้องการแก้ code ให้ใส่ตามด้านล่าง
## สำหรับ Linux/macOS (Bash/Zsh)
export BITKUB_API_KEY="YOUR_API_KEY_HERE"
export BITKUB_API_SECRET="YOUR_API_SECRET_HERE"

# ตรวจสอบว่าถูกตั้งค่าแล้ว
echo $BITKUB_API_KEY

## สำหรับ Windows (Command Prompt)
set BITKUB_API_KEY="YOUR_API_KEY_HERE"
set BITKUB_API_SECRET="YOUR_API_SECRET_HERE"

# ตรวจสอบว่าถูกตั้งค่าแล้ว
echo %BITKUB_API_KEY%

## สำหรับ Windows (PowerShell)
$env:BITKUB_API_KEY="YOUR_API_KEY_HERE"
$env:BITKUB_API_SECRET="YOUR_API_SECRET_HERE"

# ตรวจสอบว่าถูกตั้งค่าแล้ว
echo $env:BITKUB_API_KEY

# อย่าลืมฝากเงินเข้ากระเป๋าก่อน run code ด้วยนะ