"""
Dictionary Attack Checker Module
Checks for common passwords and patterns
"""

import re


class DictionaryChecker:
    """Check passwords against dictionary attacks and common patterns"""
    
    # Common passwords list (top 100 most common passwords)
    COMMON_PASSWORDS = {
        'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567',
        'letmein', 'trustno1', 'dragon', 'baseball', 'iloveyou', 'master', 'sunshine',
        'ashley', 'bailey', 'passw0rd', 'shadow', '123123', '654321', 'superman',
        'qazwsx', 'michael', 'football', 'password1', 'admin', 'welcome', 'login',
        'princess', 'solo', 'qwertyuiop', 'starwars', 'password123', 'hello',
        'freedom', 'whatever', 'trustno1', 'jordan', 'hunter', 'buster', 'thomas',
        'robert', 'ranger', 'george', 'jennifer', 'batman', 'computer', 'michelle',
        'jessica', 'pepper', 'zxcvbnm', 'charlie', 'asdfgh', 'andrew', 'joshua',
        'daniel', 'matthew', 'qwerty123', 'letmein', 'access', 'master', 'flower',
        'lovely', 'amanda', 'pass', 'admin123', 'root', 'user', 'test', 'guest',
        '123456789', '12345', '1234', '111111', '1234567890', '000000', 'password!',
        'welcome123', 'abc123', 'qwerty12345', 'password12345', 'iloveyou123',
        'sunshine1', 'princess1', 'monkey123', 'dragon123', 'baseball1', 'football1',
        'shadow123', 'master123', 'superman1', 'batman123', 'welcome1', 'hello123'
    }
    
    # Common patterns that weaken passwords
    COMMON_PATTERNS = [
        (r'(.)\1{2,}', 'Repeated characters'),
        (r'(012|123|234|345|456|567|678|789|890)', 'Sequential numbers'),
        (r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', 'Sequential letters'),
        (r'(qwerty|asdfgh|zxcvbn)', 'Keyboard pattern'),
    ]
    
    @staticmethod
    def check_common_password(password):
        """
        Check if password is in common passwords list.
        
        Returns: (is_common, message)
        """
        password_lower = password.lower()
        
        if password_lower in DictionaryChecker.COMMON_PASSWORDS:
            return True, "Password is in the common passwords list"
        
        return False, None
    
    @staticmethod
    def check_simple_variation(password):
        """
        Check if password is a simple variation of common password.
        
        Returns: (is_variation, message)
        """
        password_lower = password.lower()
        
        # Remove numbers and special chars from end
        base_password = re.sub(r'[0-9!@#$%^&*()_+=\-\[\]{}|;:,.<>?/~`]+$', '', password_lower)
        
        if base_password in DictionaryChecker.COMMON_PASSWORDS:
            return True, f"Simple variation of '{base_password}'"
        
        return False, None
    
    @staticmethod
    def check_patterns(password):
        """
        Check for common patterns in password.
        
        Returns: (has_pattern, pattern_name)
        """
        password_lower = password.lower()
        
        for pattern, name in DictionaryChecker.COMMON_PATTERNS:
            if re.search(pattern, password_lower):
                return True, name
        
        return False, None
    
    @staticmethod
    def check_dictionary_word(password):
        """
        Check if password is just a dictionary word.
        
        Returns: (is_word, message)
        """
        if len(password) >= 4 and password.lower().isalpha():
            return True, "Single dictionary word"
        
        return False, None
    
    @staticmethod
    def analyze(password):
        """
        Perform complete dictionary attack analysis.
        
        Returns: dict with vulnerability status and details
        """
        if not password:
            return {
                'is_vulnerable': False,
                'vulnerabilities': []
            }
        
        vulnerabilities = []
        
        # Check common password
        is_common, msg = DictionaryChecker.check_common_password(password)
        if is_common:
            vulnerabilities.append(msg)
        
        # Check simple variation
        is_variation, msg = DictionaryChecker.check_simple_variation(password)
        if is_variation:
            vulnerabilities.append(msg)
        
        # Check patterns
        has_pattern, pattern_name = DictionaryChecker.check_patterns(password)
        if has_pattern:
            vulnerabilities.append(f"Contains {pattern_name}")
        
        # Check dictionary word
        is_word, msg = DictionaryChecker.check_dictionary_word(password)
        if is_word:
            vulnerabilities.append(msg)
        
        return {
            'is_vulnerable': len(vulnerabilities) > 0,
            'vulnerabilities': vulnerabilities
        }
