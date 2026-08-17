from diffpriv.mechanisms import DifferentialPrivacyEngine
from diffpriv.pii_masker import PIISanitizer

def process_pipeline():
    sanitizer = PIISanitizer()
    dp = DifferentialPrivacyEngine(epsilon=0.5)
    sample_text = "Contact user at test@example.com with balance $5400"
    scrubbed = sanitizer.sanitize(sample_text)
    print(f"Scrubbed Output: {scrubbed}")

if __name__ == '__main__':
    process_pipeline()
