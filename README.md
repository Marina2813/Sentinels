![django notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/2db31367-8f96-4e88-8a8d-a1a75936204d)




# MyHours
MyHours is a sleek and efficient note-taking application designed to streamline your task management experience. Built on the Django framework, MyHoursoffers a user-friendly interface that makes organizing your tasks a breeze.

Features
## Frontend

- Home Page: The heart of MyHours, the home page greets users with a clean and intuitive interface. 

- View Task Page: Need to review your tasks? The view task page provides a comprehensive list of all your notes, neatly categorized and displayed for easy reference, ensuring they never miss an important deadline.

- Add Task Page: Creating new tasks is effortless with MyHours's add task page. Simply input the task details, including title, description, due date, and time, and let MyHour handle the rest. Users can also        assign tasks to specific categories for better organization.

## Task Management Backend:

- Adding Tasks: Behind the scenes, MyHours employs a robust backend system to handle task management efficiently. When a user adds a task through the add task page, the backend processes the input data and stores   it securely in the database, ensuring that the task is recorded accurately.

- Deleting Tasks: Users have the flexibility to remove tasks from their list when they are no longer relevant or necessary. By implementing a delete task functionality, MyHours allows users to easily declutter      their task list with just a few clicks.

- Modifying Tasks: Sometimes, task details may need to be updated or revised. MyHours facilitates task modification by enabling users to edit task information such as title, description, due date, and category.     The backend ensures that any changes made are reflected accurately in the database, maintaining data integrity.

- Changing Task Status: MyHours empowers users to track the progress of their tasks by allowing them to change the status from "To Do" to "Complete" once a task is finished. This functionality provides users with   a sense of accomplishment and helps them stay organized by marking completed tasks appropriately.

## Team members
| [![Marina Rose Shaju](https://github.com/marina2813.png?size=100)](https://github.com/marina2813) | [![Rohit Babu George](https://github.com/xrg360.png?size=100)](https://github.com/xrg360) |
|---|---|
| Marina Rose Shaju | Rohit Babu George |


## Link to product walkthrough
[link to video](https://github.com/Marina2813/Sentinels/assets/86565903/c14bdb79-8ac9-4431-a145-8eb7b954c78d)

## Libraries used
- Django - 5.0.4
- Tailwind

## How to configure
To configure the project, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/Marina2813/Sentinels
    ```

2. Navigate to the project directory:
    ```
    cd your-repo
    ```

3. Create a virtual environment:
    ```
    python -m venv env
    ```

4. Activate the virtual environment:
    - For Windows:
      ```
      .\env\Scripts\activate
      ```
    - For macOS/Linux:
      ```
      source env/bin/activate
      ```

5. Set up the database:
    ```
    python manage.py migrate
    ```

6. Create a superuser:
    ```
    python manage.py createsuperuser
    ```

7. Start the development server:
    ```
    python manage.py runserver
    ```

8. Open your web browser and visit `http://localhost:8000` and plan you day!!!!

Note: Make sure you have Python and pip installed on your system before proceeding with the above steps.
