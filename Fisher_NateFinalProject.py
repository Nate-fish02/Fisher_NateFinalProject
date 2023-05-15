from tkinter import *
from tkinter import messagebox
# create the window

root = Tk()
root.title("Item List")
root.geometry("800x600")

#My Preapp Message/instructions message
intro = """           Welcome to Beelzebub INVT 
To enter in information into the Manager first enter Item then Serial number followed by how many, after all information is entered click submit.
"""
lbl_instructions = Label(root, text=intro)
lbl_instructions.place(relx=0.5, rely=0.1, anchor=CENTER)
# create the fields and the button
lbl_Item = Label(root, text="Item Name")
e_Item = Entry(root, width=25, bd=5)
lbl_Serial = Label(root, text="Serial Number")
e_Serial = Entry(root, width=25, bd=5)
lbl_Quan = Label(root, text="Quantity")
e_Quan = Entry(root, width=25, bd=5)
b_Submit = Button(root, text="Submit")
b_Delete = Button(root, text="Delete")

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
#functiom to delete an item and then update list.
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
        lb_Items.insert(END, f"{item_name}: {item['Serial']}, {item['Quantity']}")
        
# place the labels, fields and the button on the window
lbl_Item.place(relx=0.3, rely=0.15, anchor=CENTER)
e_Item.place(relx=0.3, rely=0.2, anchor=CENTER)

lbl_Quan.place(relx=0.5, rely=0.15, anchor=CENTER)
e_Quan.place(relx=0.5, rely=0.2, anchor=CENTER)

lbl_Serial.place(relx=0.7, rely=0.15, anchor=CENTER)
e_Serial.place(relx=0.7, rely=0.2, anchor=CENTER)

b_Submit.place(relx=0.5, rely=0.3, anchor=CENTER)
b_Delete.place(relx=0.5, rely=0.8, anchor=CENTER)
# bind the button to the function that adds an item
b_Submit.config(command=add_item)
b_Delete.config(command=delete_item)
e_Item.focus()
root.mainloop()
