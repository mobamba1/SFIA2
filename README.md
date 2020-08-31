# SFIA Prject 2: Battle ships
The project will have 4 servicces running; Service 1; where all my python and html code will be written which will be used to communicate with my other services to create an output. Service 2 will create a random letter from A to H. Service 3 will create a random number from 1 to 8. This will produce a 8x8 grid which will simuate the coordinates of the battle ships. Service 4 will then combine service 2 and 3 output to create the coordinate and determine if a ship is located at that position. If it is then it will return "hit" to the service 1 to display. 

## Contents:
* Traking my Progress
* Designs
* Home Page
* Risk Assesssment
* Coverage (Unit Test) and Integration
* Deployment
* Known Issues
* Future improvements

# Tracking my Progress (Jira)
I had used chosen to use Jira to ensure that all my steps are recorded before attempting to create the application. I first started as shown in the image with 1 epic which is to create the application. However as shown later I have started to incorporate other epics to take into account how the system will need to be deployed for it is still part of the development of the project. 

add image under here 
![Jira](./SFIA%202/jira.PNG)

## Refactored
Compared to the first image there are more child task under the tasks in epics, this is due to the underestimation of the project. Each use cases (tasks under epics) were broken down further to help understand what task needs to be completed and also help track my progress on development. 

![Jira](images/Jira.PNG)
![Jira](images/Jira.PNG)

The final board can be seen in this link:
https://rowanowa.atlassian.net/jira/software/projects/SFIA2/boards/5

# Designs:
Initial Project design (Flowchart) - The image below describes how the application will communicate with each other via python HTTP request. This is a rough sketch of what it looks like for I only needed to it as a reference point:
![Jira](images/Jira.PNG)

Database (ER Diagram) - The image bellow will represent the final database,the database will not undergo any changes for I will only function is to store the coorginate that was generated but will be used to implement the Create, Read and Delete of the CRUD  functionality.

CI Pipeline:
The pipeline that i currently used was the same one for the firt SFIA project. This is due to the fact that the new techonology we were going to learnt wont be completed until a few before the deadline. This will be refactored later on.
![Jira](images/Jira.PNG)

## Refactored 
As we go along the academy my understanding of the python http request increases which enables me to implement this new knowledge into the diagram I had show above. Bellow if the update version to provide a better understanding of how the application system will flow. 
![Jira](images/Jira.PNG)

CI pipeline - Though I had not shown a CI pipeline above I had taken into account the CI pipeline I had created for the first SFIA project which had a simple CI pipeline which did not include a artifact which is now implemented in this project for we are using this technology for my project. 
![Jira](images/Jira.PNG)

Furthermore as I went along developing this web app I had a better understanding of how my services and nodes will interact.
The service diagram is to display how my services will interact with each other, who will be recieving and generating the random letters and numbers.
![Jira](images/Jira.PNG)

The Node diagram shows what each node will be configured with. These nodes represents as VMs which will need the necessary modules and packages to run the SWARM.
![Jira](images/Jira.PNG)

Flowchart above was updated to ensure that it took into account the crd (create, read and delete) functionalities that I had included later on. It was necessary to indlude a delete function to remove all the coordinates on the page, for if it is too long then the web user experience will deminish.
![Jira](images/Jira.PNG)

ER Diagram was also updated as suggested by my superior, as show in the first image above. It only recorded if the user was able to hit the opponent. This was very confusing for the user for they wouln't know what coordinates was generated that led to that outcome. Also because it only generated 2 output (hit or miss) the user might get confused as whether or not they are actually generating any coordinates. The change was very simple which was change the stored data as the coordinates generater and print if output as well.
![Jira](images/Jira.PNG)

CI Pipeline: 
This is the refactored pipeline which includes the docker and ansible into the diagram. Docker is used to compose the containers for both test environment and live environment. However the test enviornment will use the IP address of the jenkins node, while the live will use the manager and workers so that there not no conflicts with the enviornments. Ansible will only be used to configure the nodes of the necessary packages so that they can initiate docker swarm and and stack. 
![Jira](images/Jira.PNG)


# Home Page
The web application only has page which is shown in the image bellow. The page only has one button to generate the random coordinates for the user. This will then display if the user was able to hit the opponent or not.
![Jira](images/Jira.PNG)

## Refactored 
As mentioned from in my design I had changed the output to also show the coordinates and added these coordinates to the database so that they are recorded. Also a delete button was included to prevent the page from being over crowded.
![Jira](images/Jira.PNG)

# Risk Assesssment
I started off with identifying what could happen during the development of the application to ensure that funcstions as intended without any errors.
![Jira](images/Jira.PNG)

## Refactored 
During the second phases of the project (Deployment) I had to consider what could go wrong during this process. Most of the issues led to the configurations files of the project. 
![Jira](images/Jira.PNG)

# Coverage (Unit Test) and Integration
As part of the MVP we only needed to include the Unit test of the project and ensure that we are achieving 90% or more. In the images bellow it shows that I had achieved higher than required and included the mock test. 
Service 1: 
The service was tested if it loads, and mock test was used when grabbing the generated text from servive 2 and 3. 
![Jira](images/Jira.PNG)

Service 2 and 3:
These services was only tested to see if the output was generated and if it was accessible.
![Jira](images/Jira.PNG)

Service 4:
Unit test was used check if it was accessible through the port, and mock test was used to check what output will be generated (hit or miss).
![Jira](images/Jira.PNG)

## Refactored 
I had included selinium to do the integration testing. This will simulate how a user would use the application. Which tested both add and delete button.
![Jira](images/Jira.PNG)

# Deployment
Docker:
Dockerfiles was used to create a costume image for each service to be deployed as a container so that they can be deloyed all at the same time using docker compose.
![Jira](images/Jira.PNG)

Docker-compose:
The yaml file was used to deploy all containers at the same time including nginx. The ports are used to set which ports will be used to publish the conatiners, the replicas of the containers that will be deployed.
![Jira](images/Jira.PNG)

Ansible inventory:
This file is used to set the groups and varibles for the nodes. This will be used to identify which IP addresses belong to what group. Image of the code will not be shown here for it will expose the IP address. This will be refactored later.


Ansible playbooks:
This yaml file is used to configure what groups set on on the invoronment files, this is to install all the necessary modules and packages for the worker and manager nodes so that they function as intended.
![Jira](images/Jira.PNG)

Jenkinsfile and scripts:
The jenkinsfile is to initiate the number of builds the system will have. In my project there will only be 3 builds, 1 to build the system for the necessarry modules and step up for docker files to, 2 test setting up the test ennvironment so that all my test will past and initiate, and 3 deploy which is where all my shell commands for my manager node will be when the swarm as already been initiated and needs to deploy all the containers to be spread to the manager and worker nodes.
![Jira](images/Jira.PNG)

# Refactored 
I changed the creadentials in my scrips so tha they are hiding from anyone that may want to clone my repository. This is to protect my VM's IP address and they credentials for my database.
![Jira](images/Jira.PNG)


## Known Issues and Future improvements



link to the first SFIA project:
https://github.com/mobamba1/SFIA



















