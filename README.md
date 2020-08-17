# SFIA Prject 2: Battle ships
The project will have 4 servicces running; Service 1; where all my python and html code will be written which will be used to communicate with my other services to create an output. Service 2 will create a random letter from A to H. Service 3 will create a random number from 1 to 8. This will produce a 8x8 grid which will simuate the coordinates of the battle ships. Service 4 will then combine service 2 and 3 output to create the coordinate and determine if a ship is located at that position. If it is then it will return "hit" to the service 1 to display. 

## Contents:
* Traking my Progress
* Designs
* How to run the application
* Home Page
* Add Page
* Remove and Update Page
* Risk Assesssment
* Coverage (Unit Test) and Integration
* Known Issues
* Future improvements

# Tracking my Progress (Jira)
I had used chosen to use Jira to ensure that all my steps are recorded before attempting to create the application. I first started as shown in the image with 1 epic which is to create the application. However as shown later I have started to incorporate other epics to take into account how the system will need to be deployed for it is still part of the development of the project. 

add image under here 
![Jira](images/Jira.PNG)

# Refactored
Compared to the first image there are more child task under the tasks in epics, this is due to the underestimation of the project. Each use cases (tasks under epics) were broken down further to help understand what task needs to be completed and also help track my progress on development. 

![Jira](images/Jira.PNG)
![Jira](images/Jira.PNG)

The final board can be seen in this link:
https://rowanowa.atlassian.net/jira/software/projects/SFIA2/boards/5

## Designs:
Initial Project design - The image below describes how the application will communicate with each other via python HTTP request. This is a rough sketch of what it looks like for I only needed to it as a reference point:
![Jira](images/Jira.PNG)

Database - The image bellow will represent the final database,the database will not undergo any changes for I will only function is to store the coorginate that was generated but will be used to implement the Create, Read and Delete of the CRUD  functionality.

# Refactored 
As we go along the academy my understanding of the python http request increases which enables me to implement this new knowledge into the diagram I had show above. Bellow if the update version to provide a better understanding of how the application system will flow. 
![Jira](images/Jira.PNG)

CI pipeline - Though I had not shown a CI pipeline above I had taken into account the CI pipeline I had created for the first SFIA project which had a simple CI pipeline which did not include a artifact which is now implemented in this project for we are using this technology for my project. 
![Jira](images/Jira.PNG)


link to the first SFIA project:
https://github.com/mobamba1/SFIA



















