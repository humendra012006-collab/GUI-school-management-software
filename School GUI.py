import tkinter as tk
from tkinter import filedialog
import shutil
import os
import atexit
import time
import tkinter.ttk as ttk
from doctest import master
from tkinter import StringVar, IntVar
import ttkbootstrap as tkb
import pickle as pk
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk

theam_options = ("cosmo","lumen","morph","solar","superhero","darkly","cyborg","vapor")
continuty = 0
date_and_time = time.strftime("%d %b %Y %I:%M %p")
username_entry = str()
rec_visit=dict()
visit_std_rec = []
visit_tea_rec = []
visit_set_rec = []
visit_his_rec = []
visit_std_rec.append("Student Section  ")
visit_tea_rec.append("Teacher Section  ")
visit_set_rec.append("Setting Section  ")
visit_his_rec.append("History Section  ")
## later for manegement and result section
global canvas
opened_class = 1
password_try = 0
# Never disturb this location

main_file_location = os.path.join(os.getcwd(),r"class 12 project data\Basic info.bin")
try:
    # when ever change this location also change it in error box of except bolck (just bleow)
    Basic_info = dict(pk.load(open(fr"{main_file_location}","rb")))
    print(os.getcwd())
    Location = os.path.join(os.getcwd(),"class 12 project data")
    theam_selected = Basic_info["theam"]
    if Location!=os.path.join(os.getcwd(),r"class 12 project data"):
        basic_info_write = open(fr"{main_file_location}","wb")
        Basic_info["location"] = fr"{os.path.join(os.getcwd(),"class 12 project data")}"
        pk.dump(Basic_info,basic_info_write)
        basic_info_write.close()
        Location = Basic_info["location"]
except:
    # show error box
    tmsg.showerror("ERROR",f"There is problem in opening file name Basic info.bin at \n {main_file_location}" )
    theam_selected = theam_options[2]
    quit()

# Register the save_history function to run at exit
def save_visitor_history():
    username_key = username_entry
    a = visit_std_rec.copy()
    b = visit_tea_rec.copy()
    c = visit_set_rec.copy()
    d = visit_his_rec.copy()
    final_rec_visit = list()
    final_rec_visit.append(date_and_time)
    for le in [a,b,c,d]:
        if len(le) != 1:
            final_rec_visit.append(le)
    rec_visit[username_key] = final_rec_visit
    try:
        """Save the rec_visit list to History.bin at program termination."""
        fobj_read = open(fr"{Location}\History.bin", "rb")
        frec_list = pk.load(fobj_read)
        fobj_read.close()
        frec_list.append(rec_visit)
        fobj_write = open(fr"{Location}\History.bin", "wb")
        pk.dump(frec_list, fobj_write)
        fobj_write.close()
    except:
        fn = open(fr"{Location}\History.bin", "wb")
        pk.dump(list(), fn)
        fn.close()
atexit.register(save_visitor_history)

# Definations
def keyboard_enter(keyboadr_deafult_argument):
    check_pass()
def check_pass():
    global username_entry
    username_entry = user_name.get().upper()
    username_entred.update()
    username_entred.configure(state="disabled",font="comicsansms 12",foreground="gray")
    if username_entry in Basic_info["user_name"]:
        global continuty
        continuty = 1
        window_pass.destroy()
    else:
        tmsg.showinfo("Message Box","\n\tOpps! SORRY\nYou are not saved as valid user\nAsk Principal to add your name Thanks!\n")
        window_pass.destroy()
def comman_menu(window,theam = "morph"):
    if theam in ("cosmo","lumen","morph"):
        try:
            # Common Menu Section
            main_menu = tk.Menu(window)
            window.config(menu=main_menu)
            m0 = tk.Menu(main_menu, tearoff=0)
            m0.add_command(label="Student Section", foreground="black", activebackground="pink",activeforeground="blue",state="disabled")
            m01 = m0.add_command(label="Teacher Section", foreground="black", activebackground="pink",activeforeground="blue", command=teacher_section)
            m0.add_command(label="History Section", foreground="black", activebackground="pink",activeforeground="blue",command=history_section)
            m0.add_command(label="Setting Section", foreground="black", activebackground="pink",activeforeground="blue",command=setting_section)
            m0.add_command(label="Manegement Section", foreground="black", activebackground="pink",activeforeground="blue",command=lambda : tmsg.showinfo("Message","Manegement Section Comming Soon"))
            m0.add_command(label="Result Section", foreground="black", activebackground="pink",activeforeground="blue",command=lambda : tmsg.showinfo("Message","Result Section Comming Soon"))
            main_menu.add_cascade(label=" Sections", menu=m0)
            # History menu
            m1 = tk.Menu(main_menu, tearoff=0)
            m1.add_command(label="History Record", foreground="black", activebackground="pink", activeforeground="blue",command=history_section)
            m1.add_command(label="Delet History", foreground="black", activebackground="pink", activeforeground="blue",command=setting_section)
            main_menu.add_cascade(label=" History", menu=m1)
            # setting menu
            m2 = tk.Menu(main_menu, tearoff=0)
            m2.add_command(label="Change theam", foreground="black", activebackground="pink", activeforeground="blue",command=setting_section)
            m2.add_separator()
            m2.add_command(label="Add New User", foreground="black", activebackground="pink", activeforeground="blue",command=setting_section)
            m2.add_command(label="Delet Old User", foreground="black", activebackground="pink", activeforeground="blue",command=setting_section)
            m2.add_separator()
            m2.add_command(label="Change Password", foreground="black", activebackground="pink",
                           activeforeground="blue",command=setting_section)
            m2.add_command(label="Change Location", foreground="black", activebackground="pink",
                           activeforeground="blue",command=setting_section)
            main_menu.add_cascade(label=" Setting", menu=m2)
        except:
            tmsg.showinfo("Menu Error", "ERROR in comman_menu defination \n my be forget to pass window when called")
            window.destroy()

    else:
        try:
            # Common Menu Section
            main_menu = tk.Menu(window)
            window.config(menu=main_menu)
            m0 = tk.Menu(main_menu, tearoff=0)
            m0.add_command(label="Student Section", foreground="pink", activebackground="pink",activeforeground="blue",state="disabled")
            m0.add_command(label="Teacher Section", foreground="pink", activebackground="pink",activeforeground="blue", command=teacher_section)
            m0.add_command(label="History Section", foreground="pink", activebackground="pink",activeforeground="blue",command=history_section)
            m0.add_command(label="Setting Section", foreground="pink", activebackground="pink",activeforeground="blue",command=setting_section)
            m0.add_command(label="Manegement Section", foreground="pink", activebackground="pink",activeforeground="blue",command=lambda : tmsg.showinfo("Message","Manegement Section Comming Soon"))
            m0.add_command(label="Result Section", foreground="pink", activebackground="pink", activeforeground="blue",command=lambda : tmsg.showinfo("Message","Result Section Comming Soon"))
            main_menu.add_cascade(label=" Sections", menu=m0)
            # History menu
            m1 = tk.Menu(main_menu, tearoff=0)
            m1.add_command(label="History Record", foreground="pink", activebackground="pink", activeforeground="blue",command=history_section)
            m1.add_command(label="Delet History", foreground="pink", activebackground="pink", activeforeground="blue",command=setting_section)
            main_menu.add_cascade(label=" History", menu=m1)
            # setting menu
            m2 = tk.Menu(main_menu, tearoff=0)
            m2.add_command(label="Change theam", foreground="pink", activebackground="pink", activeforeground="blue",command=setting_section)
            m2.add_separator()
            m2.add_command(label="Add New User", foreground="pink", activebackground="pink", activeforeground="blue",command=setting_section)
            m2.add_command(label="Delet Old User", foreground="pink", activebackground="pink", activeforeground="blue",command=setting_section)
            m2.add_separator()
            m2.add_command(label="Change Password", foreground="pink", activebackground="pink",
                           activeforeground="blue",command=setting_section)
            m2.add_command(label="Change Location", foreground="pink", activebackground="pink",
                           activeforeground="blue",command=setting_section)
            main_menu.add_cascade(label=" Setting", menu=m2)
        except:
            tmsg.showinfo("Menu Error", "ERROR in comman_menu defination \n my be forget to pass window when called")
            window.destroy()
