import string
import re
from getpass import getpass  # For secure password input

def check_password_strength(password: str) -> dict:
    """Analyzes password strength and returns detailed feedback."""
    
    # Initialize metrics
    metrics = {
        'length': len(password),
        'upper': False,
        'lower': False,
        'digit': False,
        'special': False,
        'common_sequence': False,
        'repeats': False
    }
    
    # Character diversity checks
    metrics['upper'] = any(c.isupper() for c in password)
    metrics['lower'] = any(c.islower() for c in password)
    metrics['digit'] = any(c.isdigit() for c in password)
    metrics['special'] = any(c in string.punctuation for c in password)
    
    # Pattern checks
    metrics['common_sequence'] = bool(re.search(r'1234|abcd|qwerty', password.lower()))
    metrics['repeats'] = bool(re.search(r'(.)\1{3,}', password))  # 4+ repeats
    
    # Calculate score
    score = 0
    
    # Length scoring (12+ recommended)
    if metrics['length'] >= 12: score += 3
    elif metrics['length'] >= 8: score += 1
    
    # Character diversity (1 point per type)
    score += sum([metrics['upper'], metrics['lower'], 
                metrics['digit'], metrics['special']])
    
    # Deductions for weak patterns
    if metrics['common_sequence']: score -= 2
    if metrics['repeats']: score -= 2
    
    return {'score': max(0, score), 'metrics': metrics}

def get_feedback(analysis: dict) -> str:
    """Generate detailed feedback based on analysis."""
    feedback = []
    m = analysis['metrics']
    
    # Length feedback
    if m['length'] < 12:
        feedback.append(f"→ Too short (min 12 chars, current: {m['length']})")
    
    # Missing character types
    missing = []
    if not m['upper']: missing.append("uppercase letters")
    if not m['lower']: missing.append("lowercase letters")
    if not m['digit']: missing.append("numbers")
    if not m['special']: missing.append("special characters")
    if missing:
        feedback.append(f"→ Add {', '.join(missing)}")
    
    # Pattern warnings
    if m['common_sequence']:
        feedback.append("→ Avoid common sequences (e.g., 1234, abcd)")
    if m['repeats']:
        feedback.append("→ Avoid repeated characters (aaaa, 1111)")
    
    # Strength rating
    if analysis['score'] >= 6:
        status = "✅ Strong"
    elif analysis['score'] >= 4:
        status = "⚠️ Moderate"
    else:
        status = "❌ Weak"
    
    return "\n".join([status] + feedback)

def check_password(password: str) -> None:
    """Complete password evaluation workflow."""
    with open("common.txt") as f:
        common_passwords = set(f.read().lower().splitlines())
    
    if password.lower() in common_passwords:
        print("🔴 Security Alert: This password is too common!")
        return
    
    analysis = check_password_strength(password)
    print("\nPassword Analysis:")
    print(get_feedback(analysis))

if __name__ == "__main__":
    while True:
        try:
            # Use getpass to prevent shoulder surfing
            password = getpass("Enter password (CTRL+C to exit): ")
            check_password(password)
            print("-" * 40)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
