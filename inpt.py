from classifier import InjectionClassifier
cls = InjectionClassifier()

def is_malicious_input(text: str) -> bool:
    if cls.is_malicious(text):
        return True
    return False