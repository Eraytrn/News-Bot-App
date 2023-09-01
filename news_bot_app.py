import feedparser
from tkinter import *
import webview

def default_color_button():
    btn_latest_news.configure(bg="lightblue")
    btn_world.configure(bg="lightblue")
    btn_economy.configure(bg="lightblue")
    btn_health.configure(bg="lightblue")


def clear_frame():
    for widget in fr_news.winfo_children():
        widget.destroy()

def open_url(event):
    webview.create_window(event.widget.cget("text"),event.widget.cget("text"))
    webview.start()

def add_news(news):
    news_count=0
    for nw in news.entries:
        news_count = news_count + 1
        if news_count >2:
            break
        Label(fr_news, text=nw.title, anchor="w", font=("Helveticabold",14)).pack(side=TOP,fill="x")
        lbl_link=Label(fr_news, text=nw.link, anchor="w", font=("Helveticabold", 14),fg="blue",cursor="hand2")
        lbl_link.pack(side=TOP, fill="x")
        lbl_link.bind("<Button-1>", open_url)
        Label(fr_news, text="-", anchor="c",bg="pink", cursor="hand2").pack(side=TOP,fill="x")

def latest_news_command():
    clear_frame()
    default_color_button()
    btn_latest_news.configure(bg="blue")
    for url in latest_news_url:
     news = feedparser.parse(url)
     add_news(news)

def world_command():
    clear_frame()
    default_color_button()
    btn_world.configure(bg="blue")
    for url in world_url:
     news = feedparser.parse(url)
     add_news(news)

def economy_command():
    clear_frame()
    default_color_button()
    btn_economy.configure(bg="blue")
    for url in economy_url:
     news = feedparser.parse(url)
     add_news(news)

def health_command():
    clear_frame()
    default_color_button()
    btn_health.configure(bg="blue")
    for url in health_url:
     news = feedparser.parse(url)
     add_news(news)


latest_news_url = ["https://www.sozcu.com.tr/rss/son-dakika.xml",
                   "https://www.ensonhaber.com/rss/ensonhaber.xml",
                   "https://www.cnnturk.com/feed/rss/all/news",
                   "https://www.milliyet.com.tr/rss/rssnew/sondakikarss.xml?"]

world_url = ["https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml",
             "https://www.sozcu.com.tr/rss/dunya.xml",
             "https://www.ensonhaber.com/rss/dunya.xml",
             "https://www.cnnturk.com/feed/rss/dunya/news"]

economy_url = ["https://www.cnnturk.com/feed/rss/ekonomi/news",
               "https://www.ensonhaber.com/rss/ekonomi.xml",
               "https://www.milliyet.com.tr/rss/rssnew/ekonomirss.xml",
               "https://www.sozcu.com.tr/rss/ekonomi.xml"]

health_url = ["https://www.cnnturk.com/feed/rss/saglik/news",
              "https://www.ensonhaber.com/rss/saglik.xml",
              "https://www.sozcu.com.tr/rss/saglik.xml",
              "https://haberglobal.com.tr/rss/saglik"]

window = Tk()
window.title("News Bot Program")
window.geometry("1000x600")



fr_news = Frame(window, height=600)
fr_buttons = Frame(window,relief=RAISED, bg="pink",bd=2)


btn_latest_news = Button(fr_buttons, text="Latest News", font=("Helveticabold",14),bg="lightblue",command=latest_news_command)
btn_world = Button(fr_buttons, text="World", font=("Helveticabold",14),bg="lightblue",command=world_command)
btn_economy = Button(fr_buttons, text="Economy", font=("Helveticabold",14),bg="lightblue",command=economy_command)
btn_health = Button(fr_buttons, text="Health", font=("Helveticabold",14),bg="lightblue",command=health_command)


btn_latest_news.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_world.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_economy.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_health.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
fr_news.grid(row=0, column=1, sticky="nsew")


window.mainloop()