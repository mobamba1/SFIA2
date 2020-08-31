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

![Jira](./SFIA%202/jira.PNG)

## Refactored
Compared to the first image there are more child task under the tasks in epics, this is due to the underestimation of the project. Each use cases (tasks under epics) were broken down further to help understand what task needs to be completed and also help track my progress on development. 

![Jira2](SFIA%202/jiraRefactored.PNG)


The final board can be seen in this link:
https://rowanowa.atlassian.net/jira/software/projects/SFIA2/boards/5

# Designs:
Initial Project design (Flowchart) - The image below describes how the application will communicate with each other via python HTTP request. This is a rough sketch of what it looks like for I only needed to it as a reference point:
![Flowchart](SFIA%202/flowchart.PNG)

Database (ER Diagram) - The image bellow will represent the final database,the database will not undergo any changes for I will only function is to store the coorginate that was generated but will be used to implement the Create, Read and Delete of the CRUD  functionality.

CI Pipeline:
The pipeline that i currently used was the same one for the firt SFIA project. This is due to the fact that the new techonology we were going to learnt wont be completed until a few before the deadline. This will be refactored later on.
![CIpipeline](SFIA%202/cipipeline.PNG)

## Refactored 
As we go along the academy my understanding of the python http request increases which enables me to implement this new knowledge into the diagram I had show above. Bellow is the update version to provide a better understanding of how the application system will flow. 


Furthermore as I went along developing this web app I had a better understanding of how my services and nodes will interact.
The service diagram is to display how my services will interact with each other, who will be recieving and generating the random letters and numbers.
![serviceDiagram](SFIA%202/service.PNG)

The Node diagram shows what each node will be configured with. These nodes represents as VMs which will need the necessary modules and packages to run the SWARM.
![nodeDiagram](SFIA%202/node.PNG)

Flowchart above was updated to ensure that it took into account the crd (create, read and delete) functionalities that I had included later on. It was necessary to indlude a delete function to remove all the coordinates on the page, for if it is too long then the web user experience will deminish.
![Flowchart2](SFIA%202/flowchartRefactored.PNG)

ER Diagram was also updated as suggested by my superior, as show in the first image above. It only recorded if the user was able to hit the opponent. This was very confusing for the user for they wouln't know what coordinates was generated that led to that outcome. Also because it only generated 2 output (hit or miss) the user might get confused as whether or not they are actually generating any coordinates. The change was very simple which was change the stored data as the coordinates generater and print if output as well.
![ERD](SFIA%202/database.PNG)

CI Pipeline: 
This is the refactored pipeline which includes the docker and ansible into the diagram. Docker is used to compose the containers for both test environment and live environment. However the test enviornment will use the IP address of the jenkins node, while the live will use the manager and workers so that there not no conflicts with the enviornments. Ansible will only be used to configure the nodes of the necessary packages so that they can initiate docker swarm and and stack. 
![cipipeiline2](SFIA%202/cipipelineRefectored.PNG)


# Home Page
The web application only has page which is shown in the image bellow. The page only has one button to generate the random coordinates for the user. This will then display if the user was able to hit the opponent or not.
![Home](SFIA%202/build.PNG)

## Refactored 
As mentioned from in my design I had changed the output to also show the coordinates and added these coordinates to the database so that they are recorded. Also a delete button was included to prevent the page from being over crowded.
![Build](SFIA%202/home.PNG)

# Risk Assesssment
I started off with identifying what could happen during the development of the application to ensure that funcstions as intended without any errors.
![Risk](SFIA%202/RiskA.PNG)

## Refactored 
During the second phases of the project (Deployment) I had to consider what could go wrong during this process. Most of the issues led to the configurations files of the project. 
![Risk2](SFIA%202/RiskARefactored.PNG)
Link to Risk Assessment:https://docs.google.com/document/d/1oGzjYT81CFEZFWN7bKzq7_SW-8O5ANwZyCEEXLfLC4I/edit

# Coverage (Unit Test) and Integration
As part of the MVP we only needed to include the Unit test of the project and ensure that we are achieving 90% or more. In the images bellow it shows that I had achieved higher than required and included the mock test. 
Most of the test were written for both service 1 and 4 for they handle most of the application functionalities, while service 2 and 3 only generate a random letter or number.
Service 1: 
The service was tested if it loads, and mock test was used when grabbing the generated text from servive 2 and 3. 
![Test1](SFIA%202/service1.PNG)

