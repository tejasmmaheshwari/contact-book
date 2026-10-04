import tkinter as tk
from tkinter import messagebox

from contact_book import load_contacts, save_contacts # type: ignore


class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("420x700")
        self.root.resizable(False, False)

        self.contacts = load_contacts()

        # Main background
        self.root.configure(bg="#f5f5f5")

        self.create_header()
        self.create_search_bar()
        self.create_contact_area()
        self.create_bottom_bar()

        self.display_contacts()

    # --------------------------------------------------
    # HEADER
    # --------------------------------------------------

    def create_header(self):
        header = tk.Frame(
            self.root,
            bg="#ffffff",
            height=80
        )
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Contacts",
            font=("Arial", 25, "bold"),
            bg="#ffffff",
            fg="#222222"
        )
        title.pack(side="left", padx=25, pady=20)

        count = len(self.contacts)

        self.contact_count = tk.Label(
            header,
            text=f"{count} contacts",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#777777"
        )
        self.contact_count.pack(side="right", padx=20)

    # --------------------------------------------------
    # SEARCH BAR
    # --------------------------------------------------

    def create_search_bar(self):
        search_frame = tk.Frame(
            self.root,
            bg="#f5f5f5"
        )
        search_frame.pack(fill="x", padx=20, pady=15)

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 13),
            relief="flat",
            bg="#ffffff"
        )
        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=9
        )

        self.search_entry.insert(0, "Search contacts...")

        self.search_entry.bind(
            "<FocusIn>",
            self.clear_search_placeholder
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_contacts
        )

    def clear_search_placeholder(self, event):
        if self.search_entry.get() == "Search contacts...":
            self.search_entry.delete(0, tk.END)

    def search_contacts(self, event=None):
        search_text = self.search_entry.get().lower()

        if search_text == "search contacts...":
            search_text = ""

        filtered_contacts = []

        for contact in self.contacts:
            if search_text in contact["name"].lower():
                filtered_contacts.append(contact)

        self.display_contacts(filtered_contacts)

    # --------------------------------------------------
    # CONTACT DISPLAY AREA
    # --------------------------------------------------

    def create_contact_area(self):
        self.contact_frame = tk.Frame(
            self.root,
            bg="#f5f5f5"
        )
        self.contact_frame.pack(
            fill="both",
            expand=True,
            padx=20
        )

    def display_contacts(self, contacts=None):

        for widget in self.contact_frame.winfo_children():
            widget.destroy()

        if contacts is None:
            contacts = self.contacts

        if not contacts:
            empty_label = tk.Label(
                self.contact_frame,
                text="No contacts found",
                font=("Arial", 14),
                bg="#f5f5f5",
                fg="#888888"
            )
            empty_label.pack(pady=80)
            return

        for contact in contacts:
            self.create_contact_card(contact)

    def create_contact_card(self, contact):

        card = tk.Frame(
            self.contact_frame,
            bg="#ffffff",
            bd=0
        )
        card.pack(
            fill="x",
            pady=6
        )

        # Initial circle
        initial = contact["name"][0].upper()

        initial_label = tk.Label(
            card,
            text=initial,
            font=("Arial", 18, "bold"),
            bg="#dddddd",
            fg="#333333",
            width=3,
            height=2
        )
        initial_label.pack(
            side="left",
            padx=12,
            pady=10
        )

        # Contact information
        info_frame = tk.Frame(
            card,
            bg="#ffffff"
        )
        info_frame.pack(
            side="left",
            fill="both",
            expand=True,
            pady=10
        )

        name_label = tk.Label(
            info_frame,
            text=contact["name"],
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            fg="#222222",
            anchor="w"
        )
        name_label.pack(fill="x")

        phone_label = tk.Label(
            info_frame,
            text=contact["phone"],
            font=("Arial", 10),
            bg="#ffffff",
            fg="#666666",
            anchor="w"
        )
        phone_label.pack(fill="x")

        email_label = tk.Label(
            info_frame,
            text=contact["email"],
            font=("Arial", 9),
            bg="#ffffff",
            fg="#888888",
            anchor="w"
        )
        email_label.pack(fill="x")

        # Buttons
        button_frame = tk.Frame(
            card,
            bg="#ffffff"
        )
        button_frame.pack(
            side="right",
            padx=10
        )

        edit_button = tk.Button(
            button_frame,
            text="Edit",
            command=lambda: self.edit_contact(contact),
            relief="flat",
            bg="#eeeeee",
            fg="#333333",
            padx=8
        )
        edit_button.pack(pady=3)

        delete_button = tk.Button(
            button_frame,
            text="Delete",
            command=lambda: self.delete_contact(contact),
            relief="flat",
            bg="#eeeeee",
            fg="#333333",
            padx=5
        )
        delete_button.pack(pady=3)

    # --------------------------------------------------
    # ADD CONTACT
    # --------------------------------------------------

    def add_contact(self):

        window = tk.Toplevel(self.root)
        window.title("Add Contact")
        window.geometry("350x350")
        window.resizable(False, False)
        window.configure(bg="#ffffff")

        tk.Label(
            window,
            text="New Contact",
            font=("Arial", 20, "bold"),
            bg="#ffffff"
        ).pack(pady=20)

        # Name
        tk.Label(
            window,
            text="Name",
            bg="#ffffff",
            font=("Arial", 10)
        ).pack(anchor="w", padx=30)

        name_entry = tk.Entry(
            window,
            font=("Arial", 12)
        )
        name_entry.pack(
            fill="x",
            padx=30,
            pady=(5, 15)
        )

        # Phone
        tk.Label(
            window,
            text="Phone Number",
            bg="#ffffff",
            font=("Arial", 10)
        ).pack(anchor="w", padx=30)

        phone_entry = tk.Entry(
            window,
            font=("Arial", 12)
        )
        phone_entry.pack(
            fill="x",
            padx=30,
            pady=(5, 15)
        )

        # Email
        tk.Label(
            window,
            text="Email",
            bg="#ffffff",
            font=("Arial", 10)
        ).pack(anchor="w", padx=30)

        email_entry = tk.Entry(
            window,
            font=("Arial", 12)
        )
        email_entry.pack(
            fill="x",
            padx=30,
            pady=(5, 20)
        )

        def save_new_contact():

            name = name_entry.get().strip()
            phone = phone_entry.get().strip()
            email = email_entry.get().strip()

            if not name:
                messagebox.showerror(
                    "Error",
                    "Please enter a name."
                )
                return

            if not phone.isdigit() or len(phone) != 10:
                messagebox.showerror(
                    "Invalid Phone Number",
                    "Please enter a valid 10-digit phone number."
                )
                return

            if not email:
                messagebox.showerror(
                    "Error",
                    "Please enter an email address."
                )
                return

            contact = {
                "name": name,
                "phone": phone,
                "email": email
            }

            self.contacts.append(contact)
            save_contacts(self.contacts)

            self.update_contact_count()
            self.display_contacts()

            window.destroy()

            messagebox.showinfo(
                "Success",
                "Contact added successfully!"
            )

        tk.Button(
            window,
            text="Save Contact",
            command=save_new_contact,
            font=("Arial", 11, "bold"),
            relief="flat",
            bg="#dddddd",
            padx=20,
            pady=8
        ).pack()

    # --------------------------------------------------
    # EDIT CONTACT
    # --------------------------------------------------

    def edit_contact(self, contact):

        window = tk.Toplevel(self.root)
        window.title("Edit Contact")
        window.geometry("350x350")
        window.resizable(False, False)
        window.configure(bg="#ffffff")

        tk.Label(
            window,
            text="Edit Contact",
            font=("Arial", 20, "bold"),
            bg="#ffffff"
        ).pack(pady=20)

        # Name
        tk.Label(
            window,
            text="Name",
            bg="#ffffff"
        ).pack(anchor="w", padx=30)

        name_entry = tk.Entry(
            window,
            font=("Arial", 12)
        )
        name_entry.pack(
            fill="x",
            padx=30,
            pady=(5, 15)
        )

        name_entry.insert(0, contact["name"])

        # Phone
        tk.Label(
            window,
            text="Phone Number",
            bg="#ffffff"
        ).pack(anchor="w", padx=30)

        phone_entry = tk.Entry(
            window,
            font=("Arial", 12)
        )
        phone_entry.pack(
            fill="x",
            padx=30,
            pady=(5, 15)
        )

        phone_entry.insert(0, contact["phone"])

        # Email
        tk.Label(
            window,
            text="Email",
            bg="#ffffff"
        ).pack(anchor="w", padx=30)

        email_entry = tk.Entry(
            window,
            font=("Arial", 12)
        )
        email_entry.pack(
            fill="x",
            padx=30,
            pady=(5, 20)
        )

        email_entry.insert(0, contact["email"])

        def save_changes():

            new_name = name_entry.get().strip()
            new_phone = phone_entry.get().strip()
            new_email = email_entry.get().strip()

            if not new_name:
                messagebox.showerror(
                    "Error",
                    "Name cannot be empty."
                )
                return

            if not new_phone.isdigit() or len(new_phone) != 10:
                messagebox.showerror(
                    "Invalid Phone Number",
                    "Please enter a valid 10-digit phone number."
                )
                return

            if not new_email:
                messagebox.showerror(
                    "Error",
                    "Email cannot be empty."
                )
                return

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email

            save_contacts(self.contacts)

            self.display_contacts()

            window.destroy()

            messagebox.showinfo(
                "Success",
                "Contact updated successfully!"

            )

        tk.Button(
            window,
            text="Save Changes",
            command=save_changes,
            font=("Arial", 11, "bold"),
            relief="flat",
            bg="#dddddd",
            padx=20,
            pady=8
        ).pack()

    # --------------------------------------------------
    # DELETE CONTACT
    # --------------------------------------------------

    def delete_contact(self, contact):

        confirmation = messagebox.askyesno(
            "Delete Contact",
            f"Are you sure you want to delete {contact['name']}?"
        )

        if confirmation:

            self.contacts.remove(contact)

            save_contacts(self.contacts)

            self.update_contact_count()
            self.display_contacts()

            messagebox.showinfo(
                "Deleted",
                "Contact deleted successfully!"
            )

    # --------------------------------------------------
    # BOTTOM BAR
    # --------------------------------------------------

    def create_bottom_bar(self):

        bottom_frame = tk.Frame(
            self.root,
            bg="#ffffff",
            height=70
        )
        bottom_frame.pack(
            fill="x",
            side="bottom"
        )

        add_button = tk.Button(
            bottom_frame,
            text="+  Add Contact",
            command=self.add_contact,
            font=("Arial", 13, "bold"),
            relief="flat",
            bg="#eeeeee",
            fg="#222222",
            padx=20,
            pady=10
        )
        add_button.pack(pady=12)

    # --------------------------------------------------
    # UPDATE CONTACT COUNT
    # --------------------------------------------------

    def update_contact_count(self):

        count = len(self.contacts)

        self.contact_count.config(
            text=f"{count} contacts"
        )


# ------------------------------------------------------
# START GUI
# ------------------------------------------------------

root = tk.Tk()

app = ContactBookGUI(root)

root.mainloop()