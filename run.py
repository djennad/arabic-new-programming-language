#!/usr/bin/env python3
"""نقطة تشغيل لغة البرمجة العربية من سطر الأوامر.

الاستخدام:
    python3 run.py برنامجي.arabic
"""

import sys

from arabic_lang import خطأ_لغوي, شغّل_ملف


def main():
    if len(sys.argv) != 2:
        print("الاستخدام: python3 run.py <اسم_الملف.arabic>")
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
