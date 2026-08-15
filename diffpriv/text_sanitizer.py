import re

class TextSanitizer:
    SSN_REGEX = r'\b\d{3}-\d{2}-\d{4}\b'
    CREDIT_CARD_REGEX = r'\b(?:\d[ -]*?){13,16}\b'

    def redact_financial_pii(self, text):
        text = re.sub(self.SSN_REGEX, "[REDACTED_SSN]", text)
        text = re.sub(self.CREDIT_CARD_REGEX, "[REDACTED_CARD]", text)
        return text
