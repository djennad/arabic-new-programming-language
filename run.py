#!/usr/bin/env python3
"""نقطة تشغيل لغة البرمجة العربية من سطر الأوامر.

الاستخدام:
    python3 run.py برنامجي.arabic     ملاحظة تشغيل ملف
    python3 run.py                    ملاحظة الوضع التفاعلي (REPL)
"""

import sys

from arabic_lang import خطأ_لغوي, شغّل_ملف
from arabic_lang.interpreter import مفسر
from arabic_lang.lexer import حلل_الأسطر
from arabic_lang.parser import حلل


def _نفّذ_مقطعا(مفسر_تفاعلي, الأسطر_المؤقتة):
    المصدر = "\n".join(الأسطر_المؤقتة)
    if المصدر.strip():
        try:
            الأسطر = حلل_الأسطر(المصدر)
            if الأسطر:
                الشجرة = حلل(الأسطر)
                مفسر_تفاعلي.نفّذ_برنامج(الشجرة)
        except خطأ_لغوي as خطأ:
            print(f"خطأ: {خطأ}")


def شغّل_تفاعلي():
    print("لغة عربية — الوضع التفاعلي.")
    print("اكتب برنامجك سطرًا سطرًا، ثم اضغط Enter على سطر فارغ لتشغيله.")
    print("اكتب 'خروج' على سطر فارغ للإنهاء.")
    مفسر_تفاعلي = مفسر()
    الأسطر_المؤقتة = []
    while True:
        الطالع = "... " if الأسطر_المؤقتة else ">>> "
        try:
            السطر = input(الطالع)
        except EOFError:
            print()
            _نفّذ_مقطعا(مفسر_تفاعلي, الأسطر_المؤقتة)
            break
        if not الأسطر_المؤقتة and السطر.strip() == "خروج":
            break
        if السطر.strip() == "":
            if الأسطر_المؤقتة:
                _نفّذ_مقطعا(مفسر_تفاعلي, الأسطر_المؤقتة)
                الأسطر_المؤقتة = []
            continue
        الأسطر_المؤقتة.append(السطر)


def main():
    if len(sys.argv) == 1:
        شغّل_تفاعلي()
        return

    if len(sys.argv) != 2:
        print("الاستخدام: python3 run.py [اسم_الملف.arabic]")
        sys.exit(1)

    المسار = sys.argv[1]
    try:
        شغّل_ملف(المسار)
    except خطأ_لغوي as خطأ:
        print(f"خطأ: {خطأ}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(f"خطأ: الملف غير موجود: {المسار}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