# Student section start -------------------------------------------------------------------
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
def f3_std(class_no,search_value="None"):
    global canvas
    global f3
    for widget in f3.winfo_children():
        widget.destroy()
    class_object = Open_class(class_no)
    class_data = dict(pk.load(class_object))
    canvas = tk.Canvas(f3, borderwidth=0, background="pink")
    vsb = tk.Scrollbar(f3, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    # Create a frame inside the canvas to hold the dynamic frames
    scrollable_frame = tk.Frame(canvas, background="green")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    scrollable_frame.bind("<Configure>", on_frame_configure)
    tk.Label(scrollable_frame, text=f" CLASS NO : {class_no} ", font="comicsansms 13 italic").pack(pady=6)
    # Create a dictionary to store the frames dynamically
    frames = {}
    images = {}
    if search_value!="None":
        if search_value.isspace() == True:
            tmsg.showinfo("Message"," Please don't search for spaces! ")
            exit(f3_std())
            f3_std(opened_class)

        visit_std_rec.append(f"Search Student Name : {search_value}")
        for i in class_data:
            if search_value.lower() in class_data[i][0].lower():
                frame_name = f"f{i}"
                frame = tk.Frame(scrollable_frame, border=2, relief="solid")
                frame.pack(padx=10, pady=10, fill="x")
                frames[frame_name] = frame
                image_name = f"i{i}"
                try:
                    image = Image.open(fr"{Location}\{i}_{class_no}.jpg")
                except:
                    image = Image.open(fr"{Location}\student section 200x200.jpg")

                student_image = ImageTk.PhotoImage(image.resize((200, 210)))
                images[image_name] = student_image
                tk.Label(frames[frame_name], image=student_image, anchor="w").pack(side="left", padx=10, pady=5)
                tk.Label(frames[frame_name], text="  ", font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=0)
                tk.Label(frames[frame_name], text=f"STUDENT NAME \t : {class_data[i][0]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"ROLL NO \t : {i}", font="comicsansms 13 bold").pack(anchor="w",padx=10,pady=2)
                tk.Label(frames[frame_name], text=f"MOTHER NAME \t : {class_data[i][1]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"FATHER NAME \t : {class_data[i][2]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"EMAIL ADDRESS \t : {class_data[i][3]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"PHONE NO \t : {class_data[i][4]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"ADDRESS \t : {class_data[i][5]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"ADHAR NO \t : {class_data[i][6]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text="  ", font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)

        f3.mainloop()

    else:

        visit_std_rec.append(f"Class {class_no}")
        # Thanks to O3-mini open ai for this
        '''
        f3_std mai canvas se tk.Label tak 
        How This Works:
        Canvas and Scrollbar:
        The canvas widget is used to create a scrollable area. The scrollbar (vsb) is linked to the canvas via the yscrollcommand and command options.
        Scrollable Frame:
        A frame (scrollable_frame) is placed inside the canvas. All dynamic frames are added as children of this frame.
        Updating the Scroll Region:
        The on_frame_configure function is bound to the <Configure> event of the scrollable frame. This ensures that whenever the frame's size changes (as new widgets are added), the canvas updates its scrollable region.
        Dynamic Frames:
        A dictionary (frames) is used to store each frame with a key like "f1", "f2", etc., making them easy to access later.
        '''

        for i in range(1, len(class_data) + 1):
            frame_name = f"f{i}"
            frame = tk.Frame(scrollable_frame, border=2, relief="solid")
            frame.pack(padx=10, pady=10, fill="x")
            frames[frame_name] = frame
            image_name = f"i{i}"
            try:
                image = Image.open(fr"{Location}\{i}_{class_no}.jpg")
            except:
                image = Image.open(fr"{Location}\student section 200x200.jpg")

            student_image = ImageTk.PhotoImage(image.resize((200, 210)))
            images[image_name] = student_image
            tk.Label(frames[frame_name], image=student_image, anchor="w").pack(side="left", padx=10, pady=5)
            tk.Label(frames[frame_name], text="  ", font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=0)
            tk.Label(frames[frame_name], text=f"STUDENT NAME \t : {class_data[i][0]}",
                     font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
            tk.Label(frames[frame_name], text=f"ROLL NO \t : {i}", font="comicsansms 13 bold").pack(anchor="w", padx=10,
                                                                                                    pady=2)
            tk.Label(frames[frame_name], text=f"MOTHER NAME \t : {class_data[i][1]}",
                     font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
            tk.Label(frames[frame_name], text=f"FATHER NAME \t : {class_data[i][2]}",
                     font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
            tk.Label(frames[frame_name], text=f"EMAIL ADDRESS \t : {class_data[i][3]}",
                     font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
            tk.Label(frames[frame_name], text=f"PHONE NO \t : {class_data[i][4]}",
                     font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
            tk.Label(frames[frame_name], text=f"ADDRESS \t : {class_data[i][5]}",
                     font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
            tk.Label(frames[frame_name], text=f"AADHAAR NO \t : {class_data[i][6]}",
                     font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
            tk.Label(frames[frame_name], text="  ", font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)

        f3.mainloop()
def Open_class(clas_s,mood="r"):
    class_object = open(fr"{Location}\class{clas_s}.bin", f"{mood}b")
    return class_object
def class_1():
    global opened_class
    opened_class = 1
    f3_std(opened_class)
def class_2():
    global opened_class
    opened_class = 2
    f3_std(opened_class)
def class_3():
    global opened_class
    opened_class = 3
    f3_std(opened_class)
def class_4():
    global opened_class
    opened_class = 4
    f3_std(opened_class)
def class_5():
    global opened_class
    opened_class = 5
    f3_std(opened_class)
def class_6():
    global opened_class
    opened_class = 6
    f3_std(opened_class)
def class_7():
    global opened_class
    opened_class = 7
    f3_std(opened_class)
def class_8():
    global opened_class
    opened_class = 8
    f3_std(opened_class)
def class_9():
    global opened_class
    opened_class = 9
    f3_std(opened_class)
def class_10():
    global opened_class
    opened_class = 10
    f3_std(opened_class)
def class_11():
    global opened_class
    opened_class = 11
    f3_std(opened_class)
def class_12():
    global opened_class
    opened_class = 12
    f3_std(opened_class)
def std_edite():
    f0 = Open_class(opened_class)
    f0_re = dict(pk.load(f0))
    f0.close()
    display_order = ["STUDENT","MOTHER","FATHER","EMAIL","PHONE","ADDRESS","AADHAAR"]
    def edit_details():
        def save_edits():
            new_detailes = [(_v1.get()).title(), (_v3.get()).title(), (_v4.get()).title(), _v5.get(), str(_v6.get()), _v7.get(), str(_v8.get())]
            f0_re[fix_roll] = [(_v1.get()).title(), (_v3.get()).title(), (_v4.get()).title(), _v5.get(), _v6.get(), _v7.get(), _v8.get()]
            dn = dict()
            roll = 1
            for i in f0_re:
                dn[roll] = list(f0_re[i])
                roll = roll + 1
            fn = Open_class(opened_class, "w")
            pk.dump(dn, fn)
            fn.close()
            for c in range(0,7):
                if old_detailes[c]!=new_detailes[c]:
                    visit_std_rec.append(f"Edit[class {opened_class} roll no {fix_roll}] {display_order[c]} : {old_detailes[c]} to {new_detailes[c]}")
            edit_win.destroy()
            f3_std(opened_class)
        def imaage_button():
            #add_win.withdraw()  # Hide the main window
            # Open file dialog to select an image
            file_path = filedialog.askopenfilename(title="Select an Image",filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
            if file_path:  # Check if the user selected a file
                save_folder = Location
                destination = os.path.join(save_folder, f"{fix_roll}_{opened_class}.jpg")  # Set save path
                shutil.copy(file_path, destination)  # Copy the file to the new location
                visit_std_rec.append(f"Edit[class {opened_class} roll no {fix_roll}] Profile Photo Changed")
                print(f"New image at path : {destination}")
            else:
                tmsg.showinfo("File Selection","No file selected.")
                edit_details()
            try:
                image = Image.open(fr"{Location}\{fix_roll}_{opened_class}.jpg")
            except:
                image = Image.open(fr"{Location}\student section 200x200.jpg")

            student_image = ImageTk.PhotoImage(image.resize((200, 210)), master=edit_win)
            std_image.configure(image=student_image)
            std_image.image = student_image

        fix_roll = int(list_box.curselection()[0]) + 1
        for widget in edit_win.winfo_children():
            widget.destroy()
        try:
            image = Image.open(fr"{Location}\{fix_roll}_{opened_class}.jpg")
        except:
            image = Image.open(fr"{Location}\profile photo.jpg")
        old_detailes = [f0_re[fix_roll][0],f0_re[fix_roll][1],f0_re[fix_roll][2],f0_re[fix_roll][3],str(f0_re[fix_roll][4]),f0_re[fix_roll][5],str(f0_re[fix_roll][6])]
        student_image = ImageTk.PhotoImage(image.resize((200, 210)), master=edit_win)
        std_image = tk.Button(edit_win, image=student_image, anchor="w",command=imaage_button)
        std_image.image = student_image  # Prevents garbage collection
        std_image.pack(side="left", padx=10, pady=5)
        _v1 = StringVar(value=f0_re[fix_roll][0])
        _v2 = IntVar(value=fix_roll)
        _v3 = StringVar(value=f0_re[fix_roll][1])
        _v4 = StringVar(value=f0_re[fix_roll][2])
        _v5 = StringVar(value=f0_re[fix_roll][3])
        _v6 = StringVar(value=str(f0_re[fix_roll][4]))
        _v7 = StringVar(value=f0_re[fix_roll][5])
        _v8 = StringVar(value=str(f0_re[fix_roll][6]))
        tk.Label(edit_win, text="  ", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=0)
        tk.Label(edit_win, text=f"STUDENT NAME :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(edit_win, textvariable=_v1, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1, ipadx=60.0)
        tk.Label(edit_win, text=f"ROLL NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(edit_win, textvariable=_v2, font="comicsansms 12 italic", state="readonly").pack(anchor="w", padx=20,pady=1, ipadx=60.0)
        tk.Label(edit_win, text=f"MOTHER NAME :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(edit_win, textvariable=_v3, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1, ipadx=60.0)
        tk.Label(edit_win, text=f"FATHER NAME :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(edit_win, textvariable=_v4, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1, ipadx=60.0)
        tk.Label(edit_win, text=f"EMAIL ADDRESS :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(edit_win, textvariable=_v5, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1, ipadx=60.0)
        tk.Label(edit_win, text=f"PHONE NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(edit_win, textvariable=_v6, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1, ipadx=60.0)
        tk.Label(edit_win, text=f"ADDRESS :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(edit_win, textvariable=_v7, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1, ipadx=60.0)
        tk.Label(edit_win, text=f"AADHAAR NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(edit_win, textvariable=_v8, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1, ipadx=60.0)
        tk.Button(edit_win, text=" SAVE ", font="comicsansms 12 bold", justify="center",command=save_edits).pack(side="bottom", anchor="e", ipady=4, ipadx=30, pady=15, padx=15)

    edit_win = tk.Toplevel()
    edit_win.geometry("600x530")
    edit_win.minsize(600,530)
    edit_win.maxsize(600,530)
    tkb.Style(theam_selected)
    edit_win.title("Edit Student Details")
    tk.Label(edit_win, text="*Select Student To Edit This Details*",font="comicsansms 18 bold").pack(side="top",pady=20)
    tk.Label(edit_win, text="                     ",font="comicsansms 12 bold").pack(side="top",pady=3,padx=130,anchor="w")
    tk.Label(edit_win, text="Roll no.                     Student Name",font="comicsansms 12 bold").pack(side="top",pady=2,padx=130,anchor="w")
    del_scrollbar = tk.Scrollbar(edit_win)
    del_scrollbar.pack(side="right",fill="y")
    list_box = tk.Listbox(edit_win,font="comicsansms 13 bold",width=40,height=15,yscrollcommand=del_scrollbar.set)
    list_box.pack()
    del_scrollbar.config(command=list_box.yview)
    for i in f0_re:
        list_box.insert(list_box.size(),f" {i}               :            {f0_re[i][0]} ")
    tk.Button(edit_win,text=" Edit Details ",font="comicsansms 13 bold",command=edit_details).pack(side="bottom",ipadx=20,ipady=4,pady=20)
    edit_win.mainloop()
def std_delete():
    f0 = Open_class(opened_class)
    f0_re = dict(pk.load(f0))
    f0.close()
    def deleting():
        run = 1
        roll_select = int(list_box.curselection()[0]) + 1
        visit_std_rec.append(f"Delete[class {opened_class} rollno {roll_select} Name : {f0_re[roll_select][0]}] ")
        del f0_re[roll_select]
        dn = dict()
        for k in f0_re.keys():
            if run==roll_select:
                remove_path = os.path.join(Location,f"{roll_select}_{opened_class}.jpg")
                if os.path.exists(remove_path):
                    os.remove(remove_path)
            if run > roll_select:
                file_path = os.path.join(Location, f"{run}_{opened_class}.jpg")
                new_roll = run - 1
                new_file_path = os.path.join(Location, f"{new_roll}_{opened_class}.jpg")
                if os.path.exists(file_path):
                    os.rename(file_path, new_file_path)
                    #print(fr"path is changed to : {new_file_path}")
            dn[run]=list(f0_re[k])
            run = run + 1
        # for the last image
        file_path = os.path.join(Location, f"{run}_{opened_class}.jpg")
        new_roll = run - 1
        new_file_path = os.path.join(Location, f"{new_roll}_{opened_class}.jpg")
        if os.path.exists(file_path):
            os.rename(file_path, new_file_path)
            #print(fr"path is changed to : {new_file_path}")

        fn = Open_class(opened_class,"w")
        pk.dump(dn, fn)
        fn.close()
        del_win.destroy()
        f3_std(opened_class)

    del_win = tk.Tk()
    del_win.geometry("600x530")
    del_win.minsize(600,530)
    del_win.maxsize(600,530)
    tkb.Style(theam_selected)
    tk.Label(del_win, text="Delete Student Data By Choosing Roll No.",font="comicsansms 12 italic").pack(side="top",pady=10)
    tk.Label(del_win, text="Roll no.                Student Name",font="comicsansms 12 bold").pack(side="top",pady=10,padx=130,anchor="w")
    del_scrollbar = tk.Scrollbar(del_win)
    del_scrollbar.pack(side="right",fill="y")
    list_box = tk.Listbox(del_win,font="comicsansms 13 bold",width=40,height=15,yscrollcommand=del_scrollbar.set)
    list_box.pack()
    del_scrollbar.config(command=list_box.yview)
    for i in f0_re:
        list_box.insert(list_box.size(),f" {i}               :            {f0_re[i][0]} ")
    tk.Button(del_win,text=" DELETE ",font="comicsansms 11 italic",command=deleting).pack(side="bottom",ipadx=20,ipady=4,pady=20)
    del_win.mainloop()
def std_s(nill="None"):
    f3_std(opened_class,search_val.get())
def student_section():
    global f1
    global f2
    global search_val
    for widget in f2.winfo_children():
        widget.destroy()
    for widget in f1.winfo_children():
        widget.destroy()
    comman_menu(root, theam_selected)
    edit_image = Image.open(fr"{Location}\edit_2.jpg")
    photo_edit = ImageTk.PhotoImage(edit_image.resize((80, 80)))
    edit_1=tk.Button(f2, image=photo_edit,command=std_edite)
    edit_1.image = photo_edit
    edit_1.pack(side="left",padx=10)
    delete_image = Image.open(fr"{Location}\delete.jpg")
    photo_delete = ImageTk.PhotoImage(delete_image.resize((80, 80)))
    del_1=tk.Button(f2, image=photo_delete,command=std_delete)
    del_1.image = photo_delete
    del_1.pack(side="left", padx=10)
    def add_std():
        class_object_read = Open_class(opened_class)
        class_data = dict(pk.load(class_object_read))
        def add_submit():
            fill = 1
            try:
                phone_no = str(v6.get())
                if phone_no.isspace():
                    tmsg.showinfo("Message", "Phone no should be Entered")
                    fill=0
                if len(phone_no) != 10:
                    tmsg.showinfo("Message","Phone no should be of 10 numbers")
                    fill=0
                phone_no = int(phone_no)
            except:
                tmsg.showwarning("Warning"," Phone no must have digits only.")
                fill=0
            try:
                aadhaar_no = str(v8.get())
                if aadhaar_no.isspace():
                    tmsg.showinfo("Message", "Aadhaar no should be Entered")
                    fill=0
                if len(aadhaar_no)!=12:
                    tmsg.showinfo("Message", "Aadhaar no should be of 12 digits only.")
                    fill=0
                aadhaar_no = int(aadhaar_no)
            except:
                tmsg.showwarning("Warning", " Aadhaar no must have digits only.")
                fill=0

            for q in [str(v1.get()).title(),str(v3.get()).title(),str(v4.get()).title(),str(v5.get()),str(v7.get())]:
                if q.isspace()==True or len(q)==0:
                    tmsg.showwarning("WARNING","You must fill all the deitales.")
                    fill = 0

            if fill == 1:
                class_data[int(v2.get())] = [str(v1.get()).title(), str(v3.get()).title(), str(v4.get()).title(),
                                             str(v5.get()), phone_no, str(v7.get()), aadhaar_no]
                class_object_write = Open_class(opened_class, "w")
                pk.dump(class_data, class_object_write)
                visit_std_rec.append(f"Add student[class {opened_class} rollno {int(v2.get())} Name : {str(v1.get()).title()}]")
                add_win.destroy()
                f3_std(opened_class)
            else:
                path1 = fr"{Location}\{int(len(class_data))+1}_{opened_class}.jpg"
                if os.path.exists(path1)==True:
                    os.remove(path1)
                add_std()

        def imaage_button():
            #add_win.withdraw()  # Hide the main window
            # Open file dialog to select an image
            file_path = filedialog.askopenfilename(title="Select an Image",filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
            if file_path:  # Check if the user selected a file
                # save_folder = filedialog.askdirectory(title="Select Destination Folder",initialdir=Location)
                save_folder = Location
                # file_name = os.path.basename(file_path)  # Get the file name
                destination = os.path.join(save_folder, f"{int(len(class_data))+1}_{opened_class}.jpg")  # Set save path
                shutil.copy(file_path, destination)  # Copy the file to the new location
                print(f"Image saved successfully at: {destination}")
            else:
                tmsg.showinfo("File Selection","No file selected.")
                add_std()
            try:
                image = Image.open(fr"{Location}\{int(len(class_data))+1}_{opened_class}.jpg")
            except:
                image = Image.open(fr"{Location}\student section 200x200.jpg")

            student_image = ImageTk.PhotoImage(image.resize((200, 210)), master=add_win)
            std_image.configure(image=student_image,state="normal")
            std_image.image=student_image


        add_win = tk.Toplevel(root)
        add_win.geometry("600x510")
        add_win.minsize(600,510)
        add_win.maxsize(600,510)

        try:
            image = Image.open(fr"{Location}\{int(len(class_data)) + 1}_{opened_class}.jpg")
        except:
            image = Image.open(fr"{Location}\profile photo.jpg")
        student_image = ImageTk.PhotoImage(image.resize((200, 210)),master=add_win)
        std_image = tk.Button(add_win, image=student_image,command=imaage_button, anchor="w")
        std_image.image = student_image  # Prevents garbage collection
        std_image.pack(side="left", padx=10, pady=5)

        v1 = StringVar()
        v2 = IntVar(value=int(len(class_data)) + 1)
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        v6 = StringVar()
        v7 = StringVar()
        v8 = StringVar()

        tk.Label(add_win, text="  ", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=0)
        tk.Label(add_win, text=f"STUDENT NAME :",font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win,textvariable=v1,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"ROLL NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20,pady=1)
        tk.Entry(add_win, textvariable=v2,font="comicsansms 12 italic",state="disabled").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"MOTHER NAME :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v3,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"FATHER NAME :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v4,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"EMAIL ADDRESS :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v5,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"PHONE NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v6,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"ADDRESS :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v7,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"AADHAAR NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v8,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Button(add_win,text=" SAVE ",font="comicsansms 12 bold",justify="center",command=add_submit).pack(side="bottom",anchor="e",ipady=4,ipadx=30,pady=15,padx=15)
        add_win.mainloop()

    add_image = Image.open(fr"{Location}\add1.jpg")
    photo_add = ImageTk.PhotoImage(add_image.resize((80, 80)))
    add_1 = tk.Button(f2, image=photo_add,command=add_std)
    add_1.image = photo_add
    add_1.pack(side="left", padx=10)

    search_image = Image.open(fr"{Location}\search.jpg")
    photo_search = ImageTk.PhotoImage(search_image.resize((60, 60)))
    search_1 = tk.Button(f2, image=photo_search,command=std_s)
    search_1.image = photo_search
    search_1.pack(side="right", padx=10)
    std_search = tk.Entry(f2,textvariable=search_val,font="comicsansms 20 italic",justify="left")
    std_search.pack(side="right",padx=0,ipady=3,ipadx=30)
    std_search.bind("<KeyRelease-Return>",std_s)
    tk.Label(f3, text=" OPEN CLASS ", font="comicsansms 15 italic").pack(pady=6)
    tk.Label(f1, text=" CHOOSE CLASS ", font="comicsansms 13 italic").pack(pady=6)
    tk.Button(f1, text="CLASS NO :  1",command=class_1).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  2",command=class_2).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  3", command=class_3).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  4", command=class_4).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  5", command=class_5).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  6", command=class_6).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  7", command=class_7).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  8", command=class_8).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  9", command=class_9).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  10", command=class_10).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  11", command=class_11).pack(pady=1, fill="x")
    tk.Button(f1, text="CLASS NO :  12", command=class_12).pack(pady=1, fill="x")
    class_1()
# Student section ended -------------------------------------------------------------------
# Teacher section stared ------------------------------------------------------------------
def teacher_section():
    obj_teacher_read = open(fr"{Location}\teacher.bin","rb")
    teachers_data = dict(pk.load(obj_teacher_read))
    def tea_s(event=None):
        search_query = search_val.get()
        t3_tea(search_query if search_query else "None")
    def add_teacher():
        def add_submit_t():
            fill = 1
            try:
                phone_no = str(v6.get())
                if phone_no.isspace():
                    tmsg.showinfo("Message", "Phone no should be Entered")
                    fill=0
                if len(phone_no) != 10:
                    tmsg.showinfo("Message","Phone no should be of 10 numbers")
                    fill=0
                phone_no = int(phone_no)
            except:
                tmsg.showwarning("Warning"," Phone no must have digits only.")
                fill=0
            try:
                teacher_salary = str(v8.get())
                if teacher_salary.isspace():
                    tmsg.showinfo("Message", "Aadhaar no should be Entered")
                    fill=0
                teacher_salary = int(teacher_salary)
            except:
                tmsg.showwarning("Warning", "Salery must be in digits only.")
                fill=0

            for q in [str(v1.get()).title(),str(v3.get()).title(),str(v4.get()).title(),str(v5.get()),str(v7.get())]:
                if q.isspace()==True or len(q)==0:
                    tmsg.showwarning("WARNING","You must fill all the deitales.")
                    fill = 0

            if fill == 1:
                teachers_data[int(v2.get())] = [str(v1.get()).title(), str(v3.get()).title(), str(v4.get()).title(), phone_no,teacher_salary, str(v7.get()),str(v5.get())]
                teacher_object_write = open(fr"{Location}\teacher.bin","wb")
                pk.dump(teachers_data, teacher_object_write)
                visit_tea_rec.append(f"Add [Name : {str(v1.get()).title()}]")
                add_win.destroy()
                t3_tea()
            else:
                path1 = fr"{Location}\t_{int(len(teachers_data))+1}.jpg"
                if os.path.exists(path1)==True:
                    os.remove(path1)
                add_win.destroy()
                add_teacher()

        def imaage_button():
            #add_win.withdraw()  # Hide the main window
            # Open file dialog to select an image
            file_path = filedialog.askopenfilename(title="Select an Image",filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
            if file_path:  # Check if the user selected a file
                # save_folder = filedialog.askdirectory(title="Select Destination Folder",initialdir=Location)
                save_folder = Location
                # file_name = os.path.basename(file_path)  # Get the file name
                destination = os.path.join(save_folder, f"t_{int(len(teachers_data))+1}.jpg")  # Set save path
                shutil.copy(file_path, destination)  # Copy the file to the new location
                print(f"Image saved successfully at: {destination}")
            else:
                tmsg.showinfo("File Selection","No file selected.")
                add_teacher()
            try:
                image = Image.open(fr"{Location}\t_{int(len(teachers_data))+1}.jpg")
            except:
                image = Image.open(fr"{Location}\teacher.jpg")

            student_image = ImageTk.PhotoImage(image.resize((200, 210)), master=add_win)
            std_image.configure(image=student_image,state="normal")
            std_image.image=student_image


        add_win = tk.Toplevel(teacher_win)
        add_win.geometry("600x510")
        add_win.minsize(600,510)
        add_win.maxsize(600,510)

        try:
            image = Image.open(fr"{Location}\t_{int(len(teachers_data)) + 1}.jpg")
        except:
            image = Image.open(fr"{Location}\profile photo.jpg")

        student_image = ImageTk.PhotoImage(image.resize((200, 210)),master=add_win)
        std_image = tk.Button(add_win, image=student_image,command=imaage_button, anchor="w")
        std_image.image = student_image  # Prevents garbage collection
        std_image.pack(side="left", padx=10, pady=5)

        v1 = StringVar()
        v2 = IntVar(value=int(len(teachers_data)) + 1)
        v3 = StringVar()
        v4 = StringVar()
        v5 = StringVar()
        v6 = StringVar()
        v7 = StringVar()
        v8 = StringVar()

        tk.Label(add_win, text="  ", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=0)
        tk.Label(add_win, text=f"TEACHER NAME :",font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win,textvariable=v1,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"ID NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20,pady=1)
        tk.Entry(add_win, textvariable=v2,font="comicsansms 12 italic",state="disabled").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"SUBJECT NAME :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v3,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"DEGREE / QUALIFICATION :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v4,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"PHONE NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v6,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"TEACHER SALARY :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v8,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"EMAIL ADDRESS :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v7,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Label(add_win, text=f"ADDRESS :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
        tk.Entry(add_win, textvariable=v5,font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
        tk.Button(add_win,text=" SAVE ",font="comicsansms 12 bold",justify="center",command=add_submit_t).pack(side="bottom",anchor="e",ipady=4,ipadx=30,pady=15,padx=15)
        add_win.mainloop()
    def t3_tea(search_teacher="None"):
        for widget in t3.winfo_children():
            widget.destroy()
        def on_frame_configure_t(event):
            t_canvas.configure(scrollregion=t_canvas.bbox("all"))
        t_canvas = tk.Canvas(t3, borderwidth=0, background="pink")
        vsb_t = tk.Scrollbar(t3, orient="vertical", command=t_canvas.yview)
        t_canvas.configure(yscrollcommand=vsb_t.set)
        vsb_t.pack(side="right", fill="y")
        t_canvas.pack(side="left", fill="both", expand=True)
        # Create a frame inside the canvas to hold the dynamic frames
        scrollable_frame_t = tk.Frame(t_canvas, background="green")
        t_canvas.create_window((0, 0), window=scrollable_frame_t, anchor="nw")
        scrollable_frame_t.bind("<Configure>", on_frame_configure_t)
        tk.Label(scrollable_frame_t, text="Teachers", font="comicsansms 13 italic").pack(pady=6)
        frames = {}
        images = {}
        if search_teacher != "None":
            if search_teacher.isspace() == True:
                tmsg.showinfo("Message", " Please don't search for spaces! ")
                t3_tea()

            visit_tea_rec.append(f"Search Teacher Name : {search_teacher}")
            for i in teachers_data:
                if search_teacher.lower() in teachers_data[i][0].lower():
                    frame_name = f"t{i}"
                    frame = tk.Frame(scrollable_frame_t, border=2, relief="solid")
                    frame.pack(padx=10, pady=10, fill="x")
                    frames[frame_name] = frame
                    image_name = f"ti{i}"
                    try:
                        image = Image.open(fr"{Location}\t_{i}.jpg")
                    except:
                        image = Image.open(fr"{Location}\teacher.jpg")
                    teacher_image = ImageTk.PhotoImage(image.resize((200, 210)))
                    images[image_name] = teacher_image
                    lb1 = tk.Label(frames[frame_name], image=teacher_image, anchor="w")
                    lb1.image = teacher_image
                    lb1.pack(side="left", padx=10, pady=5)

                    tk.Label(frames[frame_name], text="  ", font="comicsansms 13 bold").pack(anchor="w", padx=10,
                                                                                             pady=0)
                    tk.Label(frames[frame_name], text=f"TEACHER NAME \t\t : {teachers_data[i][0].strip("\n")}",
                             font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                    tk.Label(frames[frame_name], text=f"ID NO \t\t\t : {i}", font="comicsansms 13 bold").pack(
                        anchor="w", padx=10, pady=2)
                    tk.Label(frames[frame_name], text=f"SUBJECT NAME \t\t : {teachers_data[i][1]}",
                             font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                    tk.Label(frames[frame_name], text=f"DEGREE / QUALIFICATION  : {teachers_data[i][2]}",
                             font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                    tk.Label(frames[frame_name], text=f"PHONE NO \t\t : {teachers_data[i][3]}",
                             font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                    tk.Label(frames[frame_name], text=f"TEACHER SALARY \t : {teachers_data[i][4]}",
                             font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                    tk.Label(frames[frame_name], text=f"EMAIL ADDRESS \t\t : {teachers_data[i][5]}",
                             font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                    tk.Label(frames[frame_name], text=f"ADDRESS \t\t : {teachers_data[i][6]}",
                             font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                    tk.Label(frames[frame_name], text="  ", font="comicsansms 13 bold").pack(anchor="w", padx=10,pady=2)
        else:
            # Thanks to O3-mini open ai for this
            '''
            f3_std mai canvas se tk.Label tak 
            How This Works:
            Canvas and Scrollbar:
            The canvas widget is used to create a scrollable area. The scrollbar (vsb) is linked to the canvas via the yscrollcommand and command options.
            Scrollable Frame:
            A frame (scrollable_frame) is placed inside the canvas. All dynamic frames are added as children of this frame.
            Updating the Scroll Region:
            The on_frame_configure function is bound to the <Configure> event of the scrollable frame. This ensures that whenever the frame's size changes (as new widgets are added), the canvas updates its scrollable region.
            Dynamic Frames:
            A dictionary (frames) is used to store each frame with a key like "f1", "f2", etc., making them easy to access later.
            '''

            for i in range(1, len(teachers_data) + 1):
                frame_name = f"t{i}"
                frame = tk.Frame(scrollable_frame_t, border=2, relief="solid")
                frame.pack(padx=10, pady=10, fill="x")
                frames[frame_name] = frame
                image_name = f"ti{i}"
                try:
                    image = Image.open(fr"{Location}\t_{i}.jpg")
                except:
                    image = Image.open(fr"{Location}\teacher.jpg")

                teacher_image = ImageTk.PhotoImage(image.resize((200, 210)))
                images[image_name] = teacher_image
                lb1 = tk.Label(frames[frame_name], image=teacher_image, anchor="w")
                lb1.image = teacher_image
                lb1.pack(side="left", padx=10, pady=5)

                tk.Label(frames[frame_name], text="  ", font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=0)
                tk.Label(frames[frame_name], text=f"TEACHER NAME \t\t : {teachers_data[i][0].strip("\n")}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"ID NO \t\t\t : {i}", font="comicsansms 13 bold").pack(anchor="w",padx=10,pady=2)
                tk.Label(frames[frame_name], text=f"SUBJECT NAME \t\t : {teachers_data[i][1]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"DEGREE / QUALIFICATION  : {teachers_data[i][2]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"PHONE NO \t\t : {teachers_data[i][3]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"TEACHER SALARY \t : {teachers_data[i][4]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"EMAIL ADDRESS \t\t : {teachers_data[i][5]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text=f"ADDRESS \t\t : {teachers_data[i][6]}",
                         font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
                tk.Label(frames[frame_name], text="  ", font="comicsansms 13 bold").pack(anchor="w", padx=10, pady=2)
    def teacher_edite():
        def edit_details():
            def save_t_edits():
                teachers_data[fix_roll] = [(_v1.get()).title(), (_v3.get()).title(), (_v4.get()).title(), _v5.get(), _v6.get(),
                                   _v7.get(), _v8.get()]
                New_Detailes = [(_v1.get()).title(), (_v3.get()).title(), (_v4.get()).title(), _v5.get(), _v6.get(),
                                   _v7.get(), _v8.get()]
                dn = dict()
                roll = 1
                for i in teachers_data:
                    dn[roll] = list(teachers_data[i])
                    roll = roll + 1
                fn = open(fr"{Location}\teacher.bin","wb")
                pk.dump(dn, fn)
                fn.close()
                for t in range(0,7):
                    if Old_detailes[t]!=New_Detailes[t]:
                        visit_tea_rec.append(f"Edit [{Display_Order[t]} : {Old_detailes[t]} to {New_Detailes[t]}]")
                edit_win.destroy()
                t3_tea()
            def imaage_button():
                # add_win.withdraw()  # Hide the main window
                # Open file dialog to select an image
                file_path = filedialog.askopenfilename(title="Select an Image",
                                                       filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
                if file_path:  # Check if the user selected a file
                    # save_folder = filedialog.askdirectory(title="Select Destination Folder",initialdir=Location)
                    save_folder = Location
                    # file_name = os.path.basename(file_path)  # Get the file name
                    destination = os.path.join(save_folder, f"t_{fix_roll}.jpg")  # Set save path
                    shutil.copy(file_path, destination)  # Copy the file to the new location
                    visit_tea_rec.append(f"Profile Photo Changed [teacher id : {fix_roll}]")
                    #print(f"Image saved successfully at: {destination}")
                else:
                    tmsg.showinfo("File Selection", "No file selected.")
                    add_teacher()
                try:
                    image = Image.open(fr"{Location}\t_{fix_roll}.jpg")
                except:
                    image = Image.open(fr"{Location}\teacher.jpg")

                student_image = ImageTk.PhotoImage(image.resize((200, 210)), master=edit_win)
                std_image.configure(image=student_image, state="normal")
                std_image.image = student_image

            fix_roll = int(list_box.curselection()[0]) + 1
            for widget in edit_win.winfo_children():
                widget.destroy()
            try:
                image = Image.open(fr"{Location}\t_{fix_roll}.jpg")
            except:
                image = Image.open(fr"{Location}\profile photo.jpg")
            Display_Order = ["TEACHER","SUBJECT","DEGREE","PHONE","SALARY","EMAIL","ADDRESS"]
            Old_detailes = [teachers_data[fix_roll][0],teachers_data[fix_roll][1],teachers_data[fix_roll][2],teachers_data[fix_roll][3],str(teachers_data[fix_roll][4]),teachers_data[fix_roll][5],str(teachers_data[fix_roll][6])]
            student_image = ImageTk.PhotoImage(image.resize((200, 210)), master=edit_win)
            std_image = tk.Button(edit_win, image=student_image, anchor="w", command=imaage_button)
            std_image.image = student_image  # Prevents garbage collection
            std_image.pack(side="left", padx=10, pady=5)
            _v1 = StringVar(value=teachers_data[fix_roll][0])
            _v2 = IntVar(value=fix_roll)
            _v3 = StringVar(value=teachers_data[fix_roll][1])
            _v4 = StringVar(value=teachers_data[fix_roll][2])
            _v5 = StringVar(value=teachers_data[fix_roll][3])
            _v6 = StringVar(value=str(teachers_data[fix_roll][4]))
            _v7 = StringVar(value=teachers_data[fix_roll][5])
            _v8 = StringVar(value=str(teachers_data[fix_roll][6]))

            tk.Label(edit_win, text="  ", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=0)
            tk.Label(edit_win, text=f"TEACHER NAME :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
            tk.Entry(edit_win, textvariable=_v1, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
            tk.Label(edit_win, text=f"ID NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
            tk.Entry(edit_win, textvariable=_v2, font="comicsansms 12 italic", state="disabled").pack(anchor="w", padx=20,pady=1, ipadx=60.0)
            tk.Label(edit_win, text=f"SUBJECT NAME :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
            tk.Entry(edit_win, textvariable=_v3, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
            tk.Label(edit_win, text=f"DEGREE / QUALIFICATION :", font="comicsansms 10 bold").pack(anchor="w", padx=20,pady=1)
            tk.Entry(edit_win, textvariable=_v4, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
            tk.Label(edit_win, text=f"PHONE NO :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
            tk.Entry(edit_win, textvariable=_v6, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
            tk.Label(edit_win, text=f"TEACHER SALARY :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
            tk.Entry(edit_win, textvariable=_v8, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
            tk.Label(edit_win, text=f"EMAIL ADDRESS :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
            tk.Entry(edit_win, textvariable=_v7, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
            tk.Label(edit_win, text=f"ADDRESS :", font="comicsansms 10 bold").pack(anchor="w", padx=20, pady=1)
            tk.Entry(edit_win, textvariable=_v5, font="comicsansms 12 italic").pack(anchor="w", padx=20, pady=1,ipadx=60.0)
            tk.Button(edit_win, text=" SAVE ", font="comicsansms 12 bold", justify="center",command=save_t_edits).pack(side="bottom", anchor="e", ipady=4, ipadx=30, pady=15, padx=15)
            edit_win.mainloop()

        edit_win = tk.Toplevel()
        edit_win.geometry("600x530")
        edit_win.minsize(600, 530)
        edit_win.maxsize(600, 530)
        tkb.Style(theam_selected)
        edit_win.title("Edit Student Details")
        tk.Label(edit_win, text="*Select Student To Edit This Details*", font="comicsansms 18 bold").pack(side="top",
                                                                                                          pady=20)
        tk.Label(edit_win, text="                     ", font="comicsansms 12 bold").pack(side="top", pady=3, padx=130,
                                                                                          anchor="w")
        tk.Label(edit_win, text="Roll no.                     Student Name", font="comicsansms 12 bold").pack(
            side="top", pady=2, padx=130, anchor="w")
        del_scrollbar = tk.Scrollbar(edit_win)
        del_scrollbar.pack(side="right", fill="y")
        list_box = tk.Listbox(edit_win, font="comicsansms 13 bold", width=40, height=15,
                              yscrollcommand=del_scrollbar.set)
        list_box.pack()
        del_scrollbar.config(command=list_box.yview)
        for i in teachers_data:
            list_box.insert(list_box.size(), f" {i}               :            {teachers_data[i][0]} ")
        tk.Button(edit_win, text=" Edit Details ", font="comicsansms 13 bold", command=edit_details).pack(side="bottom",ipadx=20,ipady=4,pady=20)
        edit_win.mainloop()
    def teacher_delete():
        def deleting():
            run = 1
            roll_select = int(list_box.curselection()[0]) + 1
            visit_tea_rec.append(f"Delete [Name : {teachers_data[roll_select][0]}]")
            del teachers_data[roll_select]
            dn = dict()
            for k in teachers_data.keys():
                if run == roll_select:
                    remove_path = os.path.join(Location, f"t_{roll_select}.jpg")
                    if os.path.exists(remove_path):
                        os.remove(remove_path)
                if run > roll_select:
                    file_path = os.path.join(Location, f"t_{run}.jpg")
                    new_roll = run - 1
                    new_file_path = os.path.join(Location, f"t_{new_roll}.jpg")
                    if os.path.exists(file_path):
                        os.rename(file_path, new_file_path)
                        print(fr"path is changed to : {new_file_path}")
                dn[run] = list(teachers_data[k])
                run = run + 1
            # for the last image
            file_path = os.path.join(Location, f"t_{run}.jpg")
            new_roll = run - 1
            new_file_path = os.path.join(Location, f"t_{new_roll}.jpg")
            if os.path.exists(file_path):
                os.rename(file_path, new_file_path)
                print(fr"path is changed to : {new_file_path}")

            fn = open(fr"{Location}\teacher.bin","wb")
            pk.dump(dn, fn)
            fn.close()
            del_win.destroy()
            t3_tea()

        del_win = tk.Toplevel()
        del_win.geometry("600x530")
        del_win.minsize(600, 530)
        del_win.maxsize(600, 530)
        tkb.Style(theam_selected)
        tk.Label(del_win, text="Delete Student Data By Choosing Roll No.", font="comicsansms 12 italic").pack(
            side="top", pady=10)
        tk.Label(del_win, text="Roll no.                Student Name", font="comicsansms 12 bold").pack(side="top",pady=10,padx=130,anchor="w")
        del_scrollbar = tk.Scrollbar(del_win)
        del_scrollbar.pack(side="right", fill="y")
        list_box = tk.Listbox(del_win, font="comicsansms 13 bold", width=40, height=15,yscrollcommand=del_scrollbar.set)
        list_box.pack()
        del_scrollbar.config(command=list_box.yview)
        for i in teachers_data:
            list_box.insert(list_box.size(), f" {i}               :            {teachers_data[i][0]} ")
        tk.Button(del_win, text=" DELETE ", font="comicsansms 11 italic", command=deleting).pack(side="bottom",ipadx=20, ipady=4,pady=20)

    teacher_win = tk.Toplevel()
    teacher_win.geometry("1280x860")
    teacher_win.minsize(1280, 860)
    tkb.Style(theam_selected)
    teacher_win.title("Teacher Section")
    search_val = StringVar()
    comman_menu(teacher_win, theam_selected)
    t1 = tk.Frame(teacher_win,border=2,relief="groove")
    t2 = tk.Frame(teacher_win,border=2,relief="groove")
    t3 = tk.Frame(teacher_win,border=2,relief="groove")
    t1.pack(side="left",fill="y", pady=5, padx=10, ipadx=100.0)
    t2.pack(side="top", fill="x", pady=5, padx=0, ipady=20.0)
    t3.pack(side="left", fill="both",pady=5,ipadx=700.0)
    tk.Button(t1, text="Teachers",font="comicsansms 13 bold",command=t3_tea).pack(pady=1, fill="x")

    edit_image = Image.open(fr"{Location}\edit_2.jpg")
    photo_edit = ImageTk.PhotoImage(edit_image.resize((80, 80)))
    edit_1 = tk.Button(t2, image=photo_edit,command=teacher_edite)
    edit_1.image = photo_edit
    edit_1.pack(side="left", padx=10)
    delete_image = Image.open(fr"{Location}\delete.jpg")
    photo_delete = ImageTk.PhotoImage(delete_image.resize((80, 80)))
    del_1 = tk.Button(t2, image=photo_delete,command=teacher_delete)
    del_1.image = photo_delete
    del_1.pack(side="left", padx=10)

    add_image = Image.open(fr"{Location}\add1.jpg")
    photo_add = ImageTk.PhotoImage(add_image.resize((80, 80)))
    add_1 = tk.Button(t2, image=photo_add,command=add_teacher)
    add_1.image = photo_add
    add_1.pack(side="left", padx=10)

    search_image = Image.open(fr"{Location}\search.jpg")
    photo_search = ImageTk.PhotoImage(search_image.resize((60, 60)))
    search_1 = tk.Button(t2, image=photo_search, command=tea_s)
    search_1.image = photo_search
    search_1.pack(side="right", padx=10)
    std_search = tk.Entry(t2, textvariable=search_val, font="comicsansms 20 italic", justify="left")
    std_search.pack(side="right", padx=0, ipady=3, ipadx=30)
    std_search.bind("<KeyRelease-Return>", tea_s)
    t3_tea()
    obj_teacher_read.close()
# Teacher section ended -------------------------------------------------------------------
# Setting section started -----------------------------------------------------------------
def setting_section():
    set_win = tk.Toplevel()
    set_win.geometry("880x720")
    set_win.minsize(880,720)
    set_win.maxsize(880,720)
    set_win.title("Setting")
    tkb.Style(theam_selected)
    def apply_theam():
        try:
            # when ever change this location also change it in error box of except bolck (just bleow)
            Basic_info_write = open(fr"{Location}\Basic info.bin", "wb")
            Basic_info["theam"] = theam_options[value.get()-1]
            visit_set_rec.append(f"Change them to {theam_options[value.get()-1]}")
            pk.dump(Basic_info,Basic_info_write)
            Basic_info_write.close()
        except:
            # show error box
            tmsg.showerror("ERROR","There is some problem in opening Basic file")
        tmsg.showinfo("Message","Please Restart the GUI.")
        exit()
    def check_password():
        if str(password_entery.get()) == Basic_info["password"]:
            visit_set_rec.append("CORRECT PASWORD")
            add_user.config(state="normal")
            delete_history.config(state="normal")
            del_user.config(state="normal")
            change_password.config(state="normal")
            change_location.config(state="normal")
            password_entery.set(value="Correct Password")
            pass_value.config(state="disabled")
        else:
            global password_try
            password_try += 1
            if password_try >3:
                tmsg.showwarning("Setting","You have try the password more than 3 times")
                exit()
            password_entery.set(value="")
            tmsg.showwarning("Password","  Wrong Password  ")
    def clear_history():
        response = tmsg.askokcancel("Delete History","Are you sure to Delete all users History")
        if response==True:
            visit_set_rec.append("**DELETE HISTORY OF USERS**")
            fn = open(fr"{Location}\History.bin", "wb")
            pk.dump(list(), fn)
            fn.close()
    def ADD_user():
        def joint_user():
            try:
                dn = dict()
                for i in Basic_info:
                    dn[i] = Basic_info[i]
                u_list = list(dn["user_name"])
                u_list.append(str(add_user_name.get()).upper())
                dn["user_name"] = u_list
                visit_set_rec.append(f"Add new user [Name : {str(add_user_name.get()).upper()}]")
                fn = open(fr"{Location}\Basic info.bin","wb")
                pk.dump(dn,fn)
                fn.close()
                tmsg.showinfo("Message","You can check add user by Restart GUI")
            except:
                tmsg.showinfo("Message","Please contact the devloper")

        q = tk.Toplevel()
        q.geometry("380x220")
        q.minsize(380, 220)
        q.maxsize(380, 220)
        q.title("User")
        tkb.Style(theam_selected)
        tk.Label(q,text="Enter user name below").pack(pady=5)
        add_user_name = StringVar()
        tk.Label(q,text="User Name :",font="comicsansms 16 italic").pack(pady=5)
        tk.Entry(q,textvariable=add_user_name,font="comicsansms 16 italic",justify="center").pack()
        tk.Button(q,text="ADD",font="comicsansms 14 bold",command=joint_user).pack(pady=10,ipadx=10)
    def DELETE_user():
        def del_user_name():
            user_index = int(l0.curselection()[0])
            ln = list(Basic_info["user_name"])

            if ln[user_index]=="HUMENDRA":
                tmsg.showwarning("You can not delet this user")
                exit()
            visit_set_rec.append(f"Delet user [Name : {ln[user_index]}]")
            ln.remove(ln[user_index])
            Basic_info["user_name"] = ln
            fn = open(fr"{Location}\Basic info.bin","wb")
            pk.dump(Basic_info,fn)
            fn.close()
            tmsg.showinfo("Message", "You can check add user by Restart GUI")

        d = tk.Toplevel()
        d.geometry("380x520")
        d.minsize(380, 520)
        d.maxsize(380, 520)
        d.title("User")
        tkb.Style(theam_selected)
        tk.Label(d,text="Select user name to delete")
        l0 = tk.Listbox(d,font="comicsansms 13 bold")
        l0.pack(pady=20,padx=10,fill="x",ipady=100)
        for k in Basic_info["user_name"]:
            l0.insert(l0.size(),k)
        tk.Button(d,text="Delete",font="comicsansms 13 bold",command=del_user_name).pack(pady=10,ipady=5,ipadx=20)
    def CHANGE_password():
        def new_password():
            if sv1.get()==sv2.get():
                if sv1.get().isspace() or sv1.get()=="":
                    tmsg.showinfo("PASSWORD","Password can not be spaces or nothing.")
                    pas.destroy()
                    CHANGE_password()
                Basic_info["password"] = str(sv1.get())
                visit_set_rec.append(f"CHANGE PASSWORD")
                fn = open(fr"{Location}\Basic info.bin", "wb")
                pk.dump(Basic_info, fn)
                fn.close()
                delete_history.config(state="disabled")
                add_user.config(state="disabled")
                del_user.config(state="disabled")
                change_password.config(state="disabled")
                change_location.config(state="disabled")
                password_entery.set(value="")
                pass_value.config(state="normal")
                pas.destroy()
            else:
                tmsg.showwarning("PASSWORD","Password is not conformed please try again.")
                pas.destroy()
                CHANGE_password()

        pas = tk.Toplevel()
        pas.geometry("320x240")
        pas.minsize(320, 240)
        pas.maxsize(320, 240)
        pas.title("PASSWORD")
        sv1 = StringVar()
        sv2 = StringVar()
        tk.Label(pas,text="    ").pack(side="top",pady=1)
        tk.Label(pas,text="New Password",font="comicsansms 13 bold").pack(anchor="nw",padx=10)
        tk.Entry(pas,textvariable=sv1,justify="center",font="comicsansms 13 italic").pack(anchor="nw",padx=10,ipadx=30)
        tk.Label(pas, text="    ").pack(side="top", pady=1)
        tk.Label(pas,text="Conform Password",font="comicsansms 13 bold").pack(anchor="nw",padx=10)
        tk.Entry(pas, textvariable=sv2, justify="center",show="*" ,font="comicsansms 13 italic").pack(anchor="nw",padx=10,ipadx=30)
        tk.Button(pas,text="SAVE",font="comicsansms 13 bold",command=new_password).pack(side="bottom",pady=20,padx=20,fill="x",ipady=1)
    def CHANGE_location():
        def update_location():
            try:
                if new_location.get().isspace() or new_location.get()=="":
                    tmsg.showwarning("Location","No path is given")
                    exit()
                if os.path.exists(new_location.get()):
                    Basic_info["location"] = fr"{new_location.get()}"
                    visit_set_rec.append(fr"LOCATION CHANGED : {new_location.get()}")
                    fn = open(fr"{Location}\Basic info.bin", "wb")
                    pk.dump(Basic_info, fn)
                    fn.close()
                else:
                    tmsg.showerror("Location","Given path does not exist.")
            except:
                tmsg.showinfo("Message","Ther is some problem in location path")
        if user_name.get().upper()=="HUMENDRA":
            lo = tk.Toplevel()
            lo.geometry("720x110")
            lo.minsize(720, 110)
            lo.maxsize(720, 110)
            lo.title("Location")
            tkb.Style(theam_selected)
            new_location = StringVar()
            tk.Label(lo, text="Copy past nwe folder location ", font="comicsansms 10 bold").pack(anchor="nw", padx=10)
            tk.Entry(lo, textvariable=new_location, justify="center", font="comicsansms 13 italic").pack(anchor="nw", padx=10,ipadx=240)
            tk.Button(lo,text="Change Location", font="comicsansms 10 bold",command=update_location).pack(anchor="w",ipadx=20,pady=20,padx=10)
        else:
            tmsg.showinfo("Message","Sorry only Principal can change the location.")

    s1 = tk.Frame(set_win,border=0,relief="sunken")
    s1.pack(side="top",pady=10,padx=10,fill="x")
    try:
        runing_theam = theam_options.index(theam_selected) + 1
    except:
        runing_theam = 6
    value = IntVar(value=runing_theam)
    tk.Label(s1,text="Choices For Themes").grid(row=0,column=0)
    tk.Checkbutton(s1,text=f"{theam_options[0]}",variable=value,onvalue=1,font="comicsansms 13 bold").grid(row=1,column=1)
    tk.Checkbutton(s1,text=f"{theam_options[1]}",variable=value,onvalue=2,font="comicsansms 13 bold").grid(row=2,column=1)
    tk.Checkbutton(s1,text=f"{theam_options[2]}",variable=value,onvalue=3,font="comicsansms 13 bold").grid(row=3,column=1)
    tk.Checkbutton(s1,text=f"   {theam_options[3]}",variable=value,onvalue=4,font="comicsansms 13 bold").grid(row=4,column=1)
    tk.Label(s1,text="\t\t\t\t").grid(row=1,column=2)
    tk.Label(s1,text="\t\t\t\t").grid(row=2,column=2)
    tk.Label(s1,text="\t\t\t\t").grid(row=3,column=2)
    tk.Label(s1,text="\t\t\t\t").grid(row=4,column=2)
    tk.Checkbutton(s1,text=f"{theam_options[4]}",variable=value,onvalue=5,font="comicsansms 13 bold").grid(row=1,column=3)
    tk.Checkbutton(s1,text=f"       {theam_options[5]}",variable=value,onvalue=6,font="comicsansms 13 bold").grid(row=2,column=3)
    tk.Checkbutton(s1,text=f"      {theam_options[6]}",variable=value,onvalue=7,font="comicsansms 13 bold").grid(row=3,column=3)
    tk.Checkbutton(s1,text=f"        {theam_options[7]}",variable=value,onvalue=8,font="comicsansms 13 bold").grid(row=4,column=3)
    tk.Button(s1,text="  Apply  ",font="comicsansms 12 bold",command=apply_theam).grid(row=7,column=2)

    s2 =tk.Frame(set_win,border=1,relief="sunken")
    s2.pack(side="top", pady=10, padx=10, fill="x")
    tk.Label(s2,text="For Further Setting Options You Need To Enter PASSWORD",font="comicsansms 10 bold").pack(pady=10)
    password_entery = StringVar()
    tk.Label(s2, text="Enter PASSWORD :", font="comicsansms 13 bold").pack(anchor="n",side="left",pady=10)
    pass_value = tk.Entry(s2,textvariable=password_entery,show="*",font="comicsansms 18 italic",justify="center")
    pass_value.pack(anchor="n",side="left",padx=10,pady=5)
    tk.Button(s2,text="Submit Password",font="comicsansms 11 bold",command=check_password).pack(anchor="n",side="right",padx=5,ipady=2,ipadx=4)

    s3 = tk.Frame(set_win,border=0,relief="sunken")
    s3.pack(side="top", pady=10, padx=10, fill="both")
    add_user = tk.Button(s3,text="  Add User  ",font="comicsansms 18 bold",state="disabled",command=ADD_user)
    del_user = tk.Button(s3,text=" Delet User ",font="comicsansms 18 bold",state="disabled",command=DELETE_user)
    change_password = tk.Button(s3,text=" Change Password ",font="comicsansms 18 bold",state="disabled",command=CHANGE_password)
    change_location = tk.Button(s3,text=" Change Location ",font="comicsansms 18 bold",state="disabled",command=CHANGE_location)
    delete_history = tk.Button(s3,text=" Delete History ",font="comicsansms 18 bold",state="disabled",command=clear_history)
    add_user.pack(side="bottom",padx=10,pady=10,fill="x")
    del_user.pack(side="bottom",padx=10,pady=10,fill="x")
    change_password.pack(side="bottom",padx=10,pady=10,fill="x")
    change_location.pack(side="bottom",padx=10,pady=10,fill="x")
    delete_history.pack(side="bottom",padx=10,pady=10,fill="x")
# Setting section ended -------------------------------------------------------------------
# History section started -----------------------------------------------------------------
def history_section():
    # Record that the history view was accessed
    visit_his_rec.append("View History")
    # Create a new top-level window
    his_win = tk.Toplevel()
    w = his_win.winfo_screenwidth()
    h = his_win.winfo_screenheight()
    his_win.geometry(f"{w}x{h}")
    his_win.minsize(w, h)
    his_win.maxsize(w, h)
    his_win.title("History")
    tkb.Style(theam_selected)
    # Create a frame to hold the text widget and scrollbars
    frame = tk.Frame(his_win)
    frame.pack(fill='both', expand=True)
    # Create the horizontal scrollbar
    x_scrollbar = tk.Scrollbar(frame, orient='horizontal')
    x_scrollbar.pack(side='bottom', fill='x')
    # Create the vertical scrollbar
    y_scrollbar = tk.Scrollbar(frame, orient='vertical')
    y_scrollbar.pack(side='right', fill='y')
    # Create a Text widget that does not wrap text (to enable horizontal scrolling)
    text_widget = tk.Text(frame, wrap='none',xscrollcommand=x_scrollbar.set,yscrollcommand=y_scrollbar.set)
    text_widget.pack(fill='both', expand=True)
    # Configure the scrollbars to scroll the text widget
    x_scrollbar.config(command=text_widget.xview)
    y_scrollbar.config(command=text_widget.yview)

    h_fileobj = open(fr"{Location}\History.bin","rb")
    his_list = pk.load(h_fileobj)
    h_fileobj.close()
    for d in his_list:
        text_widget.insert("end","\n")
        for v in d:
            text_widget.insert("end",f"User : {v} at {d[v][0]}\n")
            if len(d[v])<=1:
                pass
            for i in d[v]:
                if i == d[v][0]:
                    pass
                else:
                    s = "\t\t"
                    for j in i:
                        s = s +"--"+ j
                    text_widget.insert("end",s + "\n")
            text_widget.insert("end","\n")


# History section ended -------------------------------------------------------------------

# Definations above

#-----------------------------------------------------------------------------------------------------------------------
window_pass = tk.Tk()
window_pass.geometry("444x266")
window_pass.minsize(444,266)
window_pass.maxsize(444,266)
window_pass.title("Wellcome to KV3 School GUI")
style = tkb.Style(theam_selected)
user_name = StringVar()
tkb.Label(window_pass,text=" WELLCOME TO KV3 JAIPUR ",bootstyle="info",padding=(20,10),
          anchor="n",font="comicsansms 18 bold").pack(side="top",fill="x")
tkb.Label(window_pass,text="SOFTWARE",bootstyle="info",padding=(20,0),
          anchor="n",font="comicsansms 18 bold").pack(side="top",fill="x")
f1 = tkb.Frame(window_pass,bootstyle="default",borderwidth=7)
f1.pack(fill="x",pady=10)
tkb.Label(f1,text="NAME :",bootstyle="success",padding=(30,20),anchor="nw",font="comicsansms 10 bold").grid(row=0,column=0)
if theam_selected in ("cosmo","lumen","morph"):
    username_entred = tkb.Entry(f1,textvariable=user_name,bootstyle="success",foreground="black",font="comicsansms 12 italic",justify="center",width=25)
    username_entred.grid(row=0,column=2)
    # keyboard event when ENTER button is pressed
    username_entred.bind("<KeyRelease-Return>", keyboard_enter)
else:
    username_entred = tkb.Entry(f1, textvariable=user_name, bootstyle="success", foreground="pink",font="comicsansms 12 italic", justify="center", width=25)
    username_entred.grid(row=0, column=2)
    # keyboard event when ENTER button is pressed
    username_entred.bind("<KeyRelease-Return>", keyboard_enter)
# calling check_pass def
tkb.Button(window_pass,text=" Submit ",bootstyle="success",command=check_pass,padding=(20,10)).pack(side="top")
window_pass.mainloop()

#_______________________________________________________________________________________________________________________
# Enter in main gui
if continuty==1:
    root = tk.Tk()
    root.geometry("1280x860")
    root.minsize(1280, 860)
    root.title("Student Section")
    tkb.Style(theam_selected)
    search_val = StringVar()
    f1 = tk.Frame(root, border=2, relief="groove")
    f2 = tk.Frame(root, border=2, relief="groove")
    f3 = tk.Frame(root, border=2, relief="groove")
    f1.pack(side="left", fill="y", pady=5, padx=10, ipadx=60.0)
    f2.pack(side="top", fill="x", pady=5, padx=0, ipady=20.0)
    f3.pack(side="left", fill="both",pady=5,ipadx=700.0)
    student_section()
    root.mainloop()