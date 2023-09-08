# cinema_manager_app
Cinema system design notes 

 

Note 

The following is not a complete design brief. Instead, it is a design file note from the programmer. This incorporates the key points from various meetings and the formal design brief. 

 

Introduction 

The client proposed a basic cinema administration system that manages movies for a cinema and bookings for the movies. This application should have the following sub-systems. 

Cinema administration – manages movies showing at the cinema. 

Movie administration – manages past and present movies shown at the cinema. 

Booking administration – lets customers place bookings. 

Customer administration – tracks and manages customers placing bookings.


Stakeholders 

Local customers – the patrons/audience that will be recorded in the application as a booking for a movie session. 

Operators – the staff that will use the software to manage the cinema, movie, customer and bookings information. 

Developers – the people that created the software and will provide technical support over time. 

Owners –financed the application development and had the final sign-off. 

 

Software functionality 

The implementation should be completely written in Python as a Graphics User Interface (GUI) application, with no other resources needed (apart from supporting libraries). As mentioned above, there will be four sub-systems. 

Cinema administration 

This sub-system retains a record of the movies currently being shown (up to seven) and a record of the prior movies shown. The main sub-system leverages the functionality and data from the other three sub-systems below. 

The operator should be able to manage ALL the data related to the cinema, including the related sub-systems. 


Movie administration 

A movie entry/record only requires a few attributes: a title, running time, genre and rating. These should contain enough information for a customer to make an informed decision regarding whether to watch the movie. 

 

Booking administration 

This interface is mainly used by the operator, but there should be a feature to allow a customer to make a booking themselves. A booking would entail a session on a particular day and for a particular movie. 

Customer administration 

This will be limited information, such as customer name (not necessarily full name), contact number, and possibly email. The customer can manage this through an operator, but there is potential for a customer to edit this information themselves. 

 

Software requirements 

The application, as described below, will be implemented using object-oriented programming with Python. 

The Cinema data contains or references one or more Movie data that will be created using Python classes. The methods in these classes implement their features and behaviours. 


Cinema object details 

Below are the minimum details needed to implement the Cinema object. Additional methods may be required to complete all requirements. 

The Cinema can contain multiple Movies. The Cinema system also contains functionality for adding and removing Movies, summing the minutes of its Movies and accessing its Movie information. 

The Cinema object contains a list of Movie objects and several methods. All these features are local to the Cinema object. 

Potential attributes include the following. 

Movies: this is a list (attribute) only available to the Cinema object and is initially empty. Its role is to contain Movie objects. 

Add a movie: this method requires a Movie object as a parameter. This method will add the given Movie object to the movies list. 

Get Movie names: this is a method that requires no parameters. The method will return the movie names it currently contains. 

Remove a movie: this method requires a movie name as a parameter. It will then find the Movie object in movies with the given name and remove it from the list. (Implement a solution in case the movie name cannot be found when you call this method.) 

Find movie item: this is a method that requires a movie name as a parameter. It will then return the Movie object in the movies list that has the given name. Implement a solution in case the movie name cannot be found when you call this method. 

Find rated movies: this is a method that requires an audience rating as a parameter. It will then return a list of movie names that have the given audience rating. 

Get total minutes: this is a method that requires no parameters. It will return the sum of all the movie minutes in the movies list. 

 

Movie object details 

The Movie object contains at least the attribute’s name, minutes, and an audience rating. You may assume that the movie name is unique (i.e., there will only be one movie with this name). A Movie object further contains methods to set the name, minutes, and audience rating. Examples of ratings may include: “G”, “PG”, “M”, and “AO”. The rating is case insensitive. 

Movies also contain functionality for setting the movie name, running time, and audience rating. 

All these features are local to a Movie object. 

Movie name: this variable contains the name of this Movie object. Initially, the title is "movie name". 

Minutes: this variable contains the length in minutes of this movie. Initially, the minutes is -1. 

Audience rating: this variable contains the name of the audience rating the item is classified as. Initially, the audience rating is "not set". 

Set movie minutes: this is a method that requires a number that is larger than 0 as a parameter. Any other number (even -1) is not valid; consequently, this method will not change anything. Otherwise, this method will set the minutes to the given (valid) number. 

Set audience rating: this method requires an audience rating as a parameter. Audience ratings may only be set once. The method will set the audience rating to the given audience rating only if it has not yet been set. 

Set name and minutes: this is a method that requires a movie name and a ‘minutes’ as parameters. It will then set the name to the given name and the minutes to the given minutes. You do not need to verify that this name is unique. You need to ensure the given minutes is a valid number. 

Show movie details: this is a method with no parameters. It will produce an excerpt of the movie. An excerpt is a single string that contains the name, minutes and audience rating. 


Interface details 

The application allows a user to use the Cinema implementation. The user interaction is through a suitable GUI. 

User interface requirements: The user can then choose from the features in your Cinema and Movie objects. 

Editing Movie information: The application must have an interface to allow the user to edit the details of the existing movies in your cinema. 

Editing Booking information: The application must have an interface to allow the user to edit the details of the existing bookings per movie in the cinema. 

Formatting Audience ratings: The application interface should display the audience ratings in upper case format. 

Note: The requirements and problem description 

Some of the above requirements and the problem statement may contain missing information. This will be ascertained through the use of problem analysis and testing. 

Any missing components or information will be clearly documented and recorded. 

 

Testing 

To ensure the application functions as intended, the following testing will be conducted against the application. 

Unit testing – tested against the functional requirements. 

Integration testing – testing the files, database and general integration of the various sub-systems. 

System testing – make sure everything works on given platforms and environments. 

Acceptance testing – making sure the application works as intended and meets the stakeholders’ or users’ needs. 

 

Application operation and installation 

The current iteration of the application requires at least Python 3.8+ to operate. Owing to the additional feature request by the client for bookings available on the internet, some dependencies were required. 

Flask - Flask is a lightweight Web Server Gateway Interface (WSGI) web application framework. 

Use pip install Flask to install this dependency. 

 

The web-enabled interface is associated with the following. 

app.py – the main program. Use VScode to run or flask run at the command line. 

cinemadb.py – used to create the initial database and populate with sample data. 

templates – HTML pages for the form inputs. 

static – style sheets and other static resources. 

The online booking sub-system was developed by a different development team. As a result, there are integration issues, and this sub-system WILL fail ALL integration testing. 

 

 

Screen models 

Several user interfaces have been proposed and are not indicative of the final product. 

Main screen 

 

Customer administration 

 

Movie administration 

 

Customer administration 

 

 

 

Page models for the internet booking system 

Several pages have been proposed and are not indicative of the final product. 

Initial landing page – not integrated 

 

 

Booking listings 

 

 

Creating a booking 

Graphical user interface

Description automatically generated with low confidence 

 

 

 

 

Viewing a single booking 

Text

Description automatically generated with medium confidence 

Editing a booking 

Graphical user interface

Description automatically generated with medium confidence 
