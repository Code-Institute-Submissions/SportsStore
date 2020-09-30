# *AOB SPORTS STORE*
## MilestoneProject4 - Full Stack Frameworks with Django


Application Demo [AOB Sports Store](https://aobsportsstore.herokuapp.com/)

## Table Of Contents
1. [Description](#Description)
2. [UX](#UX)
3. [UserStories](#UserStories)
4. [Wireframes](#Wireframes)
5. [Features](#Features)
6. [FutureFeatures](#FutureFeatures)
7. [Pages](#Pages)
8. [Testing](#Testing)
9. [Deployment](#Deployment)
10. [Technologies](#Technologies)
11. [ViewProject](#ViewProject)
12. [Acknowledgements](#Acknowledgements)
13. [Disclaimer](#Disclaimer)


## Description

This application is designed to allow for Andrew O Brien Sports Massage & Supplies to advertise and sell his products via the online E-commerce store.
The application gives a direct implication that it is sports orientated from the home image and features responsive designs throughout. 
Dropdown menus indicate available categories to filter products on or optionally a user can choose to view all products and use the search bar within the products section for key words.
The challenge I undertook was to build an ecommerce site for a friend, manage his requirements throughout the process of the build while also trying to improve my skillset as a developer.


## UX

The site has been designed mainly using client feedback. The client outlined that his favourite colour was orange and I took that and integrated it into the design of the website - while not going for the 
brashness of orange, salmon was chosen as a worthy replacement. 
The user is greeted by an incredible HD photograph or sports ground and instantly prompted to look for an appointment or to go view products on the E-commerce site.
Once within the products section users can filter based on category from a convenient drop down menu or use the search option for key words within the name or description of the product. 
The user can then choose to add the item to their card, go to checkout or go back to products from this page. 
Once the user goes to checkout they will be able to remove any item from their cart which also resets the price of their grand total and cart balance. 
The site is linked directly with stripe and uses webhooks for intelligent error management. 


## UserStories

- The store owner will be able to add products
- The store owner will be able to add images on products
- The store owner will be able to edit products
- The store owner will be able to delete products
- The store owner will be able to add, delete and edit categories
- The store owner will be able to identify items as sale items by recategorising into saleitems
- The store owner will be able to grand admin access to other parties to manage the store
- Users will be greeted by a "wow" backdrop (client request)
- Users will be prompted to schedule appointments
- Users will be prompted to go to shop products
- Users will be able to view some background information about the client
- Users will be able to filter based on categories 
- Users will be able to search for key words Ad-hoc and be brought to correct list of products
- Users will be able to add any valid quantity to their cart
- Users will be shown the delivery charges 
- Users will be shown how much they need to spend to get delivery free
- Users will be able to contact the client through the website but not reference his phone or email directly
- Users will be able to navigate through products with ease on laptops, phones, ipads 
- Users will be able to add products to their cart
- Users will be able to see the total of their cart while shopping
- Users will be able to remove products from their cart
- Users will be able to navigate to the checkout app form cart
- Users will be able to navigate back to products from cart
- Users will have the ability to see a breakdown of products they are buying while checking out
- Users will have easy to fill out forms with mandatory fields like email
- Users will be able to pay with full security / peace of mind their details are safe
- Users will be able to see what items are on sale 
- Users will be able to navigate back to the home page by pressing on any of the header icons 


## Wireframes

1. Home Page Desktop [here](wireframes/homedesktop.JPG)
2. Home Page Mobile [here](wireframes/homedesktop.JPG)
3. About Page Desktop [here](wireframes/aboutdesktop.JPG)
4. About Page Mobile [here](wireframes/aboutmobile.JPG)
5. Appointments Desktop [here](wireframes/appointmentsdesktop.JPG)
6. Appointments Mobile [here](wireframes/appointmentsmobile.JPG)
7. Checkout Desktop [here](wireframes/checkoutdesktop.JPG)
8. Checkout Mobile [here](wireframes/checkoutmobile.JPG)
9. Products Desktop [here](wireframes/productsdesktop.JPG)
10. Products Mobile [here](wireframes/productsmobile.JPG)
11. Product Details Desktop [here](wireframes/productdetailsdesktop.JPG)
12. Product Details Mobile [here](wireframes/productdetailsmobile.JPG)
13. Shopping Cart Desktop [here](wireframes/shoppingcartdesktop.JPG)
14. Shopping Cart Mobile [here](wireframes/shoppingcartmobile.JPG)


## Features

- Add products - ability to add products to the site
- Edit products - ability to edit products from the site
- Delete products - ability to delete products from the site
- Buy products - ability to purchase products through the site
- Filter products - ability to filter products on the site
- Search products - ability to search products based on keywords
- View information on client - ability to view an about section on AOB
- Add items to cart - ability to add items to the cart to purchase
- Delete items from cart - ability to delete items from the card before purchase
- Securely checkout - ability to securely checkout using Stripe Payments
- View amount in Cart from any screen - ability to view € amount in card
- Contact client for appointments - ability to contact AOBSports for Sports Massage Appointments
- Carousel of Images on about page - Unfortunately this only works on local environment



## Future Features

Unfortunately my work life was heavily impacted by Covid19 during the course of this project and my worklife balance was greatly affected. 
As a result I did not get the same amount of time as past projects to implement a lot of the features I would have liked. 
The below are features I would like to include in the future:

- User login / Registration
- Emails linked to send production emails to users and owner
- Product admin screens to edit and delete on the site
- Ability for AOBSports to put up available appointments on the site
- Ability for Users to book appointments through the app rather than through emails
- Ability for Users to subscribe to weekly newsletters / training guides from AOB sports
- Ability to use apple pay while on the site on mobile

## pages

1. Home: main page ability to navigate anywhere on the site & prompts user to buy products or book appointments
2. About: gives some background information on AOBsports experience 
3. Products: lists all products available to buy on the site , allows for filtering via categories or via keywords
4. Product details: ability to drill into products to view further details outlined by the seller
5. Appointments: allows users to contact AOBSports with regard to appointment availablility on particular days
6. Special Offers: allows users to view any items that are currently on sale
7. Cart: cart is where products are listed after the user has decided they would like to purchase
8. Checkout: users will need to fill out some basic informatio, they will be able to view their order summary and begin the payments process
9. Payments Screen: Users will be able to pay securely using Stripe payments & integrated webhook functionality
10. Checkout Success : Users will be notified when their orders have been successful
11. Admin Screen: Gives the owner the ability to add, edit, delete products or Categories




## Testing

Test | Outcome
------------ | -------------
W3C HTML validation for HTML elements | Passed
W3C CSS validation for All | Passed
JSHint Javascript Test | Passed
Chrome developer tools (debugging and responsiveness testing -including all devices available) | Passed
Samsung A50 | Passed 
Iphone 7 | Passed 
Iphone X | Passed 
One Plus Nord | Passed
Ipad | Passed
HP Laptop | Passed - Header can double up on some laptops but overall pass
Friends & Family Testing | Passed
Customer | Passed - The customer is happy with the progress so far and will move into phase 2 of development
Responsive Design| Passed
Githubs Debug Log | Passed


Browser Test | Outcome
------------ | -------------
 Chrome | Passed
 Edge/IE | Passed
 Firefox | Passed
 Opera | Passed
 Safari | Passed



 On Screen Tests | Outcome
------------ | -------------
 Home screen | Passed
 Home screen (appointments) | Passed
 Home screen (shop) | Passed
 Home screen (header links) | Passed
 Products screen | Passed
 Products screen (filter categories) | Passed
 Products screen (filter keywords) | Passed
 Products screen (filter all products) | Passed
 Products screen (view products in a list) | Passed
 Products screen (clear image presentation) | Passed
 Products details | Passed
 Products details (clear image presentation) | Passed
 Products details (metadate presentation) | Passed
 Products details (quantity selection) | Passed
 Products details (add to cart button) | Passed
 Products details (go to checkout) | Passed
 Products details (back to products) | Passed
 Main Navigation (All hyperlinks to apps) | Passed
 Main Navigation (header elements link to homepage) | Passed
 Main Navigation (cart updates when product added) | Passed
 Main Navigation (cart updates when product deleted) | Passed
 Checkout | Passed
 Checkout (cart total) | Passed
 Checkout (delivery charges calculated) | Passed
 Checkout (grand total) | Passed
 Checkout (remove button) | Passed
 Checkout (display of metadata) | Passed
 Checkout (keep shopping back button) | Passed
 Checkout (ability to pay) | Passed
 Appointments (ability to fill out contact form) | Passed
 Special Offers (ability to view products on sale) | Passed




## Deployment

GitHub was used to develop the project, store code in the repository and maintain the version control of this project. 
The live demo has been deployed using Heroku and all versions pushed to the master branch on github are automatically deployed the Heroku Master.

The following steps were used to deploy the Wexford Slang Dictionary on Heroku:

1. Created an App Name
2. Logged into Heroku using $ heroku login creating a connection between Github and the Heroku application
3. Checked Heroku Apps to make sure my project was available
4. Created a new Git repository using git init
5. Added my files to the repositary and associated my Heroku application as my master branch(remote master branch)
6. Created my requirements.txt file
7. Created my ProcFile
8. Followed the steps on Boutique_ado to create an AWS S3 Bucket, seems inconsistent - difficult to get working & didn't get feedback from Tutor support.
9. Add my config Vars: SECRET_KEY, DATABASE_URL, STRIPE KEYS, AWS KEYS
10. Added both files to github and pushed to Heroku Master
11. Ran my application using $ heroku ps:scale web=1 to scale dynos
12. Logged into Heroku and set up the Config Variables in the settings > config variables section (IP & PORT)
13. Application Deployed
14. The link generated can be used instantly. The link generated for this site as: https://wexforddictionaryproject.herokuapp.com/
15. I connected my Heroku App to github to automatically deploy from the master branch, I managed the build through github then would test the app through heroku every few commits/pushes. 


N.B. my application was failing in Heroku due to an error in my requirements.txt file not finding module 'storages'. Troubleshooted many issues using the Heroku logs functionality which was very useful in locating the error. 

## Technologies

The project is built using Python, HTML, CSS and Jquery as its main components.

The following are the other Technologies used throughout the build process:
* [JQuery](https://jquery.com)
    - Used to create more robust functionalities in forms and filters 
* [Font Awesome](https://fontawesome.com/)
    - Used for useful icons to provide more intuitive UI.
* [GitHub](https://github.com/)
    - Used to develop, store and share code & Pushed to Heroku master.
* [Balsamiq](https://balsamiq.com/)
    - Used to create the original wireframes for the project.
* [Dev Tools](https://www.google.com/chrome/)
    - Used continuously when building the application & debugging any HTML, CSS & JS issues.
* [CSS Validator](https://jigsaw.w3.org/css-validator/validator)
    - Used to validate CSS code.
* [HTML Validator](https://validator.w3.org/)
    - Used to validate HTML code.
* [Javascript Validator](https://jshint.com/)
    - Used to validate Javascript code.
* [Postgres](https://www.postgresql.org/)
    - Database for Django App on Heroku
* [Heroku](https://dashboard.heroku.com/apps)
    - Used to build, run, and operate my application
* [AWS](https://s3.console.aws.amazon.com)
    - Storage for static files and media
* [Django](https://www.djangoproject.com/)
    - Python Framework for rapid development and design
* [Stripe](https://www.djangoproject.com/)
    - Payments platform for secure payments of products
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/)
    - To style Django Forms



## View Project

* The code used to develop this slang dictionary application can be viewed [here](https://github.com/Murphj99/SportsStore)
* The live version of the application was deployed using [Heroku](https://dashboard.heroku.com/apps/aobsportsstore) and can be viewed here [AOBSports](https://aobsportsstore.herokuapp.com/)


## Acknowledgements
* I got the idea to create an E-Commerce application from [Code Institute](https://www.codeinstitute.net) and used their tutorials to guide the process.


## Disclaimer
* This project was created for educational purposes only.