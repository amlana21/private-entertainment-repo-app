# Personal Entertainment Repository Organizer  

This is an application to organize personal entertainment repository. Below is a brief functional and technical description about the application.  

## About the Application  
This application helps users to track and organize their personal entertainment repository. The repository can consist of anything like the DVDs they own, on demand movies they own, comics they own, movies they want to watch and are on their watchlist etc. This application will help them track these various lists and have an unified view of what they own, what they want to own. Below are the functionalities supported by the app:  

 ### View list of Entertainment items  
 The app shows an unified list view of all the items entered in the database. It shows different page tabs based on type of items. Each type of item will have its own list view page.  The tabs are dynamic and the item types can be changed through Django admin view.  

 ### Add new items  
 Te app provides the ability for users to add items to the list and under different item categories.  

 ### Search  
 The app provides a dynamic search capability. Users can search titles on the search and search results change automatically based on results found. The search is type ahead search and searches while user is typing.  

 ### Configurable  
 The app provides an admin view via Django admin. The admin view enables users to configure values like if they want to add/track more category of entertainment items. They can add more values and also control access to the application by managing users through the admin.  

 ### Security  
 The app also provides an authentication system using Django auth. It enables users to login logout of the application.  

## Technical Details  
The application is built in Python using Django for the server side web framework. Client side is built using HTML, Javascript.Below are some technical details about the application:  
  - Project Name: entertainment_repository  
  - App Name: repository  

  ### Client Side  
  - Application styles: login.css for login page and styles.css for styling the main page.  
  - Client side functions: app.js  
  - App Pages: Login page: login.html, Home Page: index.html, Add item pop up: additem.html  

 ### Server Side  
  - Database models:  
   - ItemTypes: Category of items like DVD, Movies etc.  
   - ListTypes: Lists like Watchlist, In Progress etc.  
   - SourceType: Source of the item like Shop, On Demand etc.  
   - Items: Item lines containing all the details like name, prices, category etc.  
  - views .py: All the routes and functions which perform various actions like rendering the homepage, adding the item records
  - Database: This uses sqlite3 database. db.sqlite3 is the file which houses the data for the app.  

## Using the application  
Below are high level steps to navigate the application:  
 1. Login to the application
 2. Click on each tab to see a full list of various category of items  
 3. To search, start typing on the search bar on the nav bar. The results will change as the search term is typed. Focussed tab will change accordingly to focus on the first tab with at least one search result.  
 4. To create a new line item, click on the create icon on top right. This will pop up the create form. Fill all the fields and submit the form. It will save the item and open up the homepage  
 5. Once done, click on the logout link to log out of the application.