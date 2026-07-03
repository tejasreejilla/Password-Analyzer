// Password Strength Analyzer - JavaScript Module
// Real-time password analysis with entropy, length, and dictionary checks

// Common passwords database
const COMMON_PASSWORDS = new Set([
    'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567',
    'letmein', 'trustno1', 'dragon', 'baseball', 'iloveyou', 'master', 'sunshine',
    'ashley', 'bailey', 'passw0rd', 'shadow', '123123', '654321', 'superman',
    'qazwsx', 'michael', 'football', 'password1', 'admin', 'welcome', 'login',
    'princess', 'solo', 'qwertyuiop', 'starwars', 'password123', 'hello',
    'freedom', 'whatever', 'jordan', 'hunter', 'buster', 'thomas',
    'robert', 'ranger', 'george', 'jennifer', 'batman', 'computer', 'michelle',
    'jessica', 'pepper', 'zxcvbnm', 'charlie', 'asdfgh', 'andrew', 'joshua',
    'daniel', 'matthew', 'qwerty123', 'access', 'flower',
    'lovely', 'amanda', 'pass', 'admin123', 'root', 'user', 'test', 'guest',
    '123456789', '12345', '1234', '111111', '1234567890', '000000', 'password!',
    'welcome123', 'qwerty12345', 'password12345', 'iloveyou123',
    'sunshine1', 'princess1', 'monkey123', 'dragon123', 'baseball1', 'football1',
    'shadow123', 'master123', 'superman1', 'batman123', 'welcome1', 'hello123'
]);

// Common patterns
const COMMON_PATTERNS = [
    { regex: /(.)\1{2,}/, name: 'Repeated characters' },
    { regex: /(012|123|234|345|456|567|678|789|890)/, name: 'Sequential numbers' },
    { regex: /(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)/i, name: 'Sequential letters' },
    { regex: /(qwerty|asdfgh|zxcvbn)/i, name: 'Keyboard pattern' }
];

// Entropy Calculator
class EntropyCalculator {
    static calculateShannonEntropy(password) {
        if (!password) return 0;
        
        const charCounts = {};
        for (const char of password) {
            charCounts[char] = (charCounts[char] || 0) + 1;
        }
        
        const length = password.length;
        let entropy = 0;
        
        for (const count of Object.values(charCounts)) {
            const probability = count / length;
            entropy -= probability * Math.log2(probability);
        }
        
        return entropy * length;
    }
    
    static getCharacterSpace(password) {
        let poolSize = 0;
        
        if (/[a-z]/.test(password)) poolSize += 26;
        if (/[A-Z]/.test(password)) poolSize += 26;
        if (/[0-9]/.test(password)) poolSize += 10;
        if (/[^a-zA-Z0-9]/.test(password)) poolSize += 32;
        
        return poolSize;
    }
    
    static calculateTheoreticalEntropy(password) {
        const poolSize = this.getCharacterSpace(password);
        if (poolSize === 0) return 0;
        
        return password.length * Math.log2(poolSize);
    }
    
    static getCharacterTypes(password) {
        return {
            lowercase: /[a-z]/.test(password),
            uppercase: /[A-Z]/.test(password),
            digits: /[0-9]/.test(password),
            special: /[^a-zA-Z0-9]/.test(password)
        };
    }
}

// Dictionary Checker
class DictionaryChecker {
    static checkCommonPassword(password) {
        const lower = password.toLowerCase();
        if (COMMON_PASSWORDS.has(lower)) {
            return { isCommon: true, message: 'Password is in common passwords list' };
        }
        return { isCommon: false };
    }
    
