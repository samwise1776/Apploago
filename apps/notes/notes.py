import customtkinter as ctk
from pathlib import Path

ctk.set_appearance_mode("dark")

NOTES_FILE = Path("notes.txt")

app = ctk.CTk()
app.title("MyTech Notes")
app.geometry("900x650")


def load_note():
    if NOTES_FILE.exists():
        textbox.delete("1.0", "end")
        textbox.insert("1.0", NOTES_FILE.read_text())


def save_note():
    NOTES_FILE.write_text(
        textbox.get("1.0", "end-1c")
    )

    status.configure(
        text="Saved"
    )


def clear_note():
    textbox.delete(
        "1.0",
        "end"
    )

    status.configure(
        text="Cleared"
    )


title = ctk.CTkLabel(
    app,
    text="Notes",
    font=("Arial", 30, "bold")
)

title.pack(
    pady=(20, 10)
)


toolbar = ctk.CTkFrame(app)

toolbar.pack(
    fill="x",
    padx=20,
    pady=10
)


ctk.CTkButton(
    toolbar,
    text="Save",
    command=save_note
).pack(
    side="left",
    padx=5,
    pady=5
)


ctk.CTkButton(
    toolbar,
    text="Clear",
    command=clear_note
).pack(
    side="left",
    padx=5,
    pady=5
)


status = ctk.CTkLabel(
    toolbar,
    text="Ready"
)

status.pack(
    side="right",
    padx=10
)


textbox = ctk.CTkTextbox(
    app,
    font=("Monospace", 16)
)

textbox.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 20)
)


load_note()

app.bind(
    "<Control-s>",
    lambda event: save_note()
)

app.mainloop()