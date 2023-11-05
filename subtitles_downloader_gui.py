import os
import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import xmlrpc.client

class SubtitleDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Subtitle Downloader")
        
        # OpenSubtitles API user agent
        self.user_agent = "Wget/1.19.4 (linux-gnu)"
        self.client = xmlrpc.client.ServerProxy("http://api.opensubtitles.org/xml-rpc")
        self.token = None
        self.subtitles_list = []

        self.create_widgets()
        self.setup_grid()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter Movie Name:")
        self.label.grid(row=0, column=0, sticky="ew")

        self.entry = tk.Entry(self.root)
        self.entry.grid(row=0, column=1, sticky="ew")

        self.search_button = tk.Button(self.root, text="Search Subtitles", command=self.search_subtitles)
        self.search_button.grid(row=0, column=2, sticky="ew")

        self.subtitle_listbox = tk.Listbox(self.root)
        self.subtitle_listbox.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.download_button = tk.Button(self.root, text="Download Selected Subtitle", command=self.download_subtitle)
        self.download_button.grid(row=2, column=0, columnspan=3, sticky="ew")

    def setup_grid(self):
        self.root.grid_rowconfigure(1, weight=1)  # This makes the listbox expand vertically.
        self.root.grid_columnconfigure(1, weight=1)  # This makes the entry and listbox expand horizontally.

    def search_subtitles(self):
        movie_name = self.entry.get()
        if not movie_name:
            messagebox.showerror("Error", "Please enter a movie name")
            return

        self.token = self.client.LogIn("", "", "en", self.user_agent)["token"]

        results = self.client.SearchSubtitles(self.token, [{"query": movie_name, "sublanguageid": "eng"}])
        if "data" not in results:
            messagebox.showerror("Error", results["status"])
            return

        self.subtitles_list = results["data"]
        if not self.subtitles_list:
            messagebox.showinfo("No subtitles found", "No subtitles found for movie: " + movie_name)
            return

        self.subtitle_listbox.delete(0, tk.END)
        for i, subtitle in enumerate(self.subtitles_list):
            self.subtitle_listbox.insert(tk.END, f"{i + 1}. {subtitle['SubFileName']}")

    def download_subtitle(self):
        if not self.subtitles_list:
            messagebox.showwarning("No Subtitle Selected", "Please search and select a subtitle to download.")
            return
        
        selection = self.subtitle_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Subtitle Selected", "Please select a subtitle from the list.")
            return

        subtitle = self.subtitles_list[selection[0]]
        subtitle_url = subtitle["ZipDownloadLink"]
        movie_name = subtitle["SubFileName"]

        download_dir = simpledialog.askstring("Download Directory", "Enter download directory:", initialvalue=r"D:\Desktop")
        if not download_dir:
            messagebox.showwarning("No Directory", "No download directory specified.")
            return

        response = requests.get(subtitle_url)
        file_path = os.path.join(download_dir, movie_name)
        with open(file_path, "wb") as f:
            f.write(response.content)

        messagebox.showinfo("Download Complete", f"Subtitle downloaded to: {file_path}")

        self.client.LogOut(self.token)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")  # Set the initial size of the window
    app = SubtitleDownloaderApp(root)
    root.mainloop()
