# 🔐 Password Strength Analyzer - Web Version

A beautiful, modern web-based password strength analyzer with **real-time analysis** as you type!

## 🌐 Web Interface Features

### ✨ Real-Time Analysis
- **Instant feedback** as you type each character
- **Smooth animations** and transitions
- **Visual progress bar** (0-100 score)
- **Color-coded status** indicators
- **Show/Hide password** toggle
- **Responsive design** - works on all devices



### 📊 Analysis Metrics

**1. Overall Score (0-100)**
- Visual progress bar with gradient colors
- Status: Very Weak → Weak → Moderate → Strong → Very Strong

**2. Length Analysis**
- Real-time length checking
- Recommendations for stronger passwords

**3. Complexity Analysis**
- Live indicators for character types:
  - ✓ Lowercase letters
  - ✓ Uppercase letters
  - ✓ Digits
  - ✓ Special characters
- Instant suggestions for missing types

**4. Entropy Analysis**
- Shannon Entropy calculation
- Theoretical Entropy based on character pool
- Character pool size display

**5. Dictionary Attack Detection**
- Checks against 100+ common passwords
- Detects simple variations
- Identifies patterns (sequences, keyboard patterns, etc.)
- Visual warnings for vulnerabilities

**6. Crack Time Estimation**
- Estimates brute force attack time
- Based on 1 billion attempts/second

## 🚀 How to Run

### Option 1: Double-Click (Easiest)
1. Navigate to the project folder
2. **Double-click `index.html`**
3. Opens in your default browser

### Option 2: Right-Click
1. Right-click on `index.html`
2. Select "Open with" → Your preferred browser

### Option 3: Using Python Server
```bash
# Navigate to project directory
cd "C:\Users\dell\Documents\projects\CS  assignment"

# Start a local server (Python 3)
python -m http.server 8000

# Open browser and go to:
# http://localhost:8000
```

### Option 4: Using Live Server (VS Code)
1. Install "Live Server" extension in VS Code
2. Right-click `index.html`
3. Select "Open with Live Server"

## 📁 Web Files Structure

```
CS assignment/
│
├── index.html          # Main HTML structure
├── styles.css          # Beautiful modern styling
├── script.js           # Real-time analysis logic
│
├── Python modules (optional):
├── entropy_calculator.py
├── dictionary_checker.py
├── analyzer.py
├── gui.py
└── main.py
```

## 🎨 Interface Sections

### 1. Header
- Gradient title with modern design
- Subtitle explaining the analysis types

### 2. Password Input
- Large, clear input field
- Show/Hide password toggle button
- Focus effects and animations

### 3. Score Display
- Large score number (0-100)
- Status text with color coding
- Animated progress bar

### 4. Analysis Cards
Each card shows different metrics:
- 📏 **Length Analysis** - Character count and recommendations
- 🔤 **Complexity Analysis** - Character type indicators
- 🎲 **Entropy Analysis** - Shannon & theoretical entropy
- 📖 **Dictionary Attack** - Vulnerability warnings
- ⏱️ **Crack Time** - Estimated time to break

### 5. Tips Section
- Best practices for strong passwords
- Visual checkmarks for each tip

### 6. Footer
- Privacy notice (all analysis is local)

## 🎯 How It Works

### Real-Time Updates
```javascript
// As you type, the analyzer:
1. Calculates Shannon entropy
2. Determines character pool size
3. Checks against common passwords
4. Detects patterns
5. Estimates crack time
6. Updates all UI elements instantly
```

### Color Coding
- 🔴 **Red** (0-24): Very Weak - Critical issues
- 🟠 **Orange** (25-49): Weak - Needs improvement
- 🟡 **Yellow** (50-74): Moderate - Acceptable
- 🟢 **Light Green** (75-89): Strong - Good security
- 🟢 **Bright Green** (90-100): Very Strong - Excellent!

## 📱 Responsive Design

The interface automatically adapts to:
- 💻 Desktop computers
- 📱 Tablets
- 📱 Mobile phones

## 🔒 Privacy & Security

- ✓ **100% Local Analysis** - No data sent to servers
- ✓ **No Network Requests** - Works completely offline
- ✓ **No Data Storage** - Nothing is saved or logged
- ✓ **Client-Side Only** - All processing in your browser

## 🎓 Technical Implementation

### JavaScript Modules

**EntropyCalculator Class**
- `calculateShannonEntropy()` - Measures password randomness
- `getCharacterSpace()` - Determines character pool size
- `calculateTheoreticalEntropy()` - Maximum possible entropy

**DictionaryChecker Class**
- `checkCommonPassword()` - Matches against database
- `checkSimpleVariation()` - Detects variations
- `checkPatterns()` - Finds common patterns
- `analyze()` - Complete dictionary analysis

**PasswordAnalyzer Class**
- `analyzeLength()` - Length evaluation
- `analyzeComplexity()` - Character diversity
- `calculateCrackTime()` - Brute force estimation
- `analyze()` - Complete password analysis

**UIController Class**
- Real-time event handling
- DOM manipulation
- Visual feedback updates

## 🌟 Features Highlights

### Instant Feedback
- Updates **as you type** each character
- No need to click "Analyze" button
- Smooth, responsive animations

### Visual Indicators
- ✓ Green checkmarks for active character types
- ○ Gray circles for missing types
- Color-coded status messages
- Animated progress bar

### Smart Suggestions
- Tells you exactly what to add
- Shows which character types are missing
- Provides specific improvement tips

## 📊 Example Test Passwords

Try these in the interface:

| Password | Expected Result |
|----------|----------------|
| `password` | Very Weak - Common password |
| `Password1` | Weak - Simple variation |
| `P@ssw0rd!` | Moderate - Better but still common |
| `MyS3cur3P@ss!2024` | Strong - Good diversity |
| `aB3$xY9#mK2@pL5&` | Very Strong - Excellent! |

## 🛠️ Customization

You can easily customize:

**Colors** (in `styles.css`):
```css
.colors {
    'very_weak': '#ff4444',
    'weak': '#ff8800',
    'moderate': '#ffbb00',
    'strong': '#88cc00',
    'very_strong': '#00cc44'
}
```

**Thresholds** (in `script.js`):
```javascript
this.minLength = 8;
this.recommendedLength = 12;
this.strongLength = 16;
```

## 🎉 Try It Now!

**Just open `index.html` in your browser and start typing!**

---

**Created for CS Assignment - Modern Web-Based Password Analysis**
