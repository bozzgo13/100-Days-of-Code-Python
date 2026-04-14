# 📊 Habit Tracking Project (Pixela API)

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp**. It utilizes the [Pixela API](https://pixela.io/) to track daily habits and visualize them in a "heatmap" style graph, similar to the GitHub contribution calendar.

## 🚀 Features

  * **User Account Creation** on the Pixela platform.
  * **Graph Initialization** to track specific habits (e.g., cycling, coding, reading).
  * **Automated Data Entry** for the current day using the Python `datetime` module.
  * **Pixel Manipulation** (POST, PUT, and DELETE) to manage habit data points.


## 📋 Configuration

Update the following constants in `main.py` with your own information:

  * `USERNAME`: Your unique username.
  * `TOKEN`: Your self-generated API key/password.
  * `GRAPH_ID`: The ID of the graph you want to create/update.


## 🔍 Code Overview

The script demonstrates the full lifecycle of an API-based project:

1.  **POST (User):** Registering a new user on the service.
2.  **POST (Graph):** Defining the graph's units (e.g., kilometers, pages), color, and type.
3.  **POST (Pixel):** Recording a value for today's date. The date is automatically formatted using:
    ```python
    today = datetime.now()
    formatted_date = today.strftime("%Y%m%d")
    ```
4.  **PUT/DELETE:** Methods to update or remove existing data points for a specific day.

## 🔗 Visualization

Once you have successfully posted a pixel, you can view your progress at:
`https://pixe.la/v1/users/YOUR_USERNAME/graphs/YOUR_GRAPH_ID.html`
