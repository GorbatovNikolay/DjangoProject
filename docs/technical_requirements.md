# 1. Goal of the project

The goal of the project is to write a program like Instagram (hereafter - the Program). The Program must have a web
interface. The user can register on the website by email, create posts with images, look posts of other users via a feed
of the latest posts.

# 2. Description of the Program

The program consists of the following functional blocks:

1. Registration, authentication and authorization
2. Functionality of the user

## 2.1. Types of users

The program provides two types of users:
a user (he is both the author and the content consumer)
and a guest (can only see the authorization page, cannot like and see pictures, and visit the user's page).

## 2.2. Registration

The user registration process begins at the login page. Here the user can register, log in as a registered user or
change the forgotten password.

During the initial registration the user must enter:

* email - required, unique field
* password - required field

After entering email gets to the profile settings page.

On that page the user can fill in the following fields:

* account name - required, unique field
* first name of the user - optionally
* last name of the user - optionally
* bio - optionally
* avatar - optionally

## 2.3. Authentication

User authentication is done by email and password.

## 2.4. User functionality

The user after authentication gets access to the functionality of the Program. This functionality consists of the
following blocks:

1. Editing the profile data
2. Creating and editing posts
3. Viewing other users' posts

### 2.4.1 Editing the profile

In this section the user has the ability to edit their profile data - email, account name, password.

It is possible to change the password.

### 2.4.2 Creating and editing posts

Post, published by user, is a photo (from 1 to 10) and user account name (with a link to the user's page). The post can
have a description (max 2200 characters) and tags (max 10).

The user must be able to delete and add new tags after the post has been published.

### 2.4.3 Viewing other users' posts

The user can view other users' posts on the home page or users page.

User can like and unlike other users' posts.

# 3. Suggested technology stack

The following technology stack is proposed to implement the program:

* Backend:
    - Python language
    - Django framework
    - PostgreSQL database


* Frontend:
    - HTML
    - CSS
    - Bootstrap
