"""
Password Analyzer Core Module
Combines entropy, length, and dictionary checks
"""

from entropy_calculator import EntropyCalculator
from dictionary_checker import DictionaryChecker


class PasswordAnalyzer:
    """Main password strength analyzer"""
    
    def __init__(self):
        self.min_length = 8
        self.recommended_length = 12
        self.strong_length = 16
    
    def analyze_length(self, password):
        """
        Analyze password length.
        
        Returns: dict with score, status, and message
        """
        length = len(password)
        
        if length == 0:
            return {
                'score': 0,
                'status': 'Empty',
                'message': 'Enter a password'
            }
        elif length < self.min_length:
            return {
                'score': 0,
                'status': 'Too Short',
                'message': f'Minimum {self.min_length} characters required'
            }
        elif length < self.recommended_length:
            return {
                'score': 1,
                'status': 'Weak',
                'message': f'Use at least {self.recommended_length} characters'
            }
        elif length < self.strong_length:
            return {
                'score': 2,
                'status': 'Good',
                'message': 'Good length'
            }
        else:
            return {
                'score': 3,
                'status': 'Excellent',
                'message': 'Excellent length'
            }
    
    def analyze_complexity(self, password):
        """
        Analyze password complexity (character diversity).
        
        Returns: dict with score, status, suggestions
        """
        if not password:
            return {
                'score': 0,
                'status': 'None',
                'suggestions': ['Add lowercase', 'Add uppercase', 'Add numbers', 'Add special chars']
            }
        
        char_types = EntropyCalculator.get_character_types(password)
        
        has_lowercase = char_types['lowercase']
        has_uppercase = char_types['uppercase']
        has_digits = char_types['digits']
        has_special = char_types['special']
        
        complexity_count = sum(char_types.values())
        
        suggestions = []
        if not has_lowercase:
            suggestions.append('Add lowercase letters')
        if not has_uppercase:
            suggestions.append('Add uppercase letters')
        if not has_digits:
            suggestions.append('Add numbers')
        if not has_special:
            suggestions.append('Add special characters')
        
        if complexity_count == 1:
            return {'score': 0, 'status': 'Very Weak', 'suggestions': suggestions}
        elif complexity_count == 2:
            return {'score': 1, 'status': 'Weak', 'suggestions': suggestions}
        elif complexity_count == 3:
            return {'score': 2, 'status': 'Good', 'suggestions': suggestions}
        else:
            return {'score': 3, 'status': 'Excellent', 'suggestions': []}
    
    def calculate_crack_time(self, password):
        """
        Estimate time to crack password using brute force.
        Assumes 1 billion attempts per second.
        
        Returns: human-readable time string
        """
        pool_size = EntropyCalculator.calculate_character_space(password)
        if pool_size == 0:
            return "Instantly"
        
        length = len(password)
        total_combinations = pool_size ** length
        
        # 1 billion attempts per second
        attempts_per_second = 1e9
        seconds_to_crack = total_combinations / (2 * attempts_per_second)
        
        if seconds_to_crack < 1:
            return "< 1 second"
        elif seconds_to_crack < 60:
            return f"{seconds_to_crack:.1f} seconds"
        elif seconds_to_crack < 3600:
            return f"{seconds_to_crack/60:.1f} minutes"
        elif seconds_to_crack < 86400:
            return f"{seconds_to_crack/3600:.1f} hours"
        elif seconds_to_crack < 31536000:
            return f"{seconds_to_crack/86400:.1f} days"
        elif seconds_to_crack < 31536000 * 100:
            return f"{seconds_to_crack/31536000:.1f} years"
        elif seconds_to_crack < 31536000 * 1000:
            return f"{seconds_to_crack/(31536000*100):.0f} centuries"
        else:
            return "Millions of years"
    
    def analyze(self, password):
        """
        Perform comprehensive password analysis.
        
        Returns: dict with all analysis results
        """
        if not password:
            return {
                'password_length': 0,
                'character_pool_size': 0,
                'shannon_entropy': 0,
                'theoretical_entropy': 0,
                'length_analysis': self.analyze_length(password),
                'complexity_analysis': self.analyze_complexity(password),
                'dictionary_analysis': {'is_vulnerable': False, 'vulnerabilities': []},
                'crack_time': 'N/A',
                'overall_score': 0,
                'overall_status': 'Empty'
            }
        
        # Calculate metrics
        shannon_entropy = EntropyCalculator.calculate_shannon_entropy(password)
        theoretical_entropy = EntropyCalculator.calculate_theoretical_entropy(password)
        pool_size = EntropyCalculator.calculate_character_space(password)
        
        # Analyze components
        length_analysis = self.analyze_length(password)
        complexity_analysis = self.analyze_complexity(password)
        dictionary_analysis = DictionaryChecker.analyze(password)
        crack_time = self.calculate_crack_time(password)
        
        # Calculate overall score (0-100)
        length_score = length_analysis['score'] * 25
        complexity_score = complexity_analysis['score'] * 25
        
        # Entropy score (0-25)
        if theoretical_entropy < 28:
            entropy_score = 0
        elif theoretical_entropy < 36:
            entropy_score = 10
        elif theoretical_entropy < 60:
            entropy_score = 15
        else:
            entropy_score = 25
        
        # Dictionary score (0-25)
        dictionary_score = 0 if dictionary_analysis['is_vulnerable'] else 25
        
        overall_score = length_score + complexity_score + entropy_score + dictionary_score
        
        # Determine overall status
        if overall_score < 25:
            overall_status = 'Very Weak'
        elif overall_score < 50:
            overall_status = 'Weak'
        elif overall_score < 75:
            overall_status = 'Moderate'
        elif overall_score < 90:
            overall_status = 'Strong'
        else:
            overall_status = 'Very Strong'
        
        return {
            'password_length': len(password),
            'character_pool_size': pool_size,
            'shannon_entropy': round(shannon_entropy, 2),
            'theoretical_entropy': round(theoretical_entropy, 2),
            'length_analysis': length_analysis,
            'complexity_analysis': complexity_analysis,
            'dictionary_analysis': dictionary_analysis,
            'crack_time': crack_time,
            'overall_score': overall_score,
            'overall_status': overall_status
        }
