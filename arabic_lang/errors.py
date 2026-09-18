"""أخطاء لغة البرمجة العربية (errors for the Arabic language)."""


class خطأ_لغوي(Exception):
    """خطأ عام في اللغة، يحمل رقم السطر عند توفره."""

    def __init__(self, رسالة, رقم_السطر=None):
        self.رسالة = رسالة
        self.رقم_السطر = رقم_السطر
        if رقم_السطر is not None:
            super().__init__(f"سطر {رقم_السطر}: {رسالة}")
        else:
            super().__init__(رسالة)


# Aliases with Latin names for tooling / IDEs that struggle with Arabic identifiers.
LanguageError = خطأ_لغوي