Service 2 and 3:
These services was only tested to see if the output was generated and if it was accessible.
![Test2](SFIA%202/service2.PNG)
![Test3](SFIA%202/service3.PNG)

Service 4:
Unit test was used check if it was accessible through the port, and mock test was used to check what output will be generated (hit or miss).
![Test4](SFIA%202/service4.PNG)

## Refactored 
I had included selinium to do the integration testing. This will simulate how a user would use the application. Which tested both add and delete button. Because of this we were able to identify if the crub functions that I had implemented were working as intended which can be seen in the logs. (create, read and delete)
![Test5](SFIA%202/integration.PNG)

# Deployment
Docker:
Dockerfiles was used to create a costume image for each service to be deployed as a container so that they can be deloyed all at the same time using docker compose.
![Docker](SFIA%202/Docker.PNG)

Docker-compose:
The yaml file was used to deploy all containers at the same time including nginx. The ports are used to set which ports will be used to publish the conatiners, the replicas of the containers that will be deployed.
![Docker2](SFIA%202/dockercompose.PNG)

Ansible inventory:
This file is used to set the groups and varibles for the nodes. This will be used to identify which IP addresses belong to what group. Image of the code will not be shown here for it will expose the IP address. This will be refactored later.


Ansible playbooks:
This yaml file is used to configure what groups set on on the invoronment files, this is to install all the necessary modules and packages for the worker and manager nodes so that they function as intended.
![AnsibleP](SFIA%202/ansibleplaybook.PNG)

Jenkinsfile and scripts:
The jenkinsfile is to initiate the number of builds the system will have. In my project there will only be 3 builds, 1 to build the system for the necessarry modules and step up for docker files to, 2 test setting up the test ennvironment so that all my test will past and initiate, and 3 deploy which is where all my shell commands for my manager node will be when the swarm as already been initiated and needs to deploy all the containers to be spread to the manager and worker nodes.
![Jenkinsfile](SFIA%202/jenkinsfile.PNG)
![Scripts](SFIA%202/jenkinsscripts.PNG)

## Refactored 
I changed the creadentials in my scrips so tha they are hiding from anyone that may want to clone my repository. This is to protect my VM's IP address and they credentials for my database.
![AnsibleI](SFIA%202/ansible.PNG)

# Deployment Log
If you would like to read the Deployment log it can be found the in link bellow. This section will discuss the 3 scripts that were written to create the deployment logs.
Build Script:
In this section it was important to deactivate any environments that may be running to ensure that we start off from fresh. Also another thing that was removed as any images that were build from the previous deployment so that there are no conflicts. ansible is there excuted to setup the packages for the manager and worker nodes which will be useful later on SWARM stage. I also needed to ensure that new images are built and pushed to the docker hub, which is a registry that will store my images which will then be pulled later on the SWARM build. Before pushing it was important we stored all the credentians in jenkins so that it can be used in the scripts without them being hard coded.

Test Script:
Here I had to set up the environment but installing all the requirements using the requirements.txt which holds all necessary packages needed to run the application and test correctly. Also in each build I had to include the credentials for the database such as the URI and secret key so that they can access the database, without this the application wouldn't work. I then had to go into each service's folder to run the test written for them so that they can be separated. The images above shows the results of those test which they recieved 91% or higher for each service. The test script also executes the integration testing which test the crub functionality that included in the application. (create, read and delete) 

SWARM Script:
In this section we needed to ssh into the manager node so that we can control it with shell commands. Because of the first stage we were able to install all the required packages to execute docker commands. The manager node will then pull all the images that were pushed to docker hub. Also we clone the git repository from github (SFIA2) to make sure we have the latest docker-compose file which will be used to execute my stack service. When the stack is then deployed, all we have to do now is check if the service is running as intended.

https://github.com/mobamba1/SFIA2/blob/master/SFIA%202/buildtext.txt


## Known Issues and Future improvements
All refactores made in the code base was only was only see running in the test environment and was not fully deployed using jenkins. (besides the integration testing). This can be implemented in the future.
Would like to add a update button to enable a user to update a coordinate they had generated.
Would also like to add function that allows users to download a text file where they can keep all these coordinates the yare generated.


link to the first SFIA project:
https://github.com/mobamba1/SFIA



















