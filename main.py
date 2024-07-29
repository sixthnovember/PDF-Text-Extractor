import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox
from PyPDF2 import PdfReader

def open_file():
    """
    Opens the selected PDF file and extracts the text which gets displayed in the text box.
    """
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a pdf file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        reader = PdfReader(file)
        text_content = ""
        for page in reader.pages:
            text_content += page.extract_text() + "\n"
        text_box.config(state=tk.NORMAL)
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, text_content)
        text_box.config(state=tk.DISABLED)
        browse_text.set("Browse")
        save_button.config(state=tk.NORMAL)

def save_file():
    """
    Saves the text from the text box to a .txt file.
    """
    file = asksaveasfile(defaultextension=".txt", filetypes=[("Text file", "*.txt")], mode='wb')
    if file:
        text = text_box.get(1.0, tk.END)
        file.write(text.encode('utf-8'))
        file.close()
        messagebox.showinfo("Success", "File has been saved successfully!")

# Initialize the main window
root = tk.Tk()
root.title("PDF Text Extractor")
root.geometry("450x450")

# Title label
text_title = tk.Label(root, text="Select a PDF file to extract the text from:", font="Title")
text_title.grid(columnspan=3, column=0, row=0, pady=10)

# Browse button
browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable=browse_text, command=open_file, font="Title", bg="#fab400", fg="black", height=2, width=15)
browse_text.set("Browse")
browse_button.grid(column=1, row=1, pady=10)

# Text box for extracted text
text_box = tk.Text(root, height=10, width=50, padx=15, pady=15, wrap=tk.WORD)
text_box.grid(column=1, row=2, pady=10)
text_box.config(state=tk.DISABLED)

# Scrollbar for the text box
scrollbar = tk.Scrollbar(root, command=text_box.yview)
text_box['yscrollcommand'] = scrollbar.set
scrollbar.grid(column=2, row=2, sticky='ns')

# Save button
save_button = tk.Button(root, text="Save", command=save_file, font="Title", bg="#fab400", fg="black", height=2, width=15, state=tk.DISABLED)
save_button.grid(column=1, row=3, pady=10)

# Run main loop
root.mainloop()