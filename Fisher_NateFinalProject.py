import os 
from tkinter import *
from tkinter import messagebox
import re

# create the window

root = Tk()
root.title("Item List")
root.geometry("800x600")

#just to close the starter window cause i cannot figure out how to otherwise.
def starter_window():
    start_window = Tk()
    start_window.title("Beelzebub INVT Pre-App instructions")

    def close_window():
        start_window.destroy()

    welcome_label = Label(start_window, text="""Welcome to my App! 
    READ ME!!!  To use this app enter in an Item, Then Enter the Serial Number for the Item, Then Enter the Price and Click Submit. When done click Save and Exit and the text file will be uploaded to your desktop.
    If you make a mistake you can delete the top most item with the delete button.""")
    welcome_label.pack()

    # create a button that will call the main_loop function
    start_button = Button(start_window, text="Start", command=lambda: [close_window(), main_loop()])
    start_button.pack()

    start_window.mainloop()

def main_loop():
    
    # create the fields and the button
    lbl_Item = Label(root, text="Item Name")
    e_Item = Entry(root, width=25, bd=5)
    lbl_Serial = Label(root, text="Serial Number")
    e_Serial = Entry(root, width=25, bd=5)
    lbl_Quan = Label(root, text="Price")
    e_Quan = Entry(root, width=25, bd=5)
    b_Submit = Button(root, text="Submit")
    b_Delete = Button(root, text="Delete")
    b_Close = Button(root, text="Save then Exit")
    
    # create the dictionary to store the items
    items = {}
    
    # create the listbox to display the items
    lb_Items = Listbox(root, width=50)
    lb_Items.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    # function to add an item to the dictionary and update the listbox
    def add_item(): 
        
        # get the values from the entry fields
        item_name = e_Item.get()
        serial_num = e_Serial.get()
        quantity = e_Quan.get()
        
        # validate the input for price and serial number
        if not re.match("^[0-9]+$", quantity):
            messagebox.showerror("Error", "Price should be a number only.")
            return
        if not re.match("^[a-zA-Z0-9]{8}$", serial_num):
            messagebox.showerror("Error", "Serial Number should be an 8 character alphanumeric string.")
            return
        
        # create a dictionary item and add it to the items dictionary
        item = {"Serial": serial_num, "Quantity": quantity}
        items[item_name] = item
        
        # clear the entry fields
        e_Item.delete(0, END)
        e_Serial.delete(0, END)
        e_Quan.delete(0, END)
        
        # update the listbox with the items
        lb_Items.delete(0, END)
        for item_name, item in items.items():
            lb_Items.insert(END, f"{item_name}: {item['Serial']}, {item['Quantity']}")
    
    #function to delete an item and then update list.
    def delete_item():
        selected_item = lb_Items.curselection()
        if not selected_item:
            messagebox.showerror("Error","Please select a Valid item.")
            return
        item_name = lb_Items.get(selected_item)

        del items[item_name.split(":")[0].strip()]
    
    # clear the listbox and update it with the updated items
        lb_Items.delete(0, END)
        for item_name, item in items.items():
          lb_Items.insert(END, f"{item_name}: {item['Serial']}, {item['Price']}")
#functions to  save then exit the app
    def save_file():
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        file_path = os.path.join(desktop_path, 'item_list.txt')

        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)
    
        with open(file_path, "w") as f:
            for item_name, item in items.items():
                f.write(f"{item_name}: {item['Serial']}, {item['Quantity']}\n")
    def close_app():
        save_file()
        root.destroy()
   
# place the labels, fields and the button on the window
    lbl_Item.place(relx=0.3, rely=0.15, anchor=CENTER)
    e_Item.place(relx=0.3, rely=0.2, anchor=CENTER)

    lbl_Quan.place(relx=0.5, rely=0.15, anchor=CENTER)
    e_Quan.place(relx=0.5, rely=0.2, anchor=CENTER)

    lbl_Serial.place(relx=0.7, rely=0.15, anchor=CENTER)
    e_Serial.place(relx=0.7, rely=0.2, anchor=CENTER)

    b_Submit.place(relx=0.5, rely=0.3, anchor=CENTER)
    b_Delete.place(relx=0.4, rely=0.7, anchor=CENTER)
    b_Close.place(relx=0.6, rely=0.7, anchor=CENTER)
# bind the button to the function that adds an item
    b_Submit.config(command=add_item)
    b_Delete.config(command=delete_item)
    b_Close.config(command=close_app)

starter_window()

