# gui.py
import tkinter as tk
from tkinter import messagebox
import random
import time

class AFOQTGUI:
    def __init__(self, root, subtests):
        self.root = root
        self.subtests = subtests
        self.current_subtest = 0
        self.questions, self.answers, self.data = [], [], []
        self.current_question = 0
        self.time_remaining = 0
        self.timer_running = False
        self.user_answers = []  # To store user's answers for scoring

        # Set window size and title
        self.root.title("AFOQT Study Simulation")
        self.root.geometry("600x400")  # Set a reasonable window size

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Initialize GUI elements
        self.subtest_label = tk.Label(self.main_frame, text="", font=("Arial", 14, "bold"))
        self.subtest_label.pack(anchor="nw")

        self.timer_label = tk.Label(self.main_frame, text="Time Remaining: 00:00", font=("Arial", 12))
        self.timer_label.pack(anchor="ne")

        self.question_label = tk.Label(self.main_frame, text="", font=("Arial", 12), wraplength=550, justify="left")
        self.question_label.pack(anchor="w", pady=10)

        # Frame for options
        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.pack(fill="x", pady=5)

        # Variable to store the user's selected option
        self.selected_option = tk.StringVar()
        self.option_buttons = []

        # Submit button
        self.submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_answer, state="disabled")
        self.submit_button.pack(pady=10)

        # Load the first subtest
        self.load_subtest()

    def load_subtest(self):
        # Clear previous subtest content
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        self.option_buttons.clear()
        self.selected_option.set("")

        # Load the new subtest
        subtest = self.subtests[self.current_subtest]
        gen_func = subtest["gen_func"]
        num_questions = subtest["num_questions"]
        self.time_remaining = int(subtest["time_minutes"] * 60)  # Convert minutes to seconds

        # Generate questions and select the required number
        all_questions, all_answers, all_data = gen_func()
        indices = random.sample(range(len(all_questions)), min(num_questions, len(all_questions)))
        self.questions = [all_questions[i] for i in indices]
        self.answers = [all_answers[i] for i in indices]
        self.data = [all_data[i] for i in indices]

        # Update subtest label
        self.subtest_label.config(text=f"Subtest {self.current_subtest + 1}: {subtest['name']}")

        # Start the timer
        self.timer_running = True
        self.update_timer()

        # Display the first question
        self.current_question = 0
        self.display_question()

    def update_timer(self):
        if self.timer_running and self.time_remaining > 0:
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            self.timer_label.config(text=f"Time Remaining: {minutes:02d}:{seconds:02d}")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)  # Update every second
        elif self.time_remaining <= 0:
            self.timer_running = False
            self.timer_label.config(text="Time Remaining: 00:00")
            messagebox.showinfo("Time's Up", "Time is up for this subtest!")
            self.next_subtest()

    def display_question(self):
        # Clear previous options
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        self.option_buttons.clear()
        self.selected_option.set("")
        self.submit_button.config(state="disabled")

        # Update question label
        question_text = f"Question {self.current_question + 1} of {len(self.questions)}\n{self.questions[self.current_question]}"
        self.question_label.config(text=question_text)

        # Parse the options from the question text
        question_lines = self.questions[self.current_question].split("\n")
        option_lines = [line for line in question_lines if line.startswith(("A:", "B:", "C:", "D:"))]
        options = [line.split(":", 1)[1].strip() for line in option_lines]

        # Create radio buttons for options
        for i, option in enumerate(option_lines):
            label = option.split(":", 1)[0].strip()  # e.g., "A"
            rb = tk.Radiobutton(
                self.options_frame,
                text=option,
                variable=self.selected_option,
                value=label,
                font=("Arial", 10),
                anchor="w",
                command=self.enable_submit
            )
            rb.pack(fill="x", pady=2)
            self.option_buttons.append(rb)

        # For debugging: print to console
        print(f"Displaying question {self.current_question + 1} of subtest {self.current_subtest + 1}")
        print(self.questions[self.current_question])
        print(f"Correct answer: {self.answers[self.current_question]}")

    def enable_submit(self):
        # Enable the submit button once an option is selected
        self.submit_button.config(state="normal")

    def submit_answer(self):
        # Record the user's answer
        selected_label = self.selected_option.get()
        correct_label = self.answers[self.current_question]
        is_correct = selected_label == correct_label
        self.user_answers.append({
            "subtest": self.subtests[self.current_subtest]["name"],
            "question": self.current_question + 1,
            "selected": selected_label,
            "correct": correct_label,
            "is_correct": is_correct
        })

        # Provide feedback (optional)
        if is_correct:
            messagebox.showinfo("Feedback", "Correct!")
        else:
            messagebox.showinfo("Feedback", f"Incorrect. The correct answer was {correct_label}.")

        # Move to the next question
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.timer_running = False
            self.next_subtest()

    def next_subtest(self):
        self.current_subtest += 1
        if self.current_subtest < len(self.subtests):
            self.load_subtest()
        else:
            # End of test
            self.display_results()
            self.root.quit()

    def display_results(self):
        # Calculate scores
        total_correct = sum(1 for answer in self.user_answers if answer["is_correct"])
        total_questions = len(self.user_answers)

        # Group by subtest
        subtest_scores = {}
        for answer in self.user_answers:
            subtest = answer["subtest"]
            if subtest not in subtest_scores:
                subtest_scores[subtest] = {"correct": 0, "total": 0}
            subtest_scores[subtest]["total"] += 1
            if answer["is_correct"]:
                subtest_scores[subtest]["correct"] += 1

        # Display results
        result_text = "Test Completed!\n\nOverall Score:\n"
        result_text += f"{total_correct}/{total_questions} ({total_correct/total_questions*100:.1f}%)\n\n"
        result_text += "Subtest Scores:\n"
        for subtest, scores in subtest_scores.items():
            correct = scores["correct"]
            total = scores["total"]
            result_text += f"{subtest}: {correct}/{total} ({correct/total*100:.1f}%)\n"

        messagebox.showinfo("Test Results", result_text)