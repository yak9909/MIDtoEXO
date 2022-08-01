import mid2exogui
import os
import json

print("起動中…")

themes = {
    "light": ["arc", "#d3d3d3"],
    "dark": ["equilux", "#656565"]
}

theme = themes["light"]

if os.path.exists("./config.json"):
    config = json.load( open("./config.json", mode="r", encoding="utf-8") )
    if config.get("dark_mode"):
        theme = themes["dark"]

main = mid2exogui.Main(theme=theme)
main.mainloop()