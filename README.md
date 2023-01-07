
# Django Project - Voting App

The objective of this project is to create a Voting Application using Django.
In order to create a Voting App, there is several steps :

- Home page: in the home page, all the questions will be displayed. In each question, two buttons will be available, the "Vote" button to vote and the "View" button to view the results of the vote. 
- Vote page : this page has to be linked to each vote questions, the user of the website will be able to vote and will automatically be redirected to the results page after voting.
- Results page : this page will gather all the results of the vote and display some graphical stats if possible.
- Create page : and finally, the "Create" page to be able for a user to manually create some questions.

# Progression

06/01/2023 : Start of the project
- Setting up the django project
- Installing the environment because I am using Windows:
```sh
python -m venv env
```
- Setting up the database
```sh
python manage.py migrate
```
- Creating an initial mockup to have an idea first

![alt text](https://i.ibb.co/82JDRRF/2023-01-07-22-14-53-Window.png)

07/01/2023 : Setting up everything using Django
- Creating the form for the "Create" vote page using a model CreateForm
- Setting up the results page to display the results
- Setting up the "Vote" page to vote. The user chooses between three options and the value chosen by the user will be stored thanks to POST method in the form.
Here is the database after creating some questions and voting. We have the id of the question in the beginning, following by the question, the options and the results by the number.
![alt text](https://i.ibb.co/y0Gm8vP/2023-01-07-22-43-01-Window.png)
And the questions are also displaying correctly in the home page:

![alt text](https://i.ibb.co/cvXRznV/2023-01-07-22-51-42-Window.png)

Negative point: only three options available. The user can not create a question with two answers or more than three answers. It is limited to three answers only.