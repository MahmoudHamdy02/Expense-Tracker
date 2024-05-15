import customtkinter as ctk

class TransactionFrame(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x400")
        self.title("Transaction")

        # Create a send button
        self.send_button = ctk.CTkButton(self, text="Send", command=self.send_transaction)
        self.send_button.pack(pady=10)

        # Create a receive button
        self.receive_button = ctk.CTkButton(self, text="Receive", command=self.receive_transaction)
        self.receive_button.pack(pady=10)

    def send_transaction(self):
        # Code to send transaction goes here
        pass

    def receive_transaction(self):
        # Code to receive transaction goes here
        pass