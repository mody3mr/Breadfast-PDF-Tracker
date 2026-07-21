import pdfplumber

def read_delivery_pdf(pdf_path):
    print("⏳ جاري قراءة ملف الـ PDF...")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
            
            # استخراج اسم الفرع من النص
            lines = full_text.split('\n')
            branch_name = "غير معروف"
            for line in lines:
                if "اذن استلام فرع" in line or "Breadfast Coffee" in line:
                    branch_name = line
                    break
            
            print("\n-----------------------------------------")
            print(f"📍 الفرع المستهدف: {branch_name}")
            print("-----------------------------------------")
            print("📄 عينة من محتوى المستند المستخرج:")
            print(full_text[:400])
            print("-----------------------------------------")
            
    except Exception as e:
        print(f"❌ حدث خطأ أثناء قراءة الملف: {e}")

if __name__ == "__main__":
    # تجربة افتراضية لو اسم الملف موجود في نفس الرفository
    pdf_file = "Transfer History _ Breadfast--15-7.pdf"
    read_delivery_pdf(pdf_file)
```[cite: 1]

---

كل اللي عليك تعمل دلوقتي:
1. تفتح حسابك على GitHub وتعمل **New Repository** (سميه مثلاً `breadfast-pdf-tracker`).
2. ترفع الملفين دول (`main.py` و `requirements.txt`).
3. (اختياري) ترفع معاهم ملف PDF تجريبي من اللي بتبعتوهم على الجروب عشان الكود يقرأه.

قولي أول ما تعمل الـ Repository وتظبطه، عشان ندخل على الخطوة اللي بعدها ونضيف تحليل الرفض والمقبول!
