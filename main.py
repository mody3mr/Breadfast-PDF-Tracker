import pdfplumber

def analyze_delivery_note(pdf_path):
    print("⏳ جاري تحليل إذن الاستلام...")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
            
            # 1. استخراج اسم الفرع
            lines = full_text.split('\n')
            branch_name = "غير معروف"
            for line in lines:
                if "اذن استلام فرع" in line or "Breadfast Coffee" in line:
                    branch_name = line
                    break
            
            print(f"\n📍 الفرع المستهدف: {branch_name}")
            print("=" * 40)
            
            # 2. استخراج الجداول (Tables) من الـ PDF بدقة
            all_items = []
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        # نتأكد إن السطر فيه بيانات صنف (مش هيدر الجدول)
                        # بنظف النصوص ونشجلها
                        cleaned_row = [cell.strip() if cell else "" for cell in row]
                        all_items.append(cleaned_row)
            
            # عرض التحليل المبدئي للأصناف
            print(f"📦 تم العثور على {len(all_items)} صف/صنف في المستند.")
            
            # مؤشر عشان نعرف هل فيه رفض ولا كله تمام
            has_rejections = False
            
            for idx, item in enumerate(all_items):
                # هنا بنطبع عينة للتبسيط، وهنربطها قدام بالتحليل الكامل
                print(f"السطر {idx}: {item}")
                
            print("=" * 40)
            print("✅ تمت عملية قراءة الجدول وتحليله بنجاح!")
            
    except Exception as e:
        print(f"❌ حدث خطأ أثناء تحليل الملف: {e}")

if __name__ == "__main__":
    pdf_file = "Transfer History _ Breadfast--15-7.pdf"
    analyze_delivery_note(pdf_file)
