# Crafty
This is a website prototype for our e-commerce website Crafty. Crafty is a website for users to sell and buy custom made clothing, accessories, and props with an emphasis on cosplay. The website features a number of ways to interact with products including a shopping cart, a review option, and a favorites list. Users are able to list any items they'd like to sell and those items will be immediately available for users to interact with.

[Live Link](https://crafty-reze.onrender.com/)

## Technologies
This website uses a combination of many languages, frameworks, and packages to create a working backend API and frontend website. Some of these technologies include
* Python
* Flask
* SQL Alchemy
* React
* Redux
* AWS

## Getting started

1. Clone this repository (only this branch).

2. Install dependencies.

   ```bash
   pipenv install -r requirements.txt
   ```

3. Create a __.env__ file based on the example with proper settings for your
   development environment.

4. Make sure the SQLite3 database connection URL is in the __.env__ file.

5. This starter organizes all tables inside the `flask_schema` schema, defined
   by the `SCHEMA` environment variable.  Replace the value for
   `SCHEMA` with a unique name, **making sure you use the snake_case
   convention.**

6. Get into your pipenv, migrate your database, seed your database, and run your
   Flask app:

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

7. The React frontend has no styling applied. Copy the __.css__ files from your
   Authenticate Me project into the corresponding locations in the
   __react-vite__ folder to give your project a unique look.

8. To run the React frontend in development, `cd` into the __react-vite__
   directory and run `npm i` to install dependencies. Next, run `npm run build`
   to create the `dist` folder. The starter has modified the `npm run build`
   command to include the `--watch` flag. This flag will rebuild the __dist__
   folder whenever you change your code, keeping the production version up to
   date.

## Features
### Product Details
![image](https://github.com/user-attachments/assets/997e02fc-7e50-48bf-9472-4a4debae562e)
Our Product details page features a connection to every other page on the website. It displays the information of an individual product including:
* Information about the User who created it
* Any images associated with the product
* Reviews that have been made for the product as well as the ability for a user to write their own review
* Buttons allowing the user to add the product to their favorites or to their cart

This page required API calls to every feature in our backend and multiple separate updates to the Redux store when any of these features experienced a change.

The following code is how we implemented the display of a products images. It takes an array of the images and sets one as the main image on display. If any of the other images are clicked, that image becomes the new image on display. This code felt clever in its implementation especially because none of us had ever worked with images in this way before

![image](https://github.com/user-attachments/assets/49cef475-f142-4994-9dae-b03daf506b31)

### Reviews
![image](https://github.com/user-attachments/assets/06534007-bf78-4df3-b3e0-f80486b66a04)

Our reviews are listed under each product along side additional product details. If a user is logged in, they have the option of posting a review as well as adding an image to the review, presumably since they had purchased the product. Once a user has posted a review, they have the option to delete or update it
![image](https://github.com/user-attachments/assets/b2a147d5-c6fa-41bc-bf96-ab3b120dde31)
---
![image](https://github.com/user-attachments/assets/06580a77-2740-4d13-b07a-c5a56804338f)

Create a Review:
Our create review thunk makes a fetch request to our backend route to add a review's details into the system and then uses that review's systems to both add functional date information to the response object as well as taking image data and adding it to the newly created review all in one go. The date information allowed us to easily implement a sorting system for the reviews so that new reviews always end up at the top of the reviews page. The image is an optional feature for any customers who want to send examples of what their received product looks like

![image](https://github.com/user-attachments/assets/7257b642-4cf9-41e5-a58d-885473ef79f1)
---
![image](https://github.com/user-attachments/assets/e181ad01-fb66-43e0-8212-c11639d82bb7)

### Listings
The Current Listings page is similarly intertwined with multiple routes and provided a challenge when implementing. This page allows for a user to manage their own listings. They are able to create a listing which, after the data is validated, will appear immediately in the listings page and will be easy to interact with by other users
![image](https://github.com/user-attachments/assets/9657fb25-b3f2-4ccd-91f4-1a816ce4fe79)

The top bar randomly picks out a few listings, taking them off the list and preventing those 5 from showing up in the normal products page. Users are able to create their own listings for a product as well through their current listings tab.
![image](https://github.com/user-attachments/assets/143884ad-be9f-40d6-853a-ff6b09b15cba)

The create a product page has a neat nav bar that will scroll you down to the three sections of the form.

### Shopping Cart
![image](https://github.com/user-attachments/assets/1497d9f7-2ca2-4180-b71b-a61cc53c2835)

Adding a product to the shopping cart lists it in the shopping cart page where you can modify quantity as well as delete a product from the cart or add a product to your favorites. There is currently no payment pages available on live but they could be easily added using whatever credit card API a client would prefer. Clicking the Place your Order button will simply clear the cart currently.

### Favorites
The favorites page is a simple product display page with the options to add the product to your cart or to remove it from your favorites

![image](https://github.com/user-attachments/assets/31826304-30f0-46fd-9daf-de0e6e62d0e1)


## Challenges faced in development
We faced quite a few challenges during this project as a group such as time management, incredibly obscure bugs, and unfortunate typos.

This project was put together both backend and frontend by the three of us in the span of two weeks. There was a lot of anxiety during daily stand ups which we shared with the other group in our cohort. Our progress felt steady but slower and had us questioning our original plan to finish the backend before beginning work on the frontend. We considered working on both the frontend and backends simultaneously but sticking to our timelines and working methodically, we were able to finish the backend in time with very minimal bugs, which made our front end work much smoother after.

We also had two particularly nasty bugs in our code that set us back in our deadlines occasionally. Thankfully we were able to pair program as a team and look through our code using debugging tools and console logs to pinpoint where our code was going wrong as well as a little help from our instructor from time to time. The first bug ended up being a mistake in our destructuring of our Redux state. Because it was a nested object, rest (...) destructuring was still only creating a shallow clone. We fixed that by creating a structured clone of our redux state instead and then modifying that. Our second similar bug was a slight typo in one of our fetch requests where we had an extra backslash (/) at the end which was leading to a failed request.

## Future Features
- Order History page where shopping cart orders are saved and can be reordered
- Preventing Reviews from accounts who have not purchased the product
- Google Maps API to calculate the tax and shipping info for cart items
