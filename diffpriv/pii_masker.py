import re

class PIISanitizer:
    EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    PHONE_REGEX = r'\+?[0-9]{10,13}'

    def sanitize(self, text):
        text = re.sub(self.EMAIL_REGEX, "[REDACTED_EMAIL]", text)
        text = re.sub(self.PHONE_REGEX, "[REDACTED_PHONE]", text)
        return text
