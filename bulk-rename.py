import os, argparse
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
	def __init__(self, master=None):
		parser = argparse.ArgumentParser()
		parser.add_argument("-n", "--nobrowse", help="use working directory", action="store_true")
		args = parser.parse_args()

		if args.nobrowse:
			self.directory = "./"
		else:
			self.directory = filedialog.askdirectory(initialdir="./", title="select directory...") + "/"

		super().__init__(master)
		self.master = master;
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.filenames = os.listdir(self.directory)

		self.filename_entry_fields = []
		for i in range(0, len(self.filenames)):
			self.filename_entry_fields.append(tk.Entry(self))
			self.filename_entry_fields[i].insert(0, self.filenames[i])
			self.filename_entry_fields[i].pack(side="top")
		self.filename_entry_fields[0].focus_force()

		self.save_and_quit = tk.Button(self, text="Save and Quit",
									command=self.rename_files)
		self.save_and_quit.pack()

		self.quit = tk.Button(self, text="Quit",
							command=self.master.destroy)
		self.quit.pack(side="bottom")

	def rename_files(self):
		for i in range(0, len(self.filenames)):
			os.rename(self.directory + self.filenames[i], self.directory + self.filename_entry_fields[i].get())
		self.master.destroy()

root = tk.Tk()
app = Application(master=root)
app.mainloop()