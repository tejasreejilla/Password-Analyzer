"""
GUI Module - Real-time Password Strength Interface
Shows password strength as user types
"""

import tkinter as tk
from tkinter import ttk
from analyzer import PasswordAnalyzer


class PasswordStrengthGUI:
    """GUI for real-time password strength analysis"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Strength Analyzer")
        self.root.geometry("700x800")
        self.root.resizable(False, False)
        
        # Set color scheme
        self.colors = {
            'bg': '#1e1e1e',
            'fg': '#ffffff',
            'input_bg': '#2d2d2d',
            'very_weak': '#ff4444',
            'weak': '#ff8800',
            'moderate': '#ffbb00',
            'strong': '#88cc00',
            'very_strong': '#00cc44'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        self.analyzer = PasswordAnalyzer()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        
        # Title
        title_frame = tk.Frame(self.root, bg=self.colors['bg'])
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🔐 Password Strength Analyzer",
            font=('Arial', 24, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Real-time analysis based on Entropy, Length & Dictionary Attacks",
            font=('Arial', 10),
            bg=self.colors['bg'],
            fg='#888888'
        )
        subtitle_label.pack()
        
        # Password Input Section
        input_frame = tk.Frame(self.root, bg=self.colors['bg'])
        input_frame.pack(pady=20, padx=40, fill='x')
        
        input_label = tk.Label(
            input_frame,
            text="Enter Password:",
            font=('Arial', 12, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        input_label.pack(anchor='w')
        
        # Password entry with show/hide
        entry_container = tk.Frame(input_frame, bg=self.colors['bg'])
        entry_container.pack(fill='x', pady=5)
        
        self.password_var = tk.StringVar()
        self.password_var.trace('w', self.on_password_change)
        
        self.password_entry = tk.Entry(
            entry_container,
            textvariable=self.password_var,
            font=('Arial', 14),
            bg=self.colors['input_bg'],
            fg=self.colors['fg'],
            insertbackground=self.colors['fg'],
            relief='flat',
            show='●'
        )
        self.password_entry.pack(side='left', fill='x', expand=True, ipady=8, ipadx=10)
        
        self.show_password_var = tk.BooleanVar()
        show_btn = tk.Checkbutton(
            entry_container,
            text="Show",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            bg=self.colors['bg'],
            fg=self.colors['fg'],
            selectcolor=self.colors['input_bg'],
            activebackground=self.colors['bg'],
            activeforeground=self.colors['fg']
        )
        show_btn.pack(side='left', padx=10)
        
        # Overall Score Section
        score_frame = tk.Frame(self.root, bg=self.colors['bg'])
        score_frame.pack(pady=20, padx=40, fill='x')
        
        self.score_label = tk.Label(
            score_frame,
            text="Score: 0/100",
            font=('Arial', 18, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['fg']
        )
        self.score_label.pack()
        
        self.status_label = tk.Label(
            score_frame,
            text="Empty",
            font=('Arial', 14),
            bg=self.colors['bg'],
            fg='#888888'
        )
        self.status_label.pack()
        
        # Progress bar
        self.progress = ttk.Progressbar(
            score_frame,
            length=600,
            mode='determinate',
            maximum=100
        )
        self.progress.pack(pady=10)
        
        # Analysis Results Section
        results_frame = tk.Frame(self.root, bg=self.colors['bg'])
        results_frame.pack(pady=10, padx=40, fill='both', expand=True)
        
        # Length Analysis
        self.create_analysis_section(results_frame, "📏 Length Analysis", 0)
        self.length_status = tk.Label(
            results_frame,
            text="Status: -",
            font=('Arial', 10),
            bg=self.colors['bg'],
            fg='#888888',
            anchor='w'
        )
        self.length_status.grid(row=1, column=0, sticky='w', padx=20, pady=2)
        
        # Complexity Analysis
        self.create_analysis_section(results_frame, "🔤 Complexity Analysis", 2)
        self.complexity_status = tk.Label(
            results_frame,
            text="Status: -",
            font=('Arial', 10),
            bg=self.colors['bg'],
            fg='#888888',
            anchor='w'
        )
        self.complexity_status.grid(row=3, column=0, sticky='w', padx=20, pady=2)
        
        self.complexity_suggestions = tk.Label(
            results_frame,
            text="",
            font=('Arial', 9),
            bg=self.colors['bg'],
            fg='#ffbb00',
            anchor='w',
            wraplength=600
        )
        self.complexity_suggestions.grid(row=4, column=0, sticky='w', padx=20, pady=2)
        
        # Entropy Analysis
        self.create_analysis_section(results_frame, "🎲 Entropy Analysis", 5)
        self.entropy_info = tk.Label(
            results_frame,
            text="Shannon Entropy: 0 bits\nTheoretical Entropy: 0 bits",
            font=('Arial', 10),
            bg=self.colors['bg'],
            fg='#888888',
            anchor='w',
            justify='left'
        )
        self.entropy_info.grid(row=6, column=0, sticky='w', padx=20, pady=2)
        
        # Dictionary Attack Analysis
        self.create_analysis_section(results_frame, "📖 Dictionary Attack Analysis", 7)
        self.dictionary_status = tk.Label(
            results_frame,
            text="Status: -",
            font=('Arial', 10),
            bg=self.colors['bg'],
            fg='#888888',
            anchor='w'
        )
        self.dictionary_status.grid(row=8, column=0, sticky='w', padx=20, pady=2)
        
        self.dictionary_warnings = tk.Label(
            results_frame,
            text="",
            font=('Arial', 9),
            bg=self.colors['bg'],
            fg='#ff4444',
            anchor='w',
            wraplength=600,
            justify='left'
        )
        self.dictionary_warnings.grid(row=9, column=0, sticky='w', padx=20, pady=2)
        
        # Crack Time
        self.create_analysis_section(results_frame, "⏱️ Estimated Crack Time", 10)
        self.crack_time_label = tk.Label(
            results_frame,
            text="Brute Force: N/A",
            font=('Arial', 10),
            bg=self.colors['bg'],
            fg='#888888',
            anchor='w'
        )
        self.crack_time_label.grid(row=11, column=0, sticky='w', padx=20, pady=2)
    
    def create_analysis_section(self, parent, title, row):
        """Create a section header"""
        label = tk.Label(
            parent,
            text=title,
            font=('Arial', 12, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['fg'],
            anchor='w'
        )
        label.grid(row=row, column=0, sticky='w', pady=(10, 5))
    
    def toggle_password_visibility(self):
        """Toggle password visibility"""
        if self.show_password_var.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='●')
    
    def get_status_color(self, status):
        """Get color based on status"""
        status_lower = status.lower()
        if 'very weak' in status_lower or 'too short' in status_lower:
            return self.colors['very_weak']
        elif 'weak' in status_lower:
            return self.colors['weak']
        elif 'moderate' in status_lower or 'good' in status_lower:
            return self.colors['moderate']
        elif 'strong' in status_lower:
            return self.colors['strong']
        elif 'very strong' in status_lower or 'excellent' in status_lower:
            return self.colors['very_strong']
        else:
            return '#888888'
    
    def on_password_change(self, *args):
        """Called when password input changes - updates analysis in real-time"""
        password = self.password_var.get()
        analysis = self.analyzer.analyze(password)
        
        # Update overall score
        score = analysis['overall_score']
        status = analysis['overall_status']
        
        self.score_label.config(text=f"Score: {score}/100")
        self.status_label.config(text=status, fg=self.get_status_color(status))
        self.progress['value'] = score
        
        # Update length analysis
        length_info = analysis['length_analysis']
        self.length_status.config(
            text=f"Status: {length_info['status']} - {length_info['message']}",
            fg=self.get_status_color(length_info['status'])
        )
        
        # Update complexity analysis
        complexity_info = analysis['complexity_analysis']
        self.complexity_status.config(
            text=f"Status: {complexity_info['status']}",
            fg=self.get_status_color(complexity_info['status'])
        )
        
        if complexity_info['suggestions']:
            suggestions_text = "Suggestions: " + ", ".join(complexity_info['suggestions'])
            self.complexity_suggestions.config(text=suggestions_text)
        else:
            self.complexity_suggestions.config(text="✓ All character types present")
        
        # Update entropy analysis
        entropy_text = (
            f"Shannon Entropy: {analysis['shannon_entropy']} bits\n"
            f"Theoretical Entropy: {analysis['theoretical_entropy']} bits\n"
            f"Character Pool: {analysis['character_pool_size']}"
        )
        self.entropy_info.config(text=entropy_text)
        
        # Update dictionary analysis
        dict_info = analysis['dictionary_analysis']
        if dict_info['is_vulnerable']:
            self.dictionary_status.config(text="Status: ⚠️ VULNERABLE", fg=self.colors['very_weak'])
            warnings_text = "Issues:\n• " + "\n• ".join(dict_info['vulnerabilities'])
            self.dictionary_warnings.config(text=warnings_text)
        else:
            self.dictionary_status.config(text="Status: ✓ SECURE", fg=self.colors['very_strong'])
            self.dictionary_warnings.config(text="No common password patterns detected")
        
        # Update crack time
        self.crack_time_label.config(
            text=f"Brute Force (1B attempts/sec): {analysis['crack_time']}"
        )


def run_gui():
    """Run the GUI application"""
    root = tk.Tk()
    app = PasswordStrengthGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
