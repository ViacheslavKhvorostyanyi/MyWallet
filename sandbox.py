import tkinter as tk
from wallet_app import *


class App_GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #input fields
        self.input_transaction_value = tk.Entry(self)
        self.input_transaction_value.grid(row = 9, column = 1)
        self.input_transaction_value.insert(0, "10")

        self.input_account_value = tk.Entry(self)
        self.input_account_value.grid(row=4, column=1)
        self.input_account_value.insert(0, "100")

        self.input_account_name = tk.Entry(self)
        self.input_account_name.grid(row=2, column=1)
        self.input_account_name.insert(0, "cash")

        self.input_category_name = tk.Entry(self)
        self.input_category_name.grid(row=4, column=2)
        self.input_category_name.insert(0, "transport")
        #lebels
        self.input_account_name_label = tk.Label(self, text ="Enter Account name:")
        self.input_account_name_label.grid(row = 1, column = 1)

        self.input_account_value_label = tk.Label(self, text="Enter Account value:")
        self.input_account_value_label.grid(row=3, column=1)

        self.input_category_name_label = tk.Label(self, text="Enter Category name:")
        self.input_category_name_label.grid(row=3, column=2)

        self.input_transaction_value_label = tk.Label(self, text="Enter Transaction value:")
        self.input_transaction_value_label.grid(row=8, column=1)

        self.input_transaction_value_label = tk.Label(self, text="Select account:")
        self.input_transaction_value_label.grid(row=6, column=1)

        self.input_transaction_value_label = tk.Label(self, text="Select category:")
        self.input_transaction_value_label.grid(row=6, column=2)

        self.account_display_label = tk.Label(self, text="Current account value:")
        self.account_display_label.grid(row=1, column=2)

        self.account_display = tk.Label(self)
        self.account_display.grid(row=2, column=2)

        self.display_transaction_label = tk.Label(self,text="Last Transaction:")
        self.display_transaction_label.grid(row=8,column=2)

        self.display_transaction = tk.Label(self)
        self.display_transaction_label.grid(row=9,column=2)

        #buttons
        self.add_account_btn = tk.Button(self, text="Add Account", command=self.account_callback)
        self.add_account_btn.grid(row=5, column=1)

        self.add_transaction_btn = tk.Button(self, text="Add Transaction", command=self.transaction_callback)
        self.add_transaction_btn.grid(row=10, column=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.grid(row=11, column=1)

        self.add_category = tk.Button(self, text="Add category", command=self.category_callback)
        self.add_category.grid(row=5, column=2)
        #listboxes
        self.account_listbox=tk.Listbox(self, height=5, selectmode='SINGLE',exportselection = 0)
        self.account_listbox.grid(row = 7, column = 1)

        self.category_listbox = tk.Listbox(self, height=5, selectmode='SINGLE',)

        self.category_listbox.grid(row=7, column=2)
        #window settings
        self.master.title('My wallet')
        # self.master.geometry("500x300")

    """
    account_callback function responsibilities:
       -gets data for account creating
       -creates accounts and account list
       -add and displays account name to listbox 
    """

    def account_callback(self):
        self.entered_value = Decimal(self.input_account_value.get()).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        self.entered_name = self.input_account_name.get()
        account = Account(self.entered_name, self.entered_value)
        wallet.add_account(account)
        self.account_listbox.insert(tk.END, account.account_name)


    """
    transaction_callback function responsibilities:
       -gets data for transaction creating
       -creates transaction 
       -make calculations with selected from listbox account
        and transaction
    """
    def transaction_callback(self):

        self.entered_value = Decimal(self.input_transaction_value.get()).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        selected_category_name = self.category_listbox.get(self.category_listbox.curselection(), last=None)
        selected_account_key = self.account_listbox.get(self.account_listbox.curselection(), last=None)
        transaction = Transaction(self.entered_value, wallet.account_list[selected_account_key], selected_category_name)
        wallet.add_transaction(transaction)
        self.account_display['text'] = str(wallet.account_list[selected_account_key].account_value) + " UAH"
        self.account_display['fg'] = '#42f477'
        self.account_display['bg'] = "#000000"
        print(wallet.transaction_list)


    def category_callback(self):
        category_name = self.input_category_name.get()
        self.category_listbox.insert(tk.END, category_name)







root = tk.Tk()
app = App_GUI(master=root)
app.mainloop()




