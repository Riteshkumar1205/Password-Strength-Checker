import string
import re
import hashlib
import requests
from getpass import getpass  # For secure password input

def load_banned_passwords(filename="common.txt"):
    """Load banned passwords from a file, case-insensitive."""
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            banned = set(line.strip().lower() for line in f)
        return banned
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Skipping banned password check.")
        return set()

def calculate_entropy(password):
    """Estimate password entropy in bits (simplified)."""
    char_pool = 0
    if any(c.isupper() for c in password): char_pool += 26
    if any(c.islower() for c in password): char_pool += 26
    if any(c.isdigit() for c in password): char_pool += 10
    if any(c in string.punctuation for c in password): char_pool += 32
    if char_pool == 0: char_pool = 1  # Prevent log(0)
    entropy = len(password) * (char_pool ** 0.5)  # Simplified for demo
    return int(entropy)

def check_password_strength(password):
    """Analyze password strength and return detailed metrics."""
    metrics = {
        'length': len(password),
        'upper': any(c.isupper() for c in password),
        'lower': any(c.islower() for c in password),
        'digit': any(c.isdigit() for c in password),
        'special': any(c in string.punctuation for c in password),
        'common_sequence': bool(re.search(r'1234|abcd|qwerty', password.lower())),
        'repeats': bool(re.search(r'(.)\1{3,}', password)),
        'entropy': calculate_entropy(password)
    }
    score = 0
    # Length scoring
    if metrics['length'] >= 16: score += 3
    elif metrics['length'] >= 12: score += 2
    elif metrics['length'] >= 8: score += 1
    # Character diversity
    score += sum([metrics['upper'], metrics['lower'], metrics['digit'], metrics['special']])
    # Penalties for weak patterns
    if metrics['common_sequence']: score -= 2
    if metrics['repeats']: score -= 2
    # Bonus for high entropy
    if metrics['entropy'] > 50: score += 1
    metrics['score'] = max(0, score)
    return metrics

def is_password_breached(password):
    """Check if a password has been exposed in a breach using the HIBP API."""
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        for line in response.text.splitlines():
            if line.split(':')[0] == suffix:
                return True, int(line.split(':')[1])  # Return True and count of breaches
        return False, 0
    except Exception as e:
        print(f"Error checking password: {e}")
        return False, 0

def get_feedback(analysis):
    """Generate detailed feedback based on analysis."""
    feedback = []
    m = analysis
    # Length feedback
    if m['length'] < 12:
        feedback.append(f"→ Password is too short (min 12 chars, current: {m['length']})")
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
    if m['score'] >= 6:
        status = "✅ Strong"
    elif m['score'] >= 4:
        status = "⚠️ Moderate"
    else:
        status = "❌ Weak"
    # Entropy info
    feedback.append(f"→ Estimated entropy: {m['entropy']} bits")
    return "\n".join([status] + feedback)

def suggest_password():
    """Generate a strong password suggestion."""
    import secrets
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(16))

def main():
    """Main function to run the password checker."""
    banned_passwords = load_banned_passwords()
    while True:
        try:
            password = getpass("Enter password (CTRL+C to exit): ")
            if not password:
                print("Password cannot be empty. Try again.")
                continue
            # Check if password is banned
            if password.lower() in banned_passwords:
                print("\n🔴 Security Alert: This password is too common!")
                continue
            # HIBP API check
            is_breached, breach_count = is_password_breached(password)
            if is_breached:
                print(f"\n🔴 Security Alert: This password has been exposed in {breach_count} data breaches!")
            else:
                print("\n✅ This password has not been found in any known breaches.")
            # Analyze password
            analysis = check_password_strength(password)
            print("\nPassword Analysis:")
            print(get_feedback(analysis))
            # Offer a suggestion if weak
            if analysis['score'] < 4:
                print(f"\n💡 Suggestion: Try a stronger password like: {suggest_password()}")
            print("-" * 40)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
