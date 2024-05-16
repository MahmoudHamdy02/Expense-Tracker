import customtkinter as ctk
from PIL import Image
from CTkMessagebox import CTkMessagebox
import os

class TransactionFrame(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x400")
        self.title("Transaction")

        # Create a frame for the initial state
        self.initial_frame = ctk.CTkFrame(self)
        self.initial_frame.pack(fill="both", expand=True)

        self.sendFrame = ctk.CTkFrame(self)
        self.receiveFrame = ctk.CTkFrame(self)

        # Create a label asking for the type of transaction
        self.transaction_label = ctk.CTkLabel(self.initial_frame, text="What is the type of transaction?", font=ctk.CTkFont(size=25, weight="bold"))
        self.transaction_label.pack(pady=(120, 20))

        # Create a frame for the buttons
        self.button_frame = ctk.CTkFrame(self.initial_frame, fg_color="transparent")
        self.button_frame.pack(pady=10)
        sendImage = ctk.CTkImage(light_image=Image.open(os.path.join("GUI", "images", "money-send.png")))
        # Create a send button
        self.send_button = ctk.CTkButton(
            self.button_frame,
            image=sendImage,
            text="Send", font=ctk.CTkFont(size=15),
            command=self.send_transaction, 
            height=45, 
            width=100
            )
        self.send_button.pack(side="left", padx=20)
        recieveImage = ctk.CTkImage(light_image=Image.open(os.path.join("GUI", "images", "money-recive.png")))
        # Create a receive button
        self.receive_button = ctk.CTkButton(
            self.button_frame, 
            image=recieveImage,
            text="Receive", font=ctk.CTkFont(size=15), 
            command=self.receive_transaction, 
            height=45, 
            width=100)
        self.receive_button.pack(side="left", padx=20)

        # Create an entry field for the recipient's name
        self.name_label = ctk.CTkLabel(self.sendFrame, text="Recipient's Name:", font=ctk.CTkFont(size=15, weight="bold"))
        self.name_label.pack(pady=10)
        self.name_entry = ctk.CTkEntry(self.sendFrame, placeholder_text="Name")
        self.name_entry.pack()


        # Create a "Select from Contacts" button
        self.select_button = ctk.CTkButton(self.sendFrame, text="Select from Contacts", command=self.select_from_contacts, height=20, width=100)
        self.select_button.pack(pady=10)

        # Create an entry field for the amount
        self.amount_label = ctk.CTkLabel(self.sendFrame, text="Amount:", font=ctk.CTkFont(size=15, weight="bold"))
        self.amount_label.pack()
        self.amount_entry = ctk.CTkEntry(self.sendFrame, placeholder_text="Amount")
        self.amount_entry.pack(pady=10)

        # Create a text box for the description
        self.description_label = ctk.CTkLabel(self.sendFrame, text="Description:", font=ctk.CTkFont(size=15, weight="bold"))
        self.description_label.pack()
        self.description_entry = ctk.CTkTextbox(self.sendFrame, height=50, width=150)
        self.description_entry.pack(pady=20)
        self.description_entry.insert("0.0", "Enter description here ...")

        #Create a Confirm button
        self.confirm_button = ctk.CTkButton(self.sendFrame, text="Confirm", command=self.confirmTransaction, height=30, width=100)
        self.confirm_button.pack()

        # Create a "Back" button
        self.back_button = ctk.CTkButton(self.sendFrame, text="Cancel", command=self.go_back, height=30, width=100, fg_color="#DB3E39", hover_color="#821D1A")
        self.back_button.pack(pady=10)

        # Initially hide the send frame
        self.sendFrame.pack_forget()

        self.recieve_name_label = ctk.CTkLabel(self.receiveFrame, text="Sender's Name:", font=ctk.CTkFont(size=15, weight="bold"))
        self.recieve_name_label.pack(pady=10)
        self.recieve_name_entry = ctk.CTkEntry(self.receiveFrame, placeholder_text="Name")
        self.recieve_name_entry.pack()

        self.recieve_amount_label = ctk.CTkLabel(self.receiveFrame, text="Amount:", font=ctk.CTkFont(size=15, weight="bold"))
        self.recieve_amount_label.pack()
        self.recieve_amount_entry = ctk.CTkEntry(self.receiveFrame, placeholder_text="Amount")
        self.recieve_amount_entry.pack(pady=10)

        self.recieve_description_label = ctk.CTkLabel(self.receiveFrame, text="Description:", font=ctk.CTkFont(size=15, weight="bold"))
        self.recieve_description_label.pack()
        self.recieve_description_entry = ctk.CTkTextbox(self.receiveFrame, height=50, width=150)
        self.recieve_description_entry.pack(pady=20)
        self.recieve_description_entry.insert("0.0", "Enter description here ...")

        self.recieve_confirm_button = ctk.CTkButton(self.receiveFrame, text="Confirm", command=self.confirmRecieve, height=30, width=100)
        self.recieve_confirm_button.pack()

        self.recieve_back_button = ctk.CTkButton(self.receiveFrame, text="Cancel", command=self.go_back, height=30, width=100, fg_color="#DB3E39", hover_color="#821D1A")
        self.recieve_back_button.pack(pady=10)


    def send_transaction(self):
        self.initial_frame.pack_forget()
        self.sendFrame.pack(fill="both", expand=True)

    def confirmTransaction(self):
        self.master.doneTransaction(int(self.amount_entry.get()))
        self.destroy()
        CTkMessagebox(title="Confirm Transaction", message="Transaction Successful", icon="check")

    def receive_transaction(self):
        self.initial_frame.pack_forget()
        self.receiveFrame.pack(fill="both", expand=True)

    def confirmRecieve(self):
        self.master.doneTransaction(0)
        name = str(self.recieve_name_entry.get())
        self.destroy()
        CTkMessagebox(title="Confirm Transaction", message=f"A Request had been sent to {name}", icon="check")

    def select_from_contacts(self):
        # Code to select from contacts goes here
        pass

    def go_back(self):
        self.sendFrame.pack_forget()
        self.initial_frame.pack(fill="both", expand=True)

