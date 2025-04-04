# gui.py
import tkinter as tk
from tkinter import ttk
import os

class AFOQTGUI:
    def __init__(self, root, subtests):
        self.root = root
        self.subtests = subtests
        self.current_subtest_index = -1
        self.current_question_index = 0
        self.correct_answers = 0
        self.root.title("AFOQT Simulation")
        self.root.geometry("800x600")
        self.setup_ui()

    def setup_ui(self):
        self.question_label = tk.Label(self.root, text="", wraplength=700, justify="left")
        self.question_label.pack(pady=10)

        # Frame for attitude indicator and compass (for Instrument Comprehension)
        self.instrument_frame = tk.Frame(self.root)
        self.instrument_frame.pack(pady=5)
        self.attitude_label = tk.Label(self.instrument_frame)
        self.attitude_label.pack(side=tk.LEFT, padx=10)
        self.compass_label = tk.Label(self.instrument_frame)
        self.compass_label.pack(side=tk.LEFT, padx=10)

        # Frame for option images (for subtests with images)
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=5)
        self.option_labels = [tk.Label(self.options_frame) for _ in range(4)]
        for i, label in enumerate(self.option_labels):
            label.pack(side=tk.LEFT, padx=5)

        self.options_var = tk.StringVar()
        self.options_menu = ttk.Combobox(self.root, textvariable=self.options_var, state="readonly")
        self.options_menu.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=5)

        self.timer_label = tk.Label(self.root, text="Time Remaining: 00:00")
        self.timer_label.pack(pady=5)

        self.question_counter_label = tk.Label(self.root, text="Question 0 of 0")
        self.question_counter_label.pack(pady=5)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.next_subtest()

    def next_subtest(self):
        self.current_subtest_index += 1
        if self.current_subtest_index < len(self.subtests):
            subtest = self.subtests[self.current_subtest_index]
            print(f"Starting subtest: {subtest['name']}")
            self.current_question_index = 0
            self.questions, self.answers, self.data = subtest["gen_func"]()
            print(f"Data length: {len(self.data) if self.data is not None else 'None'}")
            self.correct_answers = 0
            self.time_remaining = int(subtest["time_minutes"] * 60)
            print(f"Timer reset to {self.time_remaining} seconds")
            self.timer_running = True
            self.update_timer()
            self.show_question()
        else:
            self.show_results()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_index])
            opts = self.questions[self.current_question_index].split("Options: ")[-1].split(", ")
            self.options_menu["values"] = opts
            self.options_var.set("")
            self.question_counter_label.config(text=f"Question {self.current_question_index + 1} of {len(self.questions)}")

            # Display images for Instrument Comprehension
            if self.subtests[self.current_subtest_index]["name"] == "Instrument Comprehension" and self.data is not None:
                try:
                    if isinstance(self.data, list) and self.current_question_index < len(self.data):
                        idx = self.data[self.current_question_index]
                        # Attitude Indicator
                        attitude_file = f"images/instrument/attitude_{idx}.png"
                        if os.path.exists(attitude_file):
                            attitude_img = tk.PhotoImage(file=attitude_file)
                            self.attitude_label.config(image=attitude_img)
                            self.attitude_label.image = attitude_img
                        else:
                            print(f"Attitude file not found: {attitude_file}")
                            self.attitude_label.config(image="")
                        # Compass
                        compass_file = f"images/instrument/compass_{idx}.png"
                        if os.path.exists(compass_file):
                            compass_img = tk.PhotoImage(file=compass_file)
                            self.compass_label.config(image=compass_img)
                            self.compass_label.image = compass_img
                        else:
                            print(f"Compass file not found: {compass_file}")
                            self.compass_label.config(image="")
                        # Options
                        for i, opt in enumerate(["a", "b", "c", "d"]):
                            opt_file = f"images/instrument/option_{opt}_{idx}.png"
                            if os.path.exists(opt_file):
                                opt_img = tk.PhotoImage(file=opt_file)
                                self.option_labels[i].config(image=opt_img)
                                self.option_labels[i].image = opt_img
                            else:
                                print(f"Option file not found: {opt_file}")
                                self.option_labels[i].config(image="")
                    else:
                        print(f"Data mismatch: {self.data}")
                        self.attitude_label.config(image="")
                        self.compass_label.config(image="")
                        for label in self.option_labels:
                            label.config(image="")
                except Exception as e:
                    print(f"Image error: {e}")
                    self.attitude_label.config(image="")
                    self.compass_label.config(image="")
                    for label in self.option_labels:
                        label.config(image="")
            else:
                # For subtests without images, clear the image labels
                self.attitude_label.config(image="")
                self.compass_label.config(image="")
                for label in self.option_labels:
                    label.config(image="")
        else:
            self.next_subtest()

    def submit_answer(self):
        user_answer = self.options_var.get()
        correct_answer = self.answers[self.current_question_index]
        if user_answer == correct_answer:
            self.correct_answers += 1
        self.current_question_index += 1
        self.show_question()

    def update_timer(self):
        if self.timer_running and self.time_remaining > 0:
            mins, secs = divmod(self.time_remaining, 60)
            self.timer_label.config(text=f"Time Remaining: {mins:02d}:{secs:02d}")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_remaining <= 0:
            self.timer_running = False
            self.next_subtest()

    def show_results(self):
        self.question_label.config(text="Simulation Complete!")
        self.options_menu.pack_forget()
        self.submit_button.pack_forget()
        self.timer_label.pack_forget()
        self.question_counter_label.pack_forget()
        score = self.correct_answers
        self.result_label.config(text=f"Total Correct Answers for Last Subtest: {score}")
        self.timer_running = False