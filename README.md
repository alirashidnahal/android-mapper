# android-mapper
# TapMirror

**TapMirror** is a Windows application that enables Android screen mirroring over USB and maps keyboard/mouse inputs to touch events on the mirrored screen.  
This project is ideal for gamers or anyone wanting to control Android devices via PC input without rooting their phones.

**تاپ‌میرور** یک نرم‌افزار ویندوزی است که با اتصال گوشی اندرویدی از طریق USB، صفحه‌ی گوشی را روی کامپیوتر نمایش می‌دهد و امکان نگاشت (Map) دکمه‌های صفحه‌کلید و ماوس را به لمس روی گوشی فراهم می‌کند.  
این ابزار مخصوص افرادی است که می‌خواهند بدون روت کردن گوشی خود، آن را از طریق موس و کیبورد کنترل کنند (مخصوصاً برای بازی‌ها).

---

## 🔧 Features | ویژگی‌ها

- ✅ **Screen Mirroring** via USB (using `scrcpy`)
- ✅ **Custom Touch Mapping** with Keyboard & Mouse
- ✅ **Save/Load Key Mappings**
- ✅ **No Root Required**
- ✅ **High Performance** (ideal for Android gaming)
- ✅ **Cross-monitor support** (multi-display aware)
- 🧩 Open Source under GPL v3 license

---

## 🖥 Requirements | پیش‌نیازها

- Windows 10/11
- Python 3.8+
- Android device with **USB debugging enabled**
- [`scrcpy`](https://github.com/Genymobile/scrcpy) installed and working

---

## 📦 Installation | نصب

1. فعال‌سازی **USB debugging** در گوشی اندروید  
   Settings → Developer options → Enable USB debugging

2. نصب `scrcpy` (برای mirror کردن گوشی):  
   [راهنمای نصب scrcpy](https://github.com/Genymobile/scrcpy)

3. نصب پیش‌نیازهای پایتون:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use | نحوه استفاده

### 1. Run `scrcpy` manually  
ابتدا پنجره‌ی scrcpy را به صورت دستی اجرا کنید تا صفحه‌ی گوشی نمایش داده شود.

### 2. Map touch points (once)

```bash
python main.py --mapping
```

با ماوس روی صفحه scrcpy کلیک کنید تا مکان لمس برای کلیدهای A, S, D, W ثبت شوند. مختصات ذخیره می‌شود در فایل `mapping.json`.

### 3. Run normally to activate keys

```bash
python main.py
```

با فشار دادن کلیدهای تعریف‌شده، تاچ مربوطه روی گوشی اجرا می‌شود!

---

## 🧠 Example Use Cases | کاربردها

- اجرای بازی‌های اندرویدی با کیبورد و موس روی کامپیوتر
- اتوماسیون تست رابط کاربری اپلیکیشن‌ها
- کنترل گوشی بدون نیاز به لمس فیزیکی

---

## 📁 Project Structure | ساختار پروژه

```
android-mapper/
│
├── main.py                 # Entry point
├── input_mapper.py         # Keyboard → Touch logic
├── mapping.json            # Saved key mappings
├── requirements.txt
└── ui/
    └── mapping_overlay.py  # GUI overlay for mapping
```

---

## ⛔ Limitations | محدودیت‌ها

- فعلاً فقط از اتصال USB پشتیبانی می‌شود.
- صدای گوشی منتقل نمی‌شود.
- پنجره scrcpy باید به صورت دستی اجرا شود.

---

## 📌 Future Plans | برنامه‌های آینده

- اتصال بی‌سیم (WiFi)
- پشتیبانی از صدا
- تعریف مپ دلخواه با GUI گرافیکی
- اضافه کردن چندین کلید و پیکربندی قابل شخصی‌سازی بیشتر
- راه‌اندازی خودکار scrcpy از داخل نرم‌افزار
- پشتیبانی از چندین دستگاه به صورت همزمان

---

## 📜 License

**TapMirror** is licensed under the [GPL v3 License](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🙌 Contribute | مشارکت

اگر قصد توسعه یا بهبود پروژه را دارید خوشحال می‌شویم همراه شوید! Pull Request بفرستید یا Issue باز کنید.

---

## ✉️ Contact

برای پیشنهادات یا گزارش باگ‌ها، از طریق Issueها یا ایمیل در تماس باشید.
