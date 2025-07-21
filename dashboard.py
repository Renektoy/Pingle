import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("IoT Room Dashboard")

# Set window size (instead of fullscreen)
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Configure grid layout for the main window
root.grid_rowconfigure(0, weight=1)  # Main section
root.grid_rowconfigure(1, weight=0)  # Alerts section
root.grid_columnconfigure(0, weight=0)  # Sidebar
root.grid_columnconfigure(1, weight=1)  # Main Content (Dashboard)
root.grid_columnconfigure(2, weight=0)  # Environment Panel

# Sidebar frame for navigation buttons (left)
sidebar_frame = tk.Frame(root, width=200, bg="lightgray")
sidebar_frame.grid(row=0, column=0, sticky="ns")

# Button list for different tabs
tabs = ["Dashboard", "Devices", "Rooms", "Automations", "Settings"]
for tab in tabs:
    button = tk.Button(sidebar_frame, text=tab, command=lambda t=tab: change_tab(t))
    button.pack(fill='x', padx=10, pady=5)

# Main content frame (for dashboard or other content)
main_content_frame = tk.Frame(root, bg="white")
main_content_frame.grid(row=0, column=1, sticky="nsew")

# Environment panel (right side)
environment_frame = tk.Frame(root, width=200, bg="lightgray")
environment_frame.grid(row=0, column=2, sticky="ns")

# Alerts section at the bottom
alerts_frame = tk.Frame(root, bg="lightgray", height=50)
alerts_frame.grid(row=1, column=0, columnspan=3, sticky="ew")
alert_label = tk.Label(alerts_frame, text="No alerts", bg="lightgray")
alert_label.pack()

# Placeholder for changing the content in the main section
def change_tab(tab_name):
    for widget in main_content_frame.winfo_children():
        widget.destroy()  # Remove previous content
    if tab_name == "Dashboard":
        label = tk.Label(main_content_frame, text="Welcome to the Dashboard", font=("Arial", 16))
        label.pack(pady=20)
    elif tab_name == "Devices":
        label = tk.Label(main_content_frame, text="Manage your devices here", font=("Arial", 16))
        label.pack(pady=20)
    elif tab_name == "Rooms":
        label = tk.Label(main_content_frame, text="Set up your rooms", font=("Arial", 16))
        label.pack(pady=20)
    elif tab_name == "Automations":
        label = tk.Label(main_content_frame, text="Create and manage automations", font=("Arial", 16))
        label.pack(pady=20)
    elif tab_name == "Settings":
        label = tk.Label(main_content_frame, text="Change app settings", font=("Arial", 16))
        label.pack(pady=20)

# Show initial dashboard content
change_tab("Dashboard")

# Display the window
root.mainloop()