    static checkSimpleVariation(password) {
        const lower = password.toLowerCase();
        const base = lower.replace(/[0-9!@#$%^&*()_+=\-\[\]{}|;:,.<>?/~`]+$/, '');
        
        if (COMMON_PASSWORDS.has(base)) {
            return { isVariation: true, message: `Simple variation of '${base}'` };
        }
        return { isVariation: false };
    }
    
    static checkPatterns(password) {
        const lower = password.toLowerCase();
        
        for (const pattern of COMMON_PATTERNS) {
            if (pattern.regex.test(lower)) {
                return { hasPattern: true, name: pattern.name };
            }
        }
        return { hasPattern: false };
    }
    
    static checkDictionaryWord(password) {
        if (password.length >= 4 && /^[a-zA-Z]+$/.test(password)) {
            return { isWord: true, message: 'Single dictionary word' };
        }
        return { isWord: false };
    }
    
    static analyze(password) {
        if (!password) {
            return { isVulnerable: false, vulnerabilities: [] };
        }
        
        const vulnerabilities = [];
        
        const commonCheck = this.checkCommonPassword(password);
        if (commonCheck.isCommon) vulnerabilities.push(commonCheck.message);
        
        const variationCheck = this.checkSimpleVariation(password);
        if (variationCheck.isVariation) vulnerabilities.push(variationCheck.message);
        
        const patternCheck = this.checkPatterns(password);
        if (patternCheck.hasPattern) vulnerabilities.push(`Contains ${patternCheck.name}`);
        
        const wordCheck = this.checkDictionaryWord(password);
        if (wordCheck.isWord) vulnerabilities.push(wordCheck.message);
        
        return {
            isVulnerable: vulnerabilities.length > 0,
            vulnerabilities
        };
    }
}

// Password Analyzer
class PasswordAnalyzer {
    constructor() {
        this.minLength = 8;
        this.recommendedLength = 12;
        this.strongLength = 16;
    }
    
    analyzeLength(password) {
        const length = password.length;
        
        if (length === 0) {
            return { score: 0, status: 'Empty', message: 'Enter a password' };
        } else if (length < this.minLength) {
            return { score: 0, status: 'Too Short', message: `Minimum ${this.minLength} characters required` };
        } else if (length < this.recommendedLength) {
            return { score: 1, status: 'Weak', message: `Use at least ${this.recommendedLength} characters` };
        } else if (length < this.strongLength) {
            return { score: 2, status: 'Good', message: 'Good length' };
        } else {
            return { score: 3, status: 'Excellent', message: 'Excellent length' };
        }
    }
    
    analyzeComplexity(password) {
        if (!password) {
            return {
                score: 0,
                status: 'None',
                suggestions: ['Add lowercase', 'Add uppercase', 'Add numbers', 'Add special chars']
            };
        }
        
        const charTypes = EntropyCalculator.getCharacterTypes(password);
        const complexityCount = Object.values(charTypes).filter(v => v).length;
        
        const suggestions = [];
        if (!charTypes.lowercase) suggestions.push('Add lowercase letters');
        if (!charTypes.uppercase) suggestions.push('Add uppercase letters');
        if (!charTypes.digits) suggestions.push('Add numbers');
        if (!charTypes.special) suggestions.push('Add special characters');
        
        let score, status;
        if (complexityCount === 1) {
            score = 0; status = 'Very Weak';
        } else if (complexityCount === 2) {
            score = 1; status = 'Weak';
        } else if (complexityCount === 3) {
            score = 2; status = 'Good';
        } else {
            score = 3; status = 'Excellent';
        }
        
        return { score, status, suggestions, charTypes };
    }
    
    calculateCrackTime(password) {
        const poolSize = EntropyCalculator.getCharacterSpace(password);
        if (poolSize === 0) return 'Instantly';
        
        const length = password.length;
        const totalCombinations = Math.pow(poolSize, length);
        const attemptsPerSecond = 1e9;
        const secondsToCrack = totalCombinations / (2 * attemptsPerSecond);
        
        if (secondsToCrack < 1) return '< 1 second';
        if (secondsToCrack < 60) return `${secondsToCrack.toFixed(1)} seconds`;
        if (secondsToCrack < 3600) return `${(secondsToCrack / 60).toFixed(1)} minutes`;
        if (secondsToCrack < 86400) return `${(secondsToCrack / 3600).toFixed(1)} hours`;
        if (secondsToCrack < 31536000) return `${(secondsToCrack / 86400).toFixed(1)} days`;
        if (secondsToCrack < 31536000 * 100) return `${(secondsToCrack / 31536000).toFixed(1)} years`;
        if (secondsToCrack < 31536000 * 1000) return `${(secondsToCrack / (31536000 * 100)).toFixed(0)} centuries`;
        return 'Millions of years';
    }
    
    analyze(password) {
        if (!password) {
            return {
                passwordLength: 0,
                characterPoolSize: 0,
                shannonEntropy: 0,
                theoreticalEntropy: 0,
                lengthAnalysis: this.analyzeLength(password),
                complexityAnalysis: this.analyzeComplexity(password),
                dictionaryAnalysis: { isVulnerable: false, vulnerabilities: [] },
                crackTime: 'N/A',
                overallScore: 0,
                overallStatus: 'Empty'
            };
        }
        
        const shannonEntropy = EntropyCalculator.calculateShannonEntropy(password);
        const theoreticalEntropy = EntropyCalculator.calculateTheoreticalEntropy(password);
        const poolSize = EntropyCalculator.getCharacterSpace(password);
        
        const lengthAnalysis = this.analyzeLength(password);
        const complexityAnalysis = this.analyzeComplexity(password);
        const dictionaryAnalysis = DictionaryChecker.analyze(password);
        const crackTime = this.calculateCrackTime(password);
        
        const lengthScore = lengthAnalysis.score * 25;
        const complexityScore = complexityAnalysis.score * 25;
        
        let entropyScore;
        if (theoreticalEntropy < 28) entropyScore = 0;
        else if (theoreticalEntropy < 36) entropyScore = 10;
        else if (theoreticalEntropy < 60) entropyScore = 15;
        else entropyScore = 25;
        
        const dictionaryScore = dictionaryAnalysis.isVulnerable ? 0 : 25;
        
        const overallScore = lengthScore + complexityScore + entropyScore + dictionaryScore;
        
        let overallStatus;
        if (overallScore < 25) overallStatus = 'Very Weak';
        else if (overallScore < 50) overallStatus = 'Weak';
        else if (overallScore < 75) overallStatus = 'Moderate';
        else if (overallScore < 90) overallStatus = 'Strong';
        else overallStatus = 'Very Strong';
        
        return {
            passwordLength: password.length,
            characterPoolSize: poolSize,
            shannonEntropy: Math.round(shannonEntropy * 100) / 100,
            theoreticalEntropy: Math.round(theoreticalEntropy * 100) / 100,
            lengthAnalysis,
            complexityAnalysis,
            dictionaryAnalysis,
            crackTime,
            overallScore,
            overallStatus
        };
    }
}

// UI Controller
class UIController {
    constructor() {
        this.analyzer = new PasswordAnalyzer();
        this.passwordInput = document.getElementById('password-input');
        this.toggleBtn = document.getElementById('toggle-visibility');
        this.eyeIcon = document.getElementById('eye-icon');
        
        this.initEventListeners();
    }
    
    initEventListeners() {
        this.passwordInput.addEventListener('input', () => this.onPasswordChange());
        this.toggleBtn.addEventListener('click', () => this.togglePasswordVisibility());
    }
    
    togglePasswordVisibility() {
        const type = this.passwordInput.type === 'password' ? 'text' : 'password';
        this.passwordInput.type = type;
        this.eyeIcon.textContent = type === 'password' ? '👁️' : '🙈';
    }
    
    getStatusClass(status) {
        const statusLower = status.toLowerCase();
        if (statusLower.includes('very weak') || statusLower.includes('too short')) return 'status-very-weak';
        if (statusLower.includes('weak')) return 'status-weak';
        if (statusLower.includes('moderate') || statusLower.includes('good')) return 'status-moderate';
        if (statusLower.includes('strong')) return 'status-strong';
        if (statusLower.includes('very strong') || statusLower.includes('excellent')) return 'status-very-strong';
        return '';
    }
    
    onPasswordChange() {
        const password = this.passwordInput.value;
        const analysis = this.analyzer.analyze(password);
        
        this.updateUI(analysis);
    }
    
    updateUI(analysis) {
        // Update overall score
        document.getElementById('score-value').textContent = `${analysis.overallScore}/100`;
        const statusElement = document.getElementById('score-status');
        statusElement.textContent = analysis.overallStatus;
        statusElement.className = 'score-status ' + this.getStatusClass(analysis.overallStatus);
        
        // Update progress bar
        const progressBar = document.getElementById('progress-bar');
        progressBar.style.width = `${analysis.overallScore}%`;
        
        // Update length analysis
        const lengthStatus = document.getElementById('length-status');
        lengthStatus.textContent = `Status: ${analysis.lengthAnalysis.status}`;
        lengthStatus.className = 'status-text ' + this.getStatusClass(analysis.lengthAnalysis.status);
        document.getElementById('length-detail').textContent = analysis.lengthAnalysis.message;
        
        // Update complexity analysis
        const complexityStatus = document.getElementById('complexity-status');
        complexityStatus.textContent = `Status: ${analysis.complexityAnalysis.status}`;
        complexityStatus.className = 'status-text ' + this.getStatusClass(analysis.complexityAnalysis.status);
        
        // Update complexity indicators
        const charTypes = analysis.complexityAnalysis.charTypes || {};
        this.updateIndicator('ind-lowercase', charTypes.lowercase);
        this.updateIndicator('ind-uppercase', charTypes.uppercase);
        this.updateIndicator('ind-digits', charTypes.digits);
        this.updateIndicator('ind-special', charTypes.special);
        
        // Update suggestions
        const suggestions = analysis.complexityAnalysis.suggestions;
        const suggestionsElement = document.getElementById('complexity-suggestions');
        if (suggestions && suggestions.length > 0) {
            suggestionsElement.textContent = 'Suggestions: ' + suggestions.join(', ');
        } else {
            suggestionsElement.textContent = '✓ All character types present';
            suggestionsElement.style.color = '#00ff66';
        }
        
        // Update entropy analysis
        document.getElementById('entropy-shannon').textContent = 
            `Shannon Entropy: ${analysis.shannonEntropy} bits`;
        document.getElementById('entropy-theoretical').textContent = 
            `Theoretical Entropy: ${analysis.theoreticalEntropy} bits`;
        document.getElementById('entropy-pool').textContent = 
            `Character Pool: ${analysis.characterPoolSize}`;
        
        // Update dictionary analysis
        const dictStatus = document.getElementById('dictionary-status');
        const dictWarnings = document.getElementById('dictionary-warnings');
        
        if (analysis.dictionaryAnalysis.isVulnerable) {
            dictStatus.textContent = 'Status: ⚠️ VULNERABLE';
            dictStatus.className = 'status-text status-very-weak';
            
            const warningsList = analysis.dictionaryAnalysis.vulnerabilities
                .map(v => `• ${v}`)
                .join('<br>');
            dictWarnings.innerHTML = `<strong>Issues:</strong><br>${warningsList}`;
            dictWarnings.className = 'warning-box vulnerable';
        } else {
            dictStatus.textContent = 'Status: ✓ SECURE';
            dictStatus.className = 'status-text status-very-strong';
            dictWarnings.textContent = '✓ No common password patterns detected';
            dictWarnings.className = 'warning-box secure';
        }
        
        // Update crack time
        document.getElementById('crack-time').textContent = 
            `Brute Force (1B attempts/sec): ${analysis.crackTime}`;
    }
    
    updateIndicator(id, isActive) {
        const element = document.getElementById(id);
        if (isActive) {
            element.classList.add('active');
        } else {
            element.classList.remove('active');
        }
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    new UIController();
});
