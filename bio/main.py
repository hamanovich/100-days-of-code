from tkinter import *
from tkinter import font
import webbrowser
from random import randint

from draggable import DraggableWidget
import bio_data

TITLE = bio_data.project_title

window = Tk()
window.geometry("900x600+1000+300")
window.resizable(0, 0)
window.title(TITLE)
window.rowconfigure(0, minsize=900, weight=1)
window.columnconfigure(1, minsize=600, weight=1)


def clear_frame_content(frame):
    frame.grid_remove()
    for widget in frame.winfo_children():
        widget.destroy()


def choose_topic(topic):
    global btn_home
    for btn in menu_btns:
        btn.config(highlightbackground="lightgreen", fg="black")
    btn_index = [index for index, (label, _) in enumerate(
        bio_data.menu_buttons) if label == topic]

    btn = menu_btns[btn_index[0]]
    btn.config(highlightbackground="green", fg="green")

    lbl_main.config(text=topic)

    frm_landing.grid_remove()
    clear_frame_content(frm_task_1)
    clear_frame_content(frm_task_2)
    clear_frame_content(frm_cytology)

    if topic == "Ботаника":
        task_1()

    if topic == "Анатомия":
        task_2()

    if topic == "Цитология":
        cytology_tasks()

    if btn_home is None:
        btn_home = Button(frm_menu_buttons,
                          text="🏠",
                          cursor="hand2",
                          highlightbackground=frm_panel.cget("bg"),
                          font=font.Font(size=20),
                          command=go_home)
        btn_home.grid(row=5, column=0, pady=5, sticky=EW)


def on_button_click(index):
    current_text = entry_answer.get()
    updated_text = f"{current_text} {index}"
    entry_answer.config(bg="white", fg="black")
    entry_answer.delete(0, END)
    entry_answer.insert(0, updated_text)


def check_result():
    result = entry_answer.get()
    formatted_result = ''.join(result.split())

    if formatted_result == bio_data.data["Ботаника"]["tasks"][0]["answer"]:
        entry_answer.config(bg="green", fg="white")
    else:
        entry_answer.config(bg="red", fg="white")


# ==========
# LEFT PANEL
def go_home():
    global btn_home
    frm_landing.grid()
    clear_frame_content(frm_task_1)
    clear_frame_content(frm_task_2)
    clear_frame_content(frm_cytology)
    clear_frame_content(btn_home)
    btn_home = None

    for btn in menu_btns:
        btn.config(highlightbackground="lightgreen", fg="black")


def left_panel_ui():
    global menu_btns
    global btn_home
    global frm_panel
    global frm_menu_buttons
    frm_panel = Frame(window, bg="lightgreen", relief=RAISED, bd=2)
    frm_panel.grid(row=0, column=0, sticky=NSEW)
    frm_panel.rowconfigure(2, weight=1)

    lbl_panel = Label(frm_panel, text="Выберите раздел:", bg="#333")
    lbl_panel.grid(row=0, column=0, padx=5, pady=15)

    frm_menu_buttons = Frame(frm_panel, bg="lightgreen")
    frm_menu_buttons.grid(row=1, column=0, padx=10, sticky=NSEW)
    menu_btns = []
    for idx, (menu_name_item, _) in enumerate(bio_data.menu_buttons):
        btn_menu = Button(frm_menu_buttons,
                          text=menu_name_item,
                          cursor="hand2",
                          highlightbackground=frm_panel.cget("bg"),
                          font=font.Font(size=20),
                          command=lambda topic=menu_name_item: choose_topic(topic))
        btn_menu.grid(row=idx, column=0, pady=5, sticky=EW)
        menu_btns.append(btn_menu)

    btn_home = None

    frm_copyrights = Frame(frm_panel, bg=frm_panel.cget("bg"))
    frm_copyrights.grid(row=2, column=0)

    lbl_copyrights = Label(frm_copyrights, text="СШ №8, Биология,\n2023", bg=frm_panel.cget(
        "bg"), fg="black", font=font.Font(size=10))
    lbl_copyrights.grid(row=0, column=0)


# ============
# MAIN CONTENT
frm_main = Frame(bg="lightgreen")
frm_main.grid(row=0, column=1, sticky=NSEW)
frm_main.columnconfigure(0, weight=1)

lbl_main = Label(frm_main, text=TITLE, bg="lightgreen", fg="black",
                 font=font.Font(size=50), anchor="center")
lbl_main.grid(row=0, column=0, columnspan=3, pady=(0, 15), sticky=EW)

frm_content = Frame(frm_main, padx=5, pady=5, bg=frm_main.cget("bg"))
frm_content.grid(row=1, column=0)

frm_landing = Frame(frm_content, bg="#333")
frm_landing.grid(row=0, column=0)

frm_task_1 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_1.grid(row=0, column=0)

frm_task_2 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_2.grid(row=0, column=0)

