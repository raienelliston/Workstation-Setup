#Module for opening applications on the system, including websites, applications, and files
import os
import webbrowser

def open_application(path):
    try:
        os.startfile(path)
    except Exception as e:
        print(f"Failed to open application: {e}")

def open_website(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Failed to open website: {e}")


def open_file(path):
    try:
        os.startfile(path)
    except Exception as e:
        print(f"Failed to open file: {e}")

def open_aplications(applications):
    for app in applications:
        if app.type == "application":
            open_application(app.path)
        elif app.type == "website":
            open_website(app.path)
        elif app.type == "file":
            open_file(app.path)
        else:
            print(f"Unknown application type: {app.type}")
    return True
if __name__ == "__main__":
    None