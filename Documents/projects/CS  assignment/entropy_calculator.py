"""
Entropy Calculator Module
Handles Shannon entropy and theoretical entropy calculations
"""

import math
from collections import Counter
import string


class EntropyCalculator:
    """Calculate various entropy metrics for passwords"""
    
    @staticmethod
    def calculate_shannon_entropy(password):
        """
        Calculate Shannon entropy of the password.
        Higher entropy = more unpredictable/random
        
        Formula: H = -Σ(p(x) * log2(p(x)))
        where p(x) is the probability of character x
        
        Returns: entropy in bits
        """
        if not password:
            return 0
        
        # Count character frequencies
        char_counts = Counter(password)
        length = len(password)
        
        # Calculate Shannon entropy
        entropy = 0
        for count in char_counts.values():
            probability = count / length
            entropy -= probability * math.log2(probability)
        
        # Normalize by password length to get bits of entropy
        entropy_bits = entropy * length
        
        return entropy_bits
    
    @staticmethod
    def calculate_character_space(password):
        """
        Calculate the character space (pool size) used in the password.
        Larger character space = stronger password
        
        Returns: pool size (int)
        """
        has_lowercase = any(c.islower() for c in password)
        has_uppercase = any(c.isupper() for c in password)
        has_digits = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        pool_size = 0
        if has_lowercase:
            pool_size += 26
        if has_uppercase:
            pool_size += 26
        if has_digits:
            pool_size += 10
        if has_special:
            pool_size += 32  # Common special characters
        
        return pool_size
    
    @staticmethod
    def calculate_theoretical_entropy(password):
        """
        Calculate theoretical maximum entropy based on character space and length.
        Formula: E = log2(N^L) = L * log2(N)
        where N = character space, L = password length
        
        Returns: theoretical entropy in bits
        """
        pool_size = EntropyCalculator.calculate_character_space(password)
        if pool_size == 0:
            return 0
        
        length = len(password)
        theoretical_entropy = length * math.log2(pool_size)
        
        return theoretical_entropy
    
    @staticmethod
    def get_character_types(password):
        """
        Get which character types are present in the password.
        
        Returns: dict with boolean values for each type
        """
        return {
            'lowercase': any(c.islower() for c in password),
            'uppercase': any(c.isupper() for c in password),
            'digits': any(c.isdigit() for c in password),
            'special': any(c in string.punctuation for c in password)
        }