frm_cytology = Frame(frm_content, bg=frm_main.cget("bg"))
frm_cytology.grid(row=0, column=0)


# ============
# LANDING SCREEN


def landing():
    lbl_landing = Label(frm_landing, anchor=W, text=f"Выберите раздел", font=font.Font(size=20),
                        pady=30)
    lbl_landing.grid(row=0, column=0, columnspan=4)

    for idx, (frm_name, frm_img) in enumerate(bio_data.menu_buttons):
        frm = Frame(frm_landing, borderwidth=2, relief=GROOVE, cursor="hand2")
        frm.grid(row=1, column=idx, padx=10, pady=10)
        image = PhotoImage(file=frm_img)
        lbl_image = Label(frm, image=image)
        lbl_image.image = image
        lbl_image.grid(row=0, column=0)
        lbl_image.bind("<Button-1>", lambda _,
                       topic=frm_name: choose_topic(topic))
        lbl_text = Label(frm, text=frm_name)
        lbl_text.grid(row=1, column=0)
        lbl_text.bind("<Button-1>", lambda _,
                      topic=frm_name: choose_topic(topic))


# =============
# TASKS CONTENT

# БОТАНИКА


def task_1():
    global entry_answer
    frm_task_1.grid()

    lbl_task = Label(frm_task_1, anchor=W, wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=bio_data.data["Ботаника"]["tasks"][0]["question"])
    lbl_task.grid(row=0, column=0)

    entry_answer = Entry(frm_task_1, bg="white",
                         fg="black", font=font.Font(size=20))
    entry_answer.grid(row=1, column=0, pady=10, sticky=EW)

    for (idx, option) in bio_data.data["Ботаника"]["tasks"][0]["options"]:
        row_frame = Frame(frm_task_1)
        row_frame.grid(row=idx+1, column=0, sticky=EW)
        row_frame.columnconfigure(1, weight=1)

        label = Label(row_frame, text=f"{idx}.", font=font.Font(size=20))
        label.grid(row=0, column=0, sticky="w")

        button = Button(row_frame,
                        text=option,
                        cursor="hand2",
                        anchor=W,
                        font=font.Font(size=18),
                        command=lambda i=idx: on_button_click(i))
        button.grid(row=0, column=1, padx=(5, 0), sticky=EW)

    check_result_button = Button(
        frm_task_1, text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_result)
    check_result_button.grid(row=10, column=0, pady=10, sticky=EW)


# ======
# АНАТОМИЯ


def task_2():
    frm_task_2.grid()
    lbl_task = Label(frm_task_2,
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=bio_data.data["Анатомия"]["tasks"][0]["question"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

    tk_image = PhotoImage(file="images/eye_350.png")
    image_label = Label(frm_task_2, image=tk_image)
    image_label.image = tk_image
    image_label.grid(row=1, column=0)

    def check_position(name, x, y):
        match_option = [option for (
            n, option) in bio_data.data["Анатомия"]["tasks"][0]["options"] if n == name][0]
        match_btn = [
            btn for btn in draggable_buttons if btn.cget("text") == name][0]

        if (abs(match_option["x"] - x)) < 15 and abs(match_option["y"] - y) < 15:
            match_btn.config(highlightbackground="green", fg="green")
        else:
            match_btn.config(highlightbackground="red", fg="red")

        print(f"EL: {name}: {match_option}. Result should be {x}:{y}")

    draggable_buttons = []
    for (name, _) in bio_data.data["Анатомия"]["tasks"][0]["options"]:
        draggable_label = DraggableWidget(
            image_label, cursor="hand2", relief=RAISED, bd=1, text=name, on_release_callback=check_position)
        draggable_label.place(x=randint(5, 200), y=randint(5, 320))
        draggable_buttons.append(draggable_label)

    # check_result_button = Button(
    #     frm_task_2, text="Проверить результат", font=font.Font(size=20), command=check_result)
    # check_result_button.grid(row=2, column=0, pady=10, sticky=EW)

    link_label = Label(
        frm_task_2, text="Узнать больше на Youtube.com", fg="lightgreen", cursor="hand2")
    link_label.grid(row=3, column=0, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open("https://youtu.be/rSVDJyqHXQk?si=3pPhfFCKeMs-yn3R"))


# ======
# ЦИТОЛОГИЯ


def cytology_tasks():
    frm_cytology.grid()
    lbl_intro = Label(frm_cytology, anchor=W, wraplength=500, bg=frm_main.cget("bg"), fg="black",
                      pady=30,
                      text=bio_data.data["Цитология"]["intro"])
    lbl_intro.grid(row=0, column=0)
    lbl_task = Label(frm_cytology, anchor=W,
                     text="Проект в процессе наполнения данными ⏰", font=font.Font(size=24))
    lbl_task.grid(row=3, column=0)


# =====
if __name__ == "__main__":
    left_panel_ui()
    landing()
    window.mainloop()
