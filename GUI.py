from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile
from GUI_Helper import make_csv, api, refine_picks, make_leaderboard

# add search bar to search for a name and display it

class App:
    def __init__(self) -> None:    
        self.root = Tk()
        # STYLE
        self.s = ttk.Style()
        self.s.theme_use('alt')
        self.s.configure('TButton', background = 'blue', foreground = 'white', width = 20, font=("Arial", 15), borderwidth=1, focusthickness=3, focuscolor='none')
        self.s.map('TButton', background=[('active','blue')])

        self.WIDTH, self.HEIGHT = 2000, 1000
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.title("Football Pool")

         # TITLE
        self.title = Label(self.root, text="Leaderboard", font=("Arial", 40))
        self.title.pack(side=TOP, pady=(40, 0))

        # DESCRIPTION
        self.description = ttk.Label(self.root, text="Please enter a week number and select a Word Document (.docx)", font=("Arial", 15))
        self.description.pack(pady=20)

        # INPUT FIELD
        # frame to center content
        self.input_frame = Frame(self.root)
        self.week = Entry(self.input_frame, width=20, font=("Arial", 16))
        self.week.insert(0, "Enter week number:")
        self.week.bind("<Button-1>", self.call_back)
        self.upload_button = ttk.Button(self.input_frame, width=15,text="Upload File", command=self.start) 

        self.input_frame.pack(pady=(0, 40))
        self.week.grid(row=0, column=0, padx=30)
        self.upload_button.grid(row=0, column=1)

        # self.root.after(3000, lambda: self.root.destroy())

    def start(self):
        week_number = self.week.get()
        prize_total = 0

        docx_file_path = askopenfile(mode='r', filetypes=[('Word Document', '*docx')]).name
        docx_file_name = docx_file_path.split("/")[-1]
        csv_name = docx_file_name.split(".")[0]
        csv_name = f"{csv_name}.csv"

        if not week_number.isnumeric():
            self.week.delete(0, END)
            self.week.insert(0, "Please enter a number")
        elif docx_file_path is not None:
            make_csv(docx_file_path, csv_name)
            winning_teams = api(week_number)
            picks = refine_picks(csv_name)
            winners = make_leaderboard(winning_teams, picks, prize_total)
            

        # BUILD TREE
        self.s.configure('Treeview', rowheight=70)
        self.tree = ttk.Treeview(self.root, selectmode="browse")

        self.tree["show"] = "headings"
        self.tree["columns"] = ("place", "name", "count")

        self.tree.column("place", anchor="c")
        self.tree.column("name", anchor="c")
        self.tree.column("count", anchor="c")

        self.tree.heading("place", text="Place")
        self.tree.heading("name", text="Name")
        self.tree.heading("count", text="Win Count")

        # INSERT INTO TREE
        for i in range(len(winners)):
            print(winners)
            self.tree.insert("", "end", values=(winners[i]["place"], winners[i]["name"], winners[i]["count"]))


        self.scroll = ttk.Scrollbar(self.root)
        self.scroll.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=BOTH)
        self.tree.pack(side=TOP, expand=TRUE, fill=BOTH) 

    def call_back(self, e):
        self.week.delete(0, END)


app = App()
app.root.mainloop()
