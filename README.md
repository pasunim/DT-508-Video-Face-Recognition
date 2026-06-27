# DT-508 Video Face Recognition

โปรเจกต์นี้เป็นระบบจดจำใบหน้าแบบ Real-time จากไฟล์วิดีโอ โดยใช้ Python ร่วมกับไลบรารี `face_recognition` และ `OpenCV`

---

## Features

- โหลดภาพใบหน้าจาก database เพื่อใช้เป็น reference
- ตรวจจับใบหน้าในแต่ละ frame ของวิดีโอแบบ Real-time
- เปรียบเทียบและระบุตัวตนของใบหน้าที่พบ
- แสดงกรอบสี่เหลี่ยมและชื่อบุคคลบนหน้าจอ
- รองรับการแสดงผลแบบ Resizable Window

---

## Requirements

- Python 3.12
- [CMake](https://cmake.org/) (สำหรับ build `dlib`)
- [Homebrew](https://brew.sh/) (macOS)

### Python Packages

| Package | หน้าที่ |
|---|---|
| `opencv-python` | อ่านวิดีโอและแสดงผล |
| `face_recognition` | ตรวจจับและจดจำใบหน้า |
| `numpy` | จัดการ array ของ frame |
| `face_recognition_models` | โมเดลสำหรับ `face_recognition` |
| `setuptools` | dependency ของ `face_recognition_models` |

---

## Installation

### 1. สร้าง Virtual Environment ด้วย Python 3.12

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install opencv-python face_recognition numpy setuptools
pip install git+https://github.com/ageitgey/face_recognition_models
```

> **หมายเหตุ:** หาก `face_recognition_models` ขึ้น error `No module named 'pkg_resources'` ให้แก้ไขไฟล์
> `.venv/lib/python3.12/site-packages/face_recognition_models/__init__.py`
> โดยเปลี่ยนบรรทัด:
> ```python
> from pkg_resources import resource_filename
> ```
> เป็น:
> ```python
> from importlib.resources import files
>
> def resource_filename(package, path):
>     return str(files(package) / path)
> ```

---

## Project Structure

```
workshop-1/
├── content/
│   └── banyapon.jpg          # ภาพใบหน้าสำหรับใช้เป็น reference
├── videos/
│   └── WIN_20220925_13_54_04_Pro.mp4   # ไฟล์วิดีโอที่ต้องการประมวลผล
├── videoface.py              # สคริปต์หลัก
├── .gitignore
└── README.md
```

---

## Usage

```bash
source .venv/bin/activate
python3 videoface.py
```

- วิดีโอจะเล่นพร้อมกรอบสี่เหลี่ยมรอบใบหน้าที่ตรวจพบ
- หากจดจำได้จะแสดงชื่อบุคคล หากไม่ได้จะแสดง `UNKNOWN`
- กด **Enter** เพื่อหยุดโปรแกรม

---

## How It Works

1. โหลดภาพ reference จาก `content/` และสร้าง face encoding
2. เปิดไฟล์วิดีโอด้วย OpenCV
3. วนลูปอ่านทีละ frame และแปลงเป็น RGB
4. ใช้ `face_recognition.face_locations()` เพื่อหาตำแหน่งใบหน้าในแต่ละ frame
5. สร้าง encoding ของใบหน้าที่พบและเปรียบเทียบกับ database
6. วาดกรอบและแสดงชื่อบน frame
7. แสดงผลผ่าน OpenCV window ขนาด 960x540

---

## Subject

DT-508 — Workshop 4
