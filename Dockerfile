# ใช้ base image ของ Python
FROM python:3.9-slim

# ตั้ง directory ใน Docker container สำหรับโปรเจค
WORKDIR /app

# คัดลอกไฟล์ทั้งหมดจากเครื่องของเราไปยัง Docker container
COPY . /app

# ติดตั้ง dependencies จาก requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# รันโปรแกรม Python ของคุณ
CMD ["python", "main.py"]
